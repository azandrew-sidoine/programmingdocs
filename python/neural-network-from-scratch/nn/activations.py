#! /usr/bin/python

import numpy as np
from nn.utils import Loss_CategoricalCrossEntropy
from timeit import timeit

class Activation():

    def __init__(self):
        self.Y  = None

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
        Y: Any
            The computed activation value
        """
        self.Y = self.forward(*kargs,**kwargs)
        return self.Y

class ReLU(Activation):

    def __init__(self):
        super().__init__()
    
    # Forward
    def forward(self, X):
        self.x = X
        # Return the output values fro  the input values using maximum of the list items
        return np.maximum(0, X)

    # Backward
    def backward(self, grad):
        # Since we need to modify the original variable, # let's make a copy of the values first
        self.x_grad = grad.copy()
        # Zero gradient where input values were negative
        self.x_grad[self.x <= 0] = 0

        # Return the gradient with respect to the input
        return self.x_grad


class Softmax(Activation):

    def __init__(self):
        super().__init__()

    # Forward
    def forward(self, X):
        # Get exponentially normalized probabilities
        # We can use this property to prevent the exponential function 
        # from overflowing. Suppose we subtract the maximum value from a 
        # list of input values. We would then change the output values 
        # to always be in a range from some negative value up to 0, as 
        # the largest number subtracted by itself returns 0, and any 
        # smaller number subtracted by it will result in a negative number — 
        # exactly the range discussed above. With Softmax, 
        # thanks to the normalization, we can subtract any value from all of 
        # the inputs, and it will not change the output:
        self.inputs = X
        exp_values = np.exp(X - np.max(X, axis=1, keepdims=True))
        return exp_values / np.sum(exp_values, axis=1, keepdims=True)

    def backward(self, grad):
        self.x_grad = np.empty_like(grad)

        # Enumerate outputs and gradients
        for i, (y_, grad_v) in enumerate(zip(self.Y, grad)):
            # Flatten output array
            y_ = y_.reshape(-1, 1)
            # Calculate the jacobian matrix of the output
            jacobian_matrix = np.diagflat(y_) - np.dot(y_, y_.T)

            # Calculate sample-wise gradient
            # And add it to the array of gradients
            self.x_grad[i] = np.dot(jacobian_matrix, grad_v)
        return self.x_grad


class Softmax_Loss_categoricalCrossEntropy(Activation):

    # Creates activation and loss function objects
    def __init__(self):
        super().__init__()
        self.activation = Softmax()
        self.loss = Loss_CategoricalCrossEntropy()

    # Forward pass
    def forward(self, inputs, y):
        y_pred = self.activation(inputs)
        loss = self.loss(y_pred, y)
        self.Y = y_pred
        return y_pred, loss

    # Backward pass
    def backward(self, grad, y):
        # Number of samples
        s = len(grad)
        # If labels are one-hot encoded,
        # turn them into discrete values
        if len(y.shape) == 2:
            y = np.argmax(y, axis=1)

        # Copy so we can safely modify
        self.x_grad = grad.copy()

        # Calculate the gradient
        self.x_grad[range(s), y] -= 1

        # Normalize gradient
        self.x_grad = self.x_grad / s
        return self.x_grad


if __name__ == '__main__':
    softmax_outputs = np.array([[0.7, 0.1, 0.2],
                              [0.1, 0.5, 0.4],
                              [0.02, 0.9, 0.08]])
    class_targets = np.array([0, 1, 1])

    def f1():
        softmax_loss = Softmax_Loss_categoricalCrossEntropy()
        dvalues1 = softmax_loss.backward(softmax_outputs, class_targets)
        pass

    def f2():
        activation = Softmax()
        activation.Y = softmax_outputs
        loss  = Loss_CategoricalCrossEntropy()
        dvalues2 = activation.backward(loss.backward(softmax_outputs, class_targets))
        pass
    
    t1 = timeit(lambda: f1(), number=10000) 
    t2 = timeit(lambda: f2(), number=10000) 
    print(t2/t1)

    # print('Gradients: combined loss and activation:')
    # print(dvalues1)
    # print('Gradients: separate loss and activation:')
    # print(dvalues2)
    pass