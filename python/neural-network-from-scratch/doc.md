# Neural Network From Scratch

- What is a tensor?

A tensor object is an object that can be represented as an array. What this means is, as programmers, we can (and will) treat tensors as arrays in the context of deep learning, and that’s really all the thought we have to put into it.

## Building Neurons

### Dot Product and Vector Addition

When multiplying vectors, you either perform a dot product or a cross product. A cross product results in a vector while a dot product results in a scalar (a single value/number).

NumPy makes performing dot product on matrices very easy for us — treating this matrix as a list of vectors and performing the dot product one by one with the vector of inputs, returning a list of dot products.

### Matrix Product

The matrix product is an operation in which we have 2 matrices, and we are performing dot products of all combinations of rows from the first matrix and the columns of the 2nd matrix

### Transposition for the Matrix Product

Note : A dot product of two vectors equals a matrix product of a row and column vector (the arrows above the letters signify that they are vectors)

Here we introduced one more new operation — transposition. Transposition simply modifies a matrix in a way that its rows become columns and columns become rows

> np.expand_dims() -> adds a new dimension at the index of the axis.

```py
import numpy as np

# Create a array of single dimension
arr = np.array([1,2,3])

print(arr.shape) # (3,)

# Expanding the row dimension of the created array
# Create a multi-dimensional array expanding with a row dimension
# Create a row vector
arr = np.expand_dims(arr, axis=0)

print(arr.shape) # (1, 3) 
```

Note: NumPy does not have a dedicated method for performing matrix product — the dot product and matrix product are both implemented in a single method: npdot().


## Adding Layers

## Activation Functions

- The Step Activation Function

Recall the purpose this activation function serves is to mimic a neuron “firing” or “not firing” based on input information

In a single neuron, if the weights · inputs + bias results in a value greater than 0, the neuron will fire and output a 1; otherwise, it will output a 0:

> y {1 if x > 0; 0 if x <= 0}

- The Linear Activation Function

A linear function is simply the equation of a line. It will appear as a straight line when graphed, where y=x and the output value equals the input.


This activation function is usually applied to the last layer’s output in the case of a regression model — a model that outputs a scalar value instead of a classification.

- The Sigmoid Activation Function

The problem with the step function is it’s not very informative. When we get to training and network optimizers, you will see that the way an optimizer works is by assessing individual impacts that weights and biases have on a network’s output. The problem with a step function is that it’s less clear to the optimizer what these impacts are because there’s very little information gathered from this function. It’s either on (1) or off (0).

The original, more granular, activation function used for neural networks was the Sigmoid activation function, which looks like:

```py
def sigmoid(z):
    # This function returns a value in the range of 0 for negative infinity, 
    # through 0.5 for the input of 0, and to 1 for positive infinity
    return 1 / (1 + exp(-z))
```

- The Rectified Linear Activation Function

The rectified linear activation function is simpler than the sigmoid. It’s quite literally y=x, clipped
at 0 from the negative side. If x is less than or equal to 0, then y is 0 — otherwise, y is equal to x.

> y {x if x > 0; 0 if x <= 0}

Note: This simple yet powerful activation function is the most widely used activation function at the time of writing for various reasons — mainly speed and efficiency.

- The Softmax Activation Function

It's an activation function at the output layer for classification poblems.

The softmax activation on the output data can take in non-normalized, or uncalibrated, inputs and produce a normalized distribution of probabilities for our classes.

In the case of classification, what we want to see is a prediction of which class the network “thinks” the input represents. This distribution returned by the softmax activation function represents confidence scores for each class and will add up to 1. The predicted class is associated with the output neuron that returned the largest confidence score. Still, we can also note the other confidence scores in our overarching algorithm/program that uses this network. For example, if our network has a confidence distribution for two classes: [045, 055], the prediction is the 2nd class, but the confidence in
this prediction isn’t very high. Maybe our program would not act in this case since it’s not very confident.

```alg
Softmax[i,j] = exp(z[i,j]/∑exp(z[i, l]))
```

Note: Exponentiation serves multiple purposes. To calculate the probabilities, we need non-negative values. Imagine the output as [4.8, 1.21, -2.385] — even after normalization, the last value will still be negative since we’ll just divide all of them by their sum. A negative probability (or confidence) does not make much sense. An exponential value of any number is always non- negative — it returns 0 for negative infinity, 1 for the input of 0, and increases for positive values.

## Calculating Network Error with Loss [Log Loss Error Function]

- Categorical Cross-Entropy Loss
 
Categorical cross-entropy is explicitly used to compare a “ground-truth” probability (y or “targets”) and some predicted distribution (y-hat or “predictions”).

It is also one of the most commonly used loss functions with a softmax activation on the output layer.

```alg
Li = -∑ y[i,j]log(y_hat[i,j])
```

Note:
Where Li denotes sample loss value, i is the i-th sample in the set, j is the label/output index, y denotes the target values, and y-hat denotes the predicted values.

Note:
Arrays or vectors like this are called one-hot, meaning one of the values is “hot” (on), with a value of 1, and the rest are “cold” (off), with values of 0.

> np.clip(y_pred, 1e-7, 1 - 1e-7) -> This method can perform clipping on an array of values, so we can apply it to the predictions directly and save this as a separate array

- Accuracy Calculation

While loss is a useful metric for optimizing a model, the metric commonly used in practice along with loss is the accuracy, which describes how often the largest confidence is the correct class
in terms of a fraction

## Derivatives

- Slope

The slope. “Rise over run”

- The Numerical Derivative

This method of calculating the derivative is called numerical differentiation — calculating the slope of the tangent line using two infinitely close points.

We care about the slope of the tangent line because it informs us about the impact that x has on this function at a particular point, referred to as the instantaneous rate of change.

```py
import matplotlib.pyplot as plt
  import numpy as np
def f(x):
    return 2*x**2
# np.arange(start, stop, step) to give us a smoother curve
x = np.array(np.arange(0, 5, 0.001))
y = f(x)
plt.plot(x, y)
colors = ['k', 'g', 'r', 'b', 'c']

def approximate_tangent_line(x, approximate_derivative):
    return (approximate_derivative*x) + b

for i in range(5):
    p2_delta = 0.0001
    x1 = i
    x2 = x1+p2_delta
    y1 = f(x1)
    y2 = f(x2)
    print((x1, y1), (x2, y2))
    approximate_derivative = (y2-y1)/(x2-x1)
    b = y2-(approximate_derivative*x2)
    to_plot = [x1-0.9, x1, x1+0.9]
    plt.scatter(x1, y1, c=colors[i]) 
    plt.plot([point for point in to_plot],
             [approximate_tangent_line(point, approximate_derivative)
                 for point in to_plot],c=colors[i])
    print('Approximate derivative for f(x)', f'where x = {x1} is {approximate_derivative}')

plt.show()
```

- The Analytical Derivative

Analytical approach is a math approach to calculating the derivative, using math function predefined rules.

## Gradients, Partial Derivatives, and the Chain Rule

`The gradient` is a vector of the size of inputs containing partial derivative solutions with respect to each of the inputs.

- Partial derivative

```
f(x,y,z) -> ∂f(x,y,z)/∂x,∂f(x,y,z)/∂y,∂f(x,y,z)/∂z
```

- The Partial Derivative of a Sum

First, we applied the sum rule — the derivative of a sum is the sum of derivatives.

- The Partial Derivative of Multiplication

- The Partial Derivative of Max

We know that the derivative of x with respect to x equals 1, so the derivative of this function with respect to x equals 1 if x is greater than y, since the function will return x. In the other case, where y is greater than x and will get returned instead, the derivative of max() with respect to x equals 0.

- The Gradient

As we mentioned at the beginning of this chapter, the gradient is a vector composed of all of the partial derivatives of a function, calculated with respect to each input variable.

That’s all we have to know abxout the gradient - it’s a vector of all of the possible partial derivatives of the function, and we denote it using the ∇ — nabla symbol that looks like an
inverted delta symbol.

We’ll be using derivatives of single-parameter functions and gradients of multivariate functions to perform gradient descent using the chain rule.

- The Chain Rule

[`This rule says that the derivative of a function chain is a product of derivatives of all of the functions in this chain, for example:`]

```alg
df(g(x))/dx = df(g(x))/dg(x) . d(dg(x))/dx = f'(g(x)) . g'(x)

∂f(g(y, h(x,z)))/∂x = ∂f(g(y, h(x,z)))/∂g(y, h(x,z)) . ∂g(y, h(x,z))/∂h(x,z) . ∂h(x,z)/∂x
```
The chain rule turns out to be the most important rule in finding the impact of singular input to the output of a chain of functions, which is the calculation of loss in our case. 

Working backward by taking the ReLU() derivative, taking the summing operation’s derivative, multiplying both, and so on, this is a process called backpropagation using the chain rule.

> np.zeros_like - It is a NumPy function that creates an array filled with zeros, with the shape of the array from its parameter

- Softmax derivative function


* Softmax derivative: (1)

```alg
∂S[i,j]/∂z[i,k] = {S[i,j] . (1 - S[i,k]) if j=k; S[i,j] . (0 - S[i,k]) if j != k}
```

* Kronecker delta function whose equation is: (2)

```alg
Sys[i,j] = {1 i = j, 0 i != j}
```

* (1) and (2) resolve to:

```alg
∂S[i,j]/∂z[i,k] = S[i,j] . (Sys[i,j] - S[i,k])
```

Note:

> np.diagflat(X) - The diagflat method creates an array using an input vector as the diagonal

```alg
x * np.eye(x.shape[0]) == np.diagflat(x)
```

* Jacobian matrix

The derivative of the Softmax function with respect to any of
its inputs returns a vector of partial derivatives (a row from the Jacobian matrix), as this input influences all the outputs, thus also influencing the partial derivative for each of them

> np.empty_like - This method creates an empty and uninitialized array. Uninitialized means that we can expect it to contain meaningless values

## Optimizers

- Stochastic Gradient Descent (SGD)

The first name, Stochastic Gradient Descent, historically refers to an optimizer that fits a single sample at a time. The second optimizer, Batch Gradient Descent, is an optimizer used to fit a whole dataset at once. The last optimizer, Mini-batch Gradient Descent, is used to fit slices of a dataset, which we’d call batches in our context.