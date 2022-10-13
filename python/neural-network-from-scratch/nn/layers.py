#! /usr/bin/python

from functools import reduce
import numpy as np

# it sets the random seed to 0 (by the default), 
# creates a float32 dtype default, 
# overrides the original dot product from NumPy
# nnfs.init()

class Node():

    def __init__(self, w, b):
        self.w_ = w
        self.b_ = b

    def activation(self, inputs):
        def __(acc, curr): (i, w) = curr; acc += i * w; return acc
        _ = reduce(__, zip(inputs, self.w_), 0)
        return _ + self.b_

class Layer():

    def __init__(self, weights, bias):
        self.w = weights
        self.b = bias
        self.Y = None

    def forward(self, inputs):
        # Each vector in the weight matrix is taken 1-by-1 against the input
        # To ouput a vector of the weight inner shape

        # To explain the order of parameters we are passing into npdot(), 
        # we should think of it as whatever comes first will decide the output shape. 
        # In our case, we are passing a list of neuron weights first and then the 
        # inputs, as our goal is to get a list of neuron outputs.

        # Note : A  dot product of a matrix and a vector results in a list of dot products.
        return np.dot(self.w, inputs) + self.b

    def __call__(self, *kargs, **kwargs):
        """Compute and return the activation of the layer
        Args:
        -----
        *kargs: list
            List of arguments to pass to the function

        **kwargs: dict
            Dictionary of positional arguments passed to the function

        Returns:
        --------
        Y: list|np.array
            The computed activation value
        """
        self.Y = self.forward(*kargs, **kwargs)
        return self.Y

class Layer2(Layer):

    def __init__(self, weights, bias):
        self.Nodes = [Node(w, b) for w, b in zip(weights, bias)]

    def forward(self, inputs):
        return [n.activation(inputs=inputs) for n in self.Nodes]

class Layer3(Layer):
    def __init__(self, weights, bias):
        super().__init__(weights, bias)


    def forward(self, inputs):
        # We mentioned that the second argument for npdot() is going to 
        # be our transposed weights, so first will be inputs,
        #  but previously weights were the first parameter. 
        # We changed that here. Before, we were modeling neuron output 
        # using a single sample of data, a vector, but now we are a 
        # step forward when we model layer behavior on a batch of data.
        return np.dot(inputs, np.array(self.w).T) + self.b


class Dense(Layer):
    """Create a Fully connected Neural Network

    Args:
    -----
    shape: tuple
        The shape of the layer
    """
    # Layer initialization
    def __init__(self, shape: tuple):
        # Initilize layer weight and biases
        # Note that we’re initializing weights to be (inputs, neurons), 
        # rather than (neurons, inputs). We’re doing this ahead instead of 
        # transposing every time we perform a forward pass, as explained 
        # in the previous chapter
        # np.random.randn produces a Gaussian distribution with a mean of 0 
        # and a variance of 1
        # Generate value between [-1 1]
        # The weights here will be the number of inputs for the first dimension 
        # and the number of neurons for the 2nd dimension
        (n_inputs, n_neurons) = shape
        w_ = .01 * np.random.randn(n_inputs, n_neurons)

        # We’ll initialize the biases with the shape of (1, n_neurons), 
        # as a row vector, which will let us easily add it to the result of 
        # the dot product later, without additional operations like transposition.
        b_ = np.zeros((1, n_neurons))
        super().__init__(w_, b_)
        self.X = None

    # Forward
    def forward(self, inputs):
        """Calculate output values from inputs, weigh and biases
        """
        self.x = inputs
        return np.dot(inputs, self.w) + self.b

    # Backward
    def backward(self, dval):
        self.w_grad = np.dot(self.x.T, dval)
        self.b_grad = np.sum(dval, axis=0, keepdims=True)

        # Input gradients
        self.x_grad = np.dot(dval, self.w.T)
        return self.x_grad
