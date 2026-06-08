from collections import deque
import random

class ReplayMemory():
    # create FIFO queue
    def __init__(self, max_len, seed=None):
        self.memory = deque([],maxlen = max_len)
    
    def append(self, new_exp):
        self.memory.append(new_exp)

    def sample(self, sample_size):
        return random.sample(self.memory, sample_size)
    
    # curr buffer size
    def __len__(self):
        return len(self.memory)
