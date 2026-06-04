import torch
import torch.nn as nn

class dqn(nn.Module):

    def __init__(self,state_dim = 12,action_dim =2, hidden_dim = 256):
        super(dqn,self).__init__()

        self.model = nn.Squential(
            nn.Linear(state_dim,hidden_dim),
            nn.ReLU(),

            nn.Linear(hidden_dim, action_dim)
        )
        
    def forward(self, x):
        return self.model(x)    