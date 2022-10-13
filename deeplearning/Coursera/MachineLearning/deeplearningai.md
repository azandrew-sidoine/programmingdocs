# ML Course By Andrew Ng

- Array indexing:


Matrices:

`S(<Row>, <Column>)`

`s(1, [1,2]) % Select 1st and 2nd column of Row 1`
`s(1, 1:2) % Select range 1:2 column of Row 1`
`s(1, :) % Select all columns of Row 1`
`s(:) % Return a vector of all elements of S`

Multi-dimension:

Use the [col1,col2,col3,...,colp], [col1 col2 col3 ... colp], [start:end], : for selecting range of data as with matrices
`S(<Row>, <Column>, <Dimension|Page>)`

- Reshaping Array:

`B = reshape(<Source>, [Optional<<Row>>, Optional<<Col>>, Optional<<Dimension>>])`

- Permuting

Use the permute function to interchange row and column subscripts on each page by specifying the order of dimensions in the second argument. The original rows of M are now columns, and the columns are now rows.

`P1 = permute(<Source>,[<RowIndex>, <ColIndex>, <PageIndex>])`

Notes:

- Regression problem: Predict continuous values ouput. Predict a next/continuous value knowing a set of values.
- Classification problems: Predict a discret value in a set of output. If the set is made of 2 items(Binary classification), else if items > 2 (Categorical/Classes classification)


--- Connaissance en integration

Soit `f` fonction continue sur l'intervalle [a;b] avec a ~= b. La valeur moyenne de f sur [a;b] est le nombre réel définit par:

`m = 1 / (b - a)∫[a;b]ƒ(x)dx`

## What is Machine Learning?

Two definitions of Machine Learning are offered. Arthur Samuel described it as: "the field of study that gives computers the ability to learn without being explicitly programmed." This is an older, informal definition.

Tom Mitchell provides a more modern definition: "A computer program is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T, as measured by P, improves with experience E."

Example: playing checkers.

E = the experience of playing many games of checkers

T = the task of playing checkers.

P = the probability that the program will win the next game.

In general, any machine learning problem can be assigned to one of two broad classifications:

Supervised learning and Unsupervised learning.

## Supervised Learning

In supervised learning, we are given a data set and already know what our correct output should look like, having the idea that there is a relationship between the input and the output.

Supervised learning problems are categorized into "regression" and "classification" problems. In a regression problem, we are trying to predict results within a continuous output, meaning that we are trying to map input variables to some continuous function. In a classification problem, we are instead trying to predict results in a discrete output. In other words, we are trying to map input variables into discrete categories. 

Example 1:

Given data about the size of houses on the real estate market, try to predict their price. Price as a function of size is a continuous output, so this is a regression problem.

We could turn this example into a classification problem by instead making our output about whether the house "sells for more or less than the asking price." Here we are classifying the houses based on price into two discrete categories.

Example 2:

(a) Regression - Given a picture of a person, we have to predict their age on the basis of the given picture

(b) Classification - Given a patient with a tumor, we have to predict whether the tumor is malignant or benign.

## Unsupervised Learning

Unsupervised learning allows us to approach problems with little or no idea what our results should look like. We can derive structure from data where we don't necessarily know the effect of the variables.

We can derive this structure by clustering the data based on relationships among the variables in the data.

With unsupervised learning there is no feedback based on the prediction results.

Example:

Clustering: Take a collection of 1,000,000 different genes, and find a way to automatically group these genes into groups that are somehow similar or related by different variables, such as lifespan, location, roles, and so on.

Non-clustering: The "Cocktail Party Algorithm", allows you to find structure in a chaotic environment. (i.e. identifying individual voices and music from a mesh of sounds at a cocktail party).

## Model Representation

To establish notation for future use, we’ll use x(i) to denote the “input” variables (living area in this example), also called input features, and y(i) to denote the “output” or target variable that we are trying to predict (price). A pair (x(i), y(i)) is called a training example, and the dataset that we’ll be using to learn—a list of m training examples (x(i), y(i));i=1,...,m—is called a training set. Note that the superscript “(i)” in the notation is simply an index into the training set, and has nothing to do with exponentiation. We will also use X to denote the space of input values, and Y to denote the space of output values. In this example, X = Y = ℝ. 

To describe the supervised learning problem slightly more formally, our goal is, given a training set, to learn a function h : X → Y so that h(x) is a “good” predictor for the corresponding value of y. For historical reasons, this function h is called a hypothesis.

Univariant Linear Regression is also called a Uni-Variant Linear Regression.

`y_pred = h(x) = b + Wx` -> where b and W are parameters of the hypothesis and are detected using the the cost function

`x = (y - b)/W`

## Cost Function

We can measure the accuracy of our hypothesis function by using a cost function. This takes an average difference (actually a fancier version of an average) of all the results of the hypothesis with inputs from x's and the actual output y's.

To break it apart, it is 1/x_hat is the mean of the squares of  h(x(i)) - y(i), or the difference between the predicted value and the actual value.
This function is otherwise called the "Squared error function", or "Mean squared error". The mean is halved 1/2 as a convenience for the computation of the gradient descent, as the derivative term of the square function will cancel out the 1/2 term. The following image summarizes what the cost function does: 

Note: 1/2 is used in cost functions, cause minimizing the half of a cost is like minimizing the cost itself, as we takes derivative in minimization process.

```
cost_func = 1/2M ∑(y_pred - y)**2 # Squared error is the most commonly used function for LR problems, and perform well on data
```

## Cost Function - Intuition I

If we try to think of it in visual terms, our training data set is scattered on the x-y plane. We are trying to make a straight line (defined by h_ø(x)) which passes through these scattered data points. 

Our objective is to get the best possible line. The best possible line will be such so that the average squared vertical distances of the scattered points from the line will be the least. Ideally, the line should pass through all the points of our training data set. In such a case, the value of J(ø0, ø1) will be 0. The following example shows the ideal situation where we have a cost function of 0.

When ø1=1, we get a slope of 1 which goes through every single data point in our model. Conversely, when ø1=0.5, we see the vertical distance from our fit to the data points increase.


## Gradient Descent - Batch gradient descent

Gradient descent Algoritm:

repeat until convergence {
    b := b - LR (1/m)∑(h(x_i) - y_i)
    w := w - LR (1/m)∑((h(x_i) - y_i) * x_i)
}

The Curve of the MSE is a "Convex" Which has only one local minimum, that is the global minimum. Thus There is no need to worry about GD to converge to a false global minimum.


## Linear Algebra in Octave

Note: Octave uses 1 based indexing #t from other programming language used in the pass.

```m
% Creating a 2x3 matrix
A = [1, 2, 3; 4, 5, 6]

% Creating a vector
v = [1, 2, 3]

% Getting the dimension of a matrix n x c
[r, c] = size(A)

% Dimension of vector
d = size(v)

% Length or scalar length of the vector
l = length(v)

% Array indexing
value = A(2, 3)


% Initialize matrix A and B 
A = [1, 2, 4; 5, 3, 2]
B = [1, 3, 4; 1, 1, 1]

% Initialize constant s 
s = 2

% See how element-wise addition works
add_AB = A + B 

% See how element-wise subtraction works
sub_AB = A - B

% See how scalar multiplication works
mult_As = A * s

% Divide A by s
div_As = A / s

r = s / A % Is Wrong, can't divide a scalar by a matrix. The order of the variables must be respect when performing such operation, else use 1/s * A

% What happens if we have a Matrix + scalar?
add_As = A + s % Works the same as the numpy broadcasting
```


Note: Linear Algebra trick

x = [2104, 1416, 1534, 852] h(x) = -40 + 0.25x -> [1, 2104; 1, 1416;1, 1534;1, 852] * [-40, .25] = y
The eqation above helps in finding an y vector.

> Predictions = Data_Matrix * ParametersMatrix ---> Where Data_Matrix = X and Predictions = Y

```m
% Matrix by vector multiplication

% Initialize matrix A 
A = [1, 2, 3; 4, 5, 6;7, 8, 9] 

% Initialize vector v 
v = [1; 0; 0] 

% Multiply A * v
Av = A * v
```

Note: Multiplying matrixes by vectors returns a vector

Note : Linear Algebra Tricks

x = [2104, 1416, 1534, 852]

With 3 competing Hypotheses:
y_1 = -40 + 0.25x
y_2 = 200 + 0.1x
y_3 = -150 + 0.4x

Donne:

[1, 2104; 1, 1416;1, 1534;1, 852] * [-40, 200, -150; .25, .1, .4] = [y_1, y_2, y_3] ---> Wher y_1, y_2, y_3 are matrixes representing the return values y of each hypotheses

```m
% Initialize a 3 by 2 matrix 
A = [1, 2; 3, 4;5, 6]

% Initialize a 2 by 1 matrix 
B = [1, 2; 7/2, 5] 

% We expect a resulting matrix of (3 by 2)*(2 by 1) = (3 by 1) 
mult_AB = A*B

% Make sure you understand why we got that result
```

```m
% Matrix multiplication and Identity matrix function
% Initialize random matrices A and B 
A = [1,2;4,5]
B = [1,1;0,2]

% Initialize a 2 by 2 identity matrix
I = eye(2)

% The above notation is the same as I = [1,0;0,1]

% What happens when we multiply I*A ? 
IA = I*A 

% How about A*I ? 
AI = A*I 

% Compute A*B 
AB = A*B 

% Is it equal to B*A? 
BA = B*A 

% Note that IA = AI but AB != BA
```

--- Matrices inverse and Transpose

Note : Only square matrix have inverses

A (M x M) matrix, A has inverse named Inv_A if and only if exist tq:
A * Inv_A = Identity_Matrix

```m
% Initialize matrix A 
A = [1,2,0;0,5,6;7,0,9]

Inv_A = pinv(A)

Id_ = A * Inv_A

% Transpose A 
A_trans = A'

% Take the inverse of A 
A_inv = inv(A)

% What is A^(-1)*A? 
A_invA = inv(A)*A
```

```m
% Octave element-wise operations on matrixes and scalar types

M = [1,2,3; 4,5,6]

L = [-1,-2,3; -4,-5,-6]

% Element-wise multiplication
D = M .* L

% Element-wise division 
D = M ./ L

% Element-wise square
M = M .^ 2

% Element wize log
v = [1, 2, 3]
logV = log(v)

% Element-wise exponentiation
expV = exp(v)

% Element-wise absolute value
absV = abs(v)

$ Element-wise negation
minusV = -v % Same as -1 * v
```

--- Octave special matrixes

```m

% Zeros-like matrix
z = zeros(n, m)

% Ones-like matrix
o = ones(n,m)

% Uniformed randomly generated matrix
r = rand(n, [m]) % use 1 param for squared matrix

% Normal rand
r = randn(n, [m])

% Identity matrix

i = eye(n, [m])

% Merging vectors into matrixes

A = [1,2,3]
B = [4,5,6]

V = [A;B] % Create 2-D (2 x 3) Matrix
V = [A B] % Create 1-D Vector with values from A and B
```

--- Range operator

```m

% evenly ranged arrays

% start: [increments] : stop % The increments is optional
r = 1 : 2 : 10
```

--- Indexing

```m
% ij indexing
s = [1,2,3; 4,5,6]

s(1,1) % Returns 1

s(1, [1,2]) % Select 1st and 2nd column of Row 1
s(1, 1:2) % Select range 1:2 column of Row 1
s(1, :) % Select all columns of Row 1
s(:) % Out all elements of S in a single vector
```

--- String Formatting

```m
str = sprintf() % Works like c-version sprintf
```

--- Maths

Note: For matrixes, Dimension 1 is the row dimension and Dimension 2 is the column.

% max(input, [], dimension)

% max(input(:)) - Return the maximum of the entire matrix

% sum(matrix_input, dimension) - Perform a rowise and column-ise sum

```m
ceil(x) % Round up x to the nearest whole number
floor(x) % Round down x to the nearest whole number
round(x) % Round x to the whole number
max(x) -> [value,index] % Highest value in a vector
min(x) -> [value,index] % Lowest value in a vector
sqrt() % Square root of x
sum(x) % Sum up all values of the matrix 
```

--- Loading data in Octave

Support `cd, ls, dir, pwd` shell commands

```m
% Load or read data from a file
r = load("path/to/file")

% Saving value to a file
save("Path/To/File", data)

% Temporary files
% They are files that are deleted when octave closes
handle = tmpfile

save("Path/To/File", data)
```

--- Control statement

==(Equals), !=(Not Equals), ~=(Not Equals), >; <; <=; >=

```
% If statement
if condition,
% Provide implementation
elseif expression,
% Provide implementation elseif
else
% Otherwise do else
end;

x = 10

if x > 5,
disp("X is larger than 5")
end;

% For loop using Range
for i = 1:10,
% ...Code
end;

% For loop with vectors
v = [1,2,3,4,5]

for i = v,
% ... Code using i value
end;

% While loop
while condition,
% Perform action
% Update condition checker
end;

while true,
v = v + 1
if v > 8,
% Perform action
break; % Jump out of the loop
% end of if statement
end;
% end of while statement
end;
```

--- Functions

```m
% Function definition 

function func = func_name(param)
    % Function definitions
endfunction


function r_value = func_min(x)
    r_value = x(1);
    for i = 2:length(x),
        if x(i) < ret,
            ret = x(i)
        end;
    end;
endfunction


% Multi value return function
function [low, high] = func_name(x)
    % Write function definition
endfunction

function [low, high] = func_min_max(x)
    low = x(1);
    high = x(1)
    for i = 2:length(x),
        if x(i) < low,
            low = x(i)
        elseif x(i) > high,
            high = x(i)
        end;
    end;
endfunction
```


--- Error checking/Validation

```m

nargin - Check if param is a variable with the number of argument passed to the function or to octave

isvector(x) - Check if the variable is a vector

error("Provide error")
```

--- Octave Logical operators

~=, ==, &&, ||

--- Plotting and Histograms

```m
hist(<Matrix|Vector>, <Unit>)
```

% plot(x_axis, y_axis, color)

```m

% Plotting signal data

x = [0:.01:.98]
y1 = sin(2 * pi * 4 * x)

figure(1); plot(x, y1, 'b'); % Plot x and y variable

y2 = cos(2 * pi * 4 * x)
figure(2); plot(x, y2, 'r'); % Plot x and cos(8π * π)

xlabel(<X_Axis_Label>) % Label of the x axis

ylabel(<Y_Axis_Label>) % Label of the y axis

legend('sin', 'cos')

title('Plot Title')

% Save the generated plot to a PNG file
print -dpng '<PlotName>.png'

% Close the plotted window
close

% Subplotting
subplot(1, 2, 1); Divides plot into 1x2 grid, access first element
plot(x, y1)
subplot(1, 2, 2); Divides plot into 1x2 grid, access second element
plot(x, y2)
clf; % Clear the plotting window

imagesc(<Matrix>), colorbar, colormap gray; % Plot an image in the grayscale range value
```

--- Moving data arround using Octave

Use `load` and `save` commands to load and save data using octave.

> save "path/to/file" variable --ascii ---> Save data in Text format

--- Removing variable in global scope

> clear variable name

--- Functional API

```m

a = [1, 15, 2, .5]

% List of element less than a value
[r,c] = find(a < 3)
```


--- Vectorization

```m
```

## Week 2

### Multiple features

x_1(4) - 4th feature of the first training measured item.

Hypothesis notation of multiple feature Lin. Reg.

(1) -> h(x) = ø0 + ø1x_1 + ø2x_2 + ... + ønx_n

With:
{
    x_0 = 1,
    X = [x_0, x_1, x_2, ..., x_n] £ R(n+1)
    ø = [ø0, ø1, ø2, ..., øn]  £ R(n+1)
}

(1) can be written as h(x) = Transpose(ø)*X

### Gradient for Multiple Variables

Recall:

J(ø0, ø1, ø2, ..., øn) = 1/2m∑(h(x(i)) - y(i))**2

Gradient Descent: n >= 1

Repeat Until Converge {
    for j:= 0...n {
        øj := øj - LR(1/m∑(h_ø(x(i)) - y(i)) * x_j(i))
    }
}

### Gradient Descent in Pratice I - Feature Scaling

Normalization, which is scaling the feature to a similar range of value, help gradient descent to converge faster

--- Feature scaling

Rule of thumbs: Get every feature between a `-1 <= x(i) <= 1` or a scale close to [-1] and [1]

--- Mean Normalization

Replace x_i with `(x_i - µ_i)/(max_value_i - min_value_i)` to make features have approximately zero mean.
Note: Does not apply to `x0=1`

Note: `(max_value_i - min_value_i)` can be the standard deviation also

### Gradient Descent in Pratice II - Learning Rate

If the J_ø is increasing, One must adjust the LR of the gradient descent.

For LR Try:
..., .001, .003, .01, .03, .1, ...

### Features and Polynomial Regression

Note: Don't just stick to input data provided feature, Else try to create or find a feature that combine 2 or 3 pre-existing features and apply Lin. Reg. to it as well.

### Normal Equation

Normal Equation : Method to solve for ø of the J(ø) Cost function analytically.

ø = Inverse(Transpose(X) * X) * Transpose(X) * Y

When using Normal Equations, Feature squaling is not required.

GD:
Pros - Works well even when n is large

Cons - {Need to choose LR, Needs many iterations}

Normal Equation:
Pros - {No need to choose LR, Don't need to Iterate}
Cons - {Slow if n is large cause need to compute Inverse(Trans(X)*X)}.

Note : If n(Number of features) > 10000, prefer usage of gradient descent.

For Classification and Logistic Regression problems, Normal Equations does not work.


## Classification 

To attempt classification, one method is to use linear regression and map all predictions greater than 0.5 as a 1 and all less than 0.5 as a 0. However, this method doesn't work well because classification is not actually a linear function.

The classification problem is just like the regression problem, except that the values we now want to predict take on only a small number of discrete values. For now, we will focus on the binary classification problem in which y can take on only two values, 0 and 1. (Most of what we say here will also generalize to the multiple-class case.) For instance, if we are trying to build a spam classifier for email, then x (i) may be some features of a piece of email, and y may be 1 if it is a piece of spam mail, and 0 otherwise. Hence, `y∈{0,1}`. `0 is also called the negative class`, and `1 the positive class`, and they are sometimes also denoted by the symbols “-” and “+.” Given x(i), the corresponding y(i) is also called the label for the training example.

### Hypothesis Representation

We will use the sigmoïd function to perform the logistic regression.

Note: Sigmoïd Function == Logistic Function

`sig(z) = 1/1 + exp(-z) `---- When z -> -∞ sig(z) -> 0, When z -> +∞, sig(z) -> 1; When z -> 0, sig(z) -> .5.

Note: `z = Transpose(ø)*X` --- Linear Regression

Note: `h(ø)_x = sigmoid(Transpose(ø)*X)`

Note: 
The function g(z), shown here, maps any real number to the (0, 1) interval, making it useful for transforming an arbitrary-valued function into a function better suited for classification.

-- Interpretation

h_ø(x) = sig(z) = P(y=1|x; ø) --- Probability that y=1 given x, parameterized by ø.

Probability interpretation:

`P(y=0|x;ø) + P(y=1|x; ø) = 1 => P(y=1|x; ø) = 1 - P(y=0|x;ø) => P(y=0|x;ø) = 1 - P(y=1|x; ø)`

### Decision Boundary

With any `z >= 0, g(z) >= .5` => h_ø(x) = `g(Transpose(ø) * X) >= .5, Transpose(ø) * X >= 0`

With any `z <= 0, g(z) <= .5` => h_ø(x) = `g(Transpose(ø) * X) <= .5, Transpose(ø) * X <= 0`

The decision boundary is the function g(z) = .5


### Cost Function

Fit parameters ø to the logistic regression.

Recall:

- Linear Regression: J(ø) = 1/2m * ∑ (h(ø)_x - y)**2 => `J(ø) = 1/m * ∑ 1/2 * (h(ø)_x - y)**2`

Suppose:
`Cost(h(ø)_x, y) = 1/2 * (h(ø)_x - y)**2 => J(ø) = 1/m∑Cost(h(ø)_x - y)`

Because Sigmoid function is not a linear/convex function, this cost does not work well in finding global minima using gradient descent (Cause, the cost function will end up with multiple local minima)

Logistic regression cost function:

`Cost(h(ø)_x, y) = { -log(h(ø)_x) if y=1;  -log(1 - h(ø)_x) if y=0}`

Recap:
`Cost(h(ø)_x, y) = 0 If h(ø)_x = y`
`Cost(h(ø)_x, y) -> ∞ If y=1 and h(ø)_x -> 0`
`Cost(h(ø)_x, y) -> ∞ If y=0 and h(ø)_x -> 1`


### Simplified cost function & Gradient Descent

`Cost(h(ø)x, y) = -y * log(h(ø)_x) - (1-y)log(1-h(ø)_x)` -> Because y elementOf {0, 1}

Therefore the cost function is written as follow:

`J(ø) = -1/m ∑ (y * log(h(ø)_x) + (1-y) * log(1 - h(ø)_x)` -> It's a function derived from

Vectorized implementation:

`J(ø) = 1/m * ∑(-Transpose(y)log(h) - Transpose(1 - y)log(1 - h))`

the maximum likelyhood estimation statistic property.

Gradient descent: Try to find theta which minimize J(ø)

Repeat until converge: {
    `ø = 1/m ∑ (h(ø)_x - y) x`
}

Vectorized implementation:

`ø = ø - (LR/m Transpose(X) (h(ø)_x - y)`

Looks like linear regression but h(ø)_x = sigmoid(Transpose(ø)x)

### Advanced Optimization

Octave provide advance optimization algorithm alternatives to Conjugate Gradient, BFGS, L-BFGS

```m

function [jVal, gradient] = <CostFunctionName>(theta)
    jVal = ... % Rvalue of the cost function

    gradient = ... % Compute/Calculate the gradient using vectorized impl


% Using the cost function to calculate the theta values and Gradient using optimized algos

options = optimset('GradObj', 'on', 'MaxIter', 100)

initial_theta_val = zeros(2, 1) % Theta is 1-D vector of N values

[optTheta, functionVal, exitFlag] = fminunc(@CostFunctionName, initial_theta_val, options)

% optTheta -> The optimal value of theta for costFunc to converge
% functionVal -> R Value of the cost function
% exitFlag -> 1 if cost function well-converge
```

### Multiclass Classification: One-vs-all

It comes in to convert the classification to a binary classification for each class.
Find the probability of item being of class 1, 2, 3, ... etc.

`h(ø)_x  = P(y=i|x; ø) where (i=1, 2, 3, ..etc)`

Train a logistic regression classifier `h(ø)_x_(i)` for each class `i` to predict the probability y=i

On a new input x, to make prediction, pick class i that maximizes `h(ø)_x`: `max(h(ø)_x)`

```alg
y elementOf {0, 1, 2, ..., n}

For each element of {0, 1, 2, ..., n}:
Find: h(ø)_x(element) = P(y=element|x; ø)

prediction = max(h(ø)_x)
```

## The problem of overfitting

This terminology is applied to both linear and logistic regression. There are two main options to address the issue of overfitting:

1) Reduce the number of features:
- Manually select which features to keep.
- Use a model selection algorithm (studied later in the course).

2) Regularization
- Keep all the features, but reduce the magnitude of parameters øj.
- Regularization works well when we have a lot of slightly useful features.


### Cost Function

The λ, or lambda in the cost function, is the regularization parameter. It determines how much the costs of our theta parameters are inflated.

Regularized Linear Regression:

`J(ø) = 1/2m ∑[(h(ø)_x - y)**2 + ß∑ø(j)]`

Gradient descent:

Regularized gradient descent consist of updating the previous value of theta using a value closer to 1, and reducing
it by the gradient on each iteration:

Repeat j = [] {
    ø_0 = ø_0 - LR/m * ∑(h(ø)_x - y)x_0
    ø_j = ø_j( 1 - LR * ß/m) - LR/m * ∑(h(ø)_x - y)x_j
}

Normal Equation:

Fn =  Transpose(X) * X + ß[[0 0 ...0], [0 1 0 ... 0], [0 0 1 0 ...]...]
ø = Inverse(Fn) * Transpose(X) * Y

Note: Fn will be inversible if if ß > 0, therefore it solve the inversibility issue with the normal equation

## Neural Network

Recent resurgence : State-of-the-art technique for many applications.

Note : If a network has s(j) units in a layer j, s(j+1) units in layer j+1, then ø(j) will be of dimension `s(j+1) x s(j) + 1`

NN: [x_0,x_1,x_2] -> [<HiddenLayers>] -> h_ø(x)

`a(j)i="activation" of unit i in layer j`
`Θ(j)=matrix of weights controlling function mapping from layer j to layer j+1`

### Model Representation

Vectorized implementation of the NN:

`z(j) = ø(j-1) . X`
`a(j) = Activation(z(j)) # Logistic_Function(z(j))`

-- Add the bias term

`a(j)0 = 1 -> a(j) ElementOf R(j+1)`
`z(j+1) = ø(j)a(j)`
`h(ø)x = a(j+1) = g(z(j+1))`

### Applications

--- Example and Intuitions

AND:
    ø = [-30, 20 20] x1, and x2 -> g(-30 + 20 * x1 + 20 * x2)

NOR:
    ø = [10, -20 -20] x1, and x2 -> g(10 -20 * x1 - 20 * x2)

OR:
    ø = [-10, 20 20] x1, and x2 -> g(-10 -20 * x1 - 20 * x2)

XOR:
   NN With NOR(AND + OR )


## Cost function and Backpropagation

### Cost function

Training sets -> {(x(1), y(1)), (x(2), y(2)), ..., (x(m), y(m))}

L -> Number of layer in the network

s_l -> No. of units(not counting the bias unit) in Layer l. (Number of neurons)

--- Classification Problems

- Binary Classification: Output_Unit = h_x(ø) = K -> With K number of unit in output layer, K ElementOf {0,1}

Multi Classification(K CLasses): Output_Unit = h_x(ø) = K -> With K number of unit in output layer, K ElementOf {k > 2}

Cost function:

It consist of the SUM of the sum of the error of each output unit.

----------------------------------------------------------------------------------
J(Θ)=−1m∑i=1m∑k=1K[y(i)klog((hΘ(x(i)))k)+(1−y(i)k)log(1−(hΘ(x(i)))k)]+λ2m∑l=1L−1∑i=1sl∑j=1sl+1(Θ(l)j,i)2
----------------------------------------------------------------------------------

### Back propagation

For each layer starting from output layer:
With output layer L=4;
`error(L) = a(L) - y`
`error(L-1) = Transpose(ø(L-1)) * error(L) .* g'(Z(L-1))` -> With g'(Z(L-1)) = z .* (1-z)
`error(L-1) = Transpose(ø(L-2)) * error(L-1) .* g'(Z(L-2))`
...

## Gradient Checking

`∂J(ø)/∂ø = J(ø + œ) - J(ø - œ)` / 2œ with œ=10e-4

3,09 - 2.97 = 0.12 / 0.02

3,5643 - 2,9403

```m
for i = 1:n:
   thetaPlus = theta;
   thetaMinus = theta;
   gradApprox(i) = (J(thetaPlus(i) + EPISILON) - J(thetaMinus(i) - EPISILON)) / 2 * EPSILON;
end;
% Check that gradApprox approx= DVecFromBackProp

epsilon = 1e-4;
for i = 1:n,
  thetaPlus = theta;
  thetaPlus(i) += epsilon;
  thetaMinus = theta;
  thetaMinus(i) -= epsilon;
  gradApprox(i) = (J(thetaPlus) - J(thetaMinus))/(2*epsilon)
end;
```

### Random initialization

- rand(input_r, input_c) : Generate an (input_r x input_c) matrix of values between [0,1].

```m
theta = rand(input_r, input_c) * (2 * DISTRIBUTION_RANGE) - DISTRIBUTION_RANGE % theta [-DISTRIBUTION_RANGE, DISTRIBUTION_RANGE]
```

### Recall

--- Pick network architecture:

> No. Of Input unit - Dimension of x(i) features
> No. of output units - Number of class
> If Hidden layers > 1, all hidden layers must have the same no. of units.

--- Training neural network

> Randomly initialize weights
> Implement forward propagation to get h(x(i))_ø for any x(i)
> Implement code to compute cost function J(ø)
> Implement backprop to compute partial derivatives ∂(J(ø))/∂(ø(L))

for i = 1: NumberOfTraningSet {
    - Perform forward propagation using example (x(i), y(i))
    - Get activation a(L) and Delta(L)
    - Compute the gradient vector
}

> Use gradient checking to check backprop rvalues and numerical estimate
> Disable gradient checking cause of it being computational slow
> Use GD or advanced optimization method with backprop to try to minimize J(ø) as a function of parameters.
