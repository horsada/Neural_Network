import numpy as np

class Perceptron:
    """A single neuron with the sigmoid activation function.
       Attributes:
          inputs: The number of inputs in the perceptron, not counting the bias.
          bias:   The bias term. By defaul it's 1.0."""

    def __init__(self, inputs, bias = 1.0):
        """Return a new Perceptron object with the specified number of inputs (+1 for the bias).""" 
        self.weights = (np.random.rand(inputs+1) * 2) - 1
        self.bias = bias

    def run(self, x):
        """Run the perceptron. x is a python list with the input values."""
        total = np.dot(np.append(x,self.bias), self.weights)
        return self.sigmoid(total)

    def set_weights(self, w_init):
        self.weights = np.array(w_init, float)
       # assert len(w_init) == self.inputs

    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

# AND Gate Test
"""
neuron = Perceptron(2)
neuron.set_weights([10,10,-15])

print(neuron.run([1,1]))
"""

# OR Gate Test
"""
neuron = Perceptron(2)
neuron.set_weights([10,10,-5])

print(neuron.run([0,0]))
print(neuron.run([0,1]))
print(neuron.run([1,0]))
print(neuron.run([1,1]))
"""