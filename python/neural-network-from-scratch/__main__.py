#! /usr/bin/python

# import numpy as np
import nnfs
import matplotlib.pyplot as plt
from nnfs.datasets import spiral_data
from nn.activations import ReLU, Softmax, Softmax_Loss_categoricalCrossEntropy
from nn.layers import Dense, Layer2, Layer, Layer3
from nn.utils import Loss_CategoricalCrossEntropy, Accuracy
from nn.optimizers import SGD

# it sets the random seed to 0 (by the default),
# creates a float32 dtype default,
# overrides the original dot product from NumPy
# nnfs.init()

if __name__ == '__main__':

    l = Layer([[0.2, 0.8, -0.5, 1],
               [0.5, -0.91, 0.26, -0.5],
               [-0.26, -0.27, 0.17, 0.87]],
              [2, 3, 0.5])

    print(l([1, 2, 3, 2.5]))

    l2 = Layer2([[0.2, 0.8, -0.5, 1],
                 [0.5, -0.91, 0.26, -0.5],
                 [-0.26, -0.27, 0.17, 0.87]],
                [2, 3, 0.5])

    print(l2([1, 2, 3, 2.5]))

    l3 = Layer3([[0.2, 0.8, -0.5, 1],
                 [0.5, -0.91, 0.26, -0.5],
                 [-0.26, -0.27, 0.17, 0.87]],
                [2, 3, 0.5])

    out = l3([[1.0, 2.0, 3.0, 2.5],
              [2.0, 5.0, -1.0, 2.0],
              [-1.5, 2.7, 3.3, -0.8]])
    print("Output shape: {}".format(out.shape))
    print(out)

    X, y = spiral_data(samples=100, classes=3)

    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='brg')
    plt.show()

    # Creating Neural Network
    # First Dense Layer
    dense_l1 = Dense((2, 3))
    # Rectifier Linear Unit Activation
    relu_activation = ReLU()
    # Second Dense layer
    dense_l2 = Dense((3, 3))
    # Create loss function
    # Softmax activation function for output
    loss_activation = Softmax_Loss_categoricalCrossEntropy()
    accuracy_obj = Accuracy()

    # Creates the optimizer
    optimizer = SGD()

    # Train in loop
    for epoch in range(10001):
        X_ = dense_l1(X)
        X_ = relu_activation(X_)
        X_ = dense_l2(X_)
        
        (Y_hat, loss) = loss_activation(X_, y)
        # Calculate model accuracy
        accuracy = accuracy_obj(Y_hat, y)
        if not epoch % 100: print(f'epoch: {epoch}, ' +
            f'acc: {accuracy:.3f}, ' + f'loss: {loss:.3f}')

        # Backward pass
        dense_l1.backward(
            relu_activation.backward(
                dense_l2.backward(
                    loss_activation.backward(Y_hat, y)
                )
            )
        )
        optimizer.update_params(dense_l1)
        optimizer.update_params(dense_l2)

        if not epoch % 100:
            pass

    print(dense_l1.w_grad)
    print(dense_l1.b_grad)
    print(dense_l2.w_grad)
    print(dense_l2.b_grad)
