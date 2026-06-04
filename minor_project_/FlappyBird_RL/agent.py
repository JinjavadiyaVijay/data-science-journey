import flappy_bird_gymnasium
import gymnasium as gym
from DQN import dqn
from experience_replay import ReplayMemory

# detect gpu and set gpu 
if torch.cuda.is_available():
    device = "cuda"
else:
    device = "cpu"


def run(self,is_training = True,render = False):
    env = gym.make("FlappyBird-v0", render_mode="human" if render else None, use_lidar=True)
    
    num_state = env.observation_space.shape[0] # input dim
    num_actions = env.actions_space.n # output dim

    policy_dqn = dqn(num_state,num_actions).to(device)
    state, _ = env.reset()

    if is_training:
        memory = ReplayMemory(10000)

    while True:
        # Next action:
        # (feed the observation to your agent here)
        action = env.action_space.sample()
    
        # Processing:
        next_state, reward, terminated, _, _ = env.step(action)
        
        if is_training:
            memory.append((state, action, new_state, reward, terminated))
        
        if terminated:
            break
    
    env.close()