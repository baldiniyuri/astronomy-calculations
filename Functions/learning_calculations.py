import numpy as np


class LearningCalculation:
    def __init__(self, x: float, w: float, b: float, learning_rate: float):
        self.x = x.reshape(1, -1)
        self.w = w
        self.b = b
        self.learning_rate = learning_rate

    def linear_model(self):
        # z = w⋅x + b
        z = np.matmul(self.w, self.x.T) + self.b
        return z

    def linear_function(self):
        # f(x) = y = 2x - 2
        y = 2 * self.x - 2
        return y

    def mean_squared_error(self, y_true):
        y_pred = self.linear_function()
        mse = np.mean((y_true - y_pred)**2)
        return mse

    def update_weights(self, dw):
        # w := w - A dj(w)/dw
        self.w -= self.learning_rate * dw

    def forward_propagation(self, weights):
        z = self.x
        activations = [z]
        for i in range(len(weights)):
            z = np.dot(z, weights[i])
            a = self.sigmoid(z)
            activations.append(a)
        return activations

    def weight_updates(self, weights, activations, deltas):
        for i in range(len(weights)):
            weights[i] -= self.learning_rate * np.dot(activations[i].T, deltas[i])
        return weights

    def back_propagation(self, y_true, weights):
        activations = self.forward_propagation(weights)
        deltas = [activations[-1] - y_true]
        for i in range(len(weights)-1, 0, -1):
            delta = np.dot(deltas[-1], weights[i].T) * self.sigmoid_derivative(activations[i])
            deltas.append(delta)
        deltas.reverse()
        weights = self.weight_updates(weights, activations, deltas)
        return weights

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def sigmoid_derivative(self, a):
        return a * (1 - a)


def start_learning():
    # Create input data (x), weights (w), and bias (b)
    x = np.array([[1.0], [2.0], [3.0]])
    w = np.array([[0.1], [0.2]])
    b = 0.3

    # Instantiate the LearningCalculation class with x, w, and b
    learning_calc = LearningCalculation(x, w, b)

    # Compute the linear model output
    z = learning_calc.linear_model()
    print("Linear model output (z):", z)

    # Compute the linear function output
    y = learning_calc.linear_function()
    print("Linear function output (y):", y)

    # Compute the mean squared error
    y_true = np.array([[1.0], [2.0], [3.0]])
    mse = learning_calc.mean_squared_error(y_true)
    print("Mean squared error (MSE):", mse)

    # Update the weights using the gradient (dw) and learning rate (A)
    dw = np.array([[0.1], [0.2]])
    learning_rate = 0.01
    learning_calc.update_weights(dw, learning_rate)

    # Define the network weights for forward propagation
    weights = [np.array([[0.1, 0.2], [0.3, 0.4]]), np.array([[0.5, 0.6]])]

    # Perform forward propagation
    activations = learning_calc.forward_propagation(weights)
    print("Activations:", activations)

    # Perform backpropagation to update the weights
    updated_weights = learning_calc.back_propagation(y_true, weights, learning_rate)
    print("Updated weights:", updated_weights)
