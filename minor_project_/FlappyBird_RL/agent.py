import flappy_bird_gymnasium
import random
import gymnasium as gym
from DQN import dqn
from experience_replay import ReplayMemory
import itertools
import yaml
import torch
import torch.nn as nn
import torch.optim as optim 

# detect gpu and set gpu 
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


class Agent : 
    def __init__(self,peram_set):
        with open ("perameter.yaml","r") as f:
            all_pera_set = yaml.safe_load(f)
            params = all_param_set[peram_set]

            self.alpha = params["alpha"]
            self.gamma = params["gamma"]
            self.epsilon_init = params["epsilon_init"]
            self.epsilon_min = params["epsilon_min"]
            self.epsilon_decay = params["epsilon_decay"]
            self.mini_batch_size = params["mini_batch_size"]
            self.replay_memory_size = params["replay_memory_size"]
            self.network_sync_rate = params["network_sync_rate"]
            self.reward_threshold = params["reward_threshold"]
           
            self.loss = nn.MSELoss()
            self.optim = None

    def run(self,is_training = True,render = False):
        env = gym.make("FlappyBird-v0", render_mode="human" if render else None, use_lidar=True)
        
        num_state = env.observation_space.shape[0] # input dim
        num_actions = env.actions_space.n # output dim

        policy_dqn = dqn(num_state,num_actions).to(device)
        state, _ = env.reset()

        if is_training:
            memory = ReplayMemory(self.replay_memory_size)
            epsilon = self.epsilon_init

            target_dqn = dqn(num_state, num_actions).to(device)
            # copy the wt & bais vals from policy => target
            target_dqn.load_state_dict(policy_dqn.state_dict())

            step = 0

            self.optim = optim.Adam(policy_dqn.parameters(), lr = self.alpha )

        for episode in itertools.count():

            state,_ = env.reset()
            state = torch.tensor(state, dtype = torch.float, device = device)

            episode_reward = 0
            terminated = False

            while not terminated :
                
                if is_training and random.random()< epsilon :
                    action = env.action_space.sample() # explore
                    action = torch.tensor(action, dtype = torch.float, device = device)
                    
                else:
                    with torch.no_grad():
                        action = policy_dqn(state.unsqueeze(dim = 0)).squeeze().argmax() # exploit
                
                # Next action:
                action = env.action_space.sample()
            
                # Processing:
                next_state, reward, terminated, _, _ = env.step(action.item())

                reward = torch.tensor(reward, dtype = torch.float, device = device)
                next_state = torch.tensor(next_state, dtype = torch.float, device = device)

                if is_training:
                    memory.append((state, action, new_state, reward, terminated))
                    step +=1

                    state = new_state 
                    episode_reward += reward
                print(f"for episode: {episode} => reward :{episode_reward}, epsilon: {epsilon}")

                if is_training:
                    #epsilon decay 
                    epsilon  = max(epsilon * self.epsilon_decay, self.epsilon_min)
            
                if is_training and len(memory)>self.mini_batch_size:
                    #get sample
                    min_batch = memory.sample(self.mini_batch_size)

                    optimize(min_batch,policy_dqn, target_dqn)

                    # sync the network
                    if step > self.network_sync_rate:
                        target_dqn.load_state_dict(policy_dqn.state_dict()) 
                        step = 0                   