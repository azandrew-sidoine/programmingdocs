#! /usr/bin/python

# Stochastic Gradient Descent (SGD) optimizer
class SGD():

    # Initialize the hyper parameters
    def __init__(self, learning_rate = 1.0):
        self.lr = learning_rate

    def update_params(self, layer):
        print('Weight', layer.w)
        layer.w += -self.lr * layer.w
        layer.b += -self.lr * layer.b
    pass