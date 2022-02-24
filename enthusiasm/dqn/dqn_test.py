import numpy as np

from dqn import *


layers = [12, 64, 32, 4]
model = LinearDQN(layers)
input_arr = np.random.uniform(size=(3, 12))
print(model.forward(input_arr))
print(model.update(input_arr).shape)
