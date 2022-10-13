function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%
X = [ones(m, 1) X]
% =========================================================================

    % Generic implementation
    input_ = X;
    A = {0, 0};
    last = size(A, 1) + 1;
    layers_theta = {Theta1, Theta2};
    for c = 1:last,
        l_theta = cell2mat(layers_theta(1 , c));
        curr = sigmoid(input_ * l_theta');
        A(c) = curr;
        if c < last,
            size_curr = size(curr);
            curr = [ones(size_curr, 1) curr];
            input_ = curr;
        end;
    end;
    [_, p] = max(cell2mat(A(1, end)), [], 2);

    % Direct implementation
    % input_ = X;
    % l1_a = sigmoid(input_ * Theta1')
    % n = size(l1_a);
    % l1_a = [ones(n, 1), l1_a];
    % l2_a = sigmoid(l1_a * Theta2');
    % [_, p] = max(l2_a, [], 2);
end
