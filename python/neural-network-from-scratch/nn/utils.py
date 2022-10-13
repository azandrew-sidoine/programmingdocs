#! /usr/bin/python

import numpy as np

class Loss():

    def forward(self, y_pred, y):
        raise NotImplementedError

    # Calculates the data and regularization losses 
    # given model output and ground truth values
    def __call__(self, output, y):
        # Sample loss 
        l = self.forward(output, y)

        # Calculate loss mean
        return np.mean(l)

class Loss_CategoricalCrossEntropy(Loss):
    
    def forward(self, y_pred, y):
        # Number of samples in a batch
        s = len(y_pred)

        # Clip data to prevent division by zero
        y_pred_clipped = np.clip(y_pred, 1e-7, 1 - 1e-7)

        # Probabilities for target values
        # only if categorical labels
        if len(y.shape) == 1:
            confidences = y_pred_clipped[range(s), y]
        elif len(y.shape) == 2:
            confidences = np.sum(y_pred_clipped*y, axis=1)
        # Losses
        return -np.log(confidences)

    def backward(self, grad, y):
        # Numbe of samples
        s = len(grad)

        # Number of labels in every samle
        # Use the first sample to find the count
        labels  = len(grad[0])

        # If the labels are sparse, turn them in one-hot vector
        if len(y.shape) == 1:
            y = np.eye(labels)[y]

        # Calculate the gradient
        self.x_grad = -y/grad

        # Normalize gradient
        self.x_grad = self.x_grad / s
        return self.x_grad

class Accuracy():

    def __call__(self, y_pred, y):
        p = np.argmax(y_pred, axis=1)
        if len(y.shape) == 2:
            y = np.argmax(y, axis=1) 
        return np.mean(p == y)

