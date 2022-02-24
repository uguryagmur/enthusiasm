import jax.numpy as jnp
from jax import random, jacobian
from typing import List


def softmax(input_array: jnp.ndarray):
    exp_array = jnp.exp(input_array - jnp.max(input_array))
    return exp_array / exp_array.sum()


class LinearDQN:
    def __init__(self, layer_sizes: List[int]):
        key = random.PRNGKey(42)
        self.layers = [random.uniform(key, (layer_sizes[i], layer_sizes[i + 1]), dtype=jnp.float64, minval=0, maxval=0.02) for i in range(len(layer_sizes) - 1)]
        self.gradient = jacobian(self.forward)

    def forward(self, input_array: jnp.ndarray):
        output = jnp.array(input_array, copy=True)
        for i, layer in enumerate(self.layers):
            output = jnp.matmul(output, layer)
            output = jnp.clip(output, a_min=0) if i != len(self.layers) else softmax(output)
        return output

    def update(self, input_array: jnp.array):
        return self.gradient(input_array)
