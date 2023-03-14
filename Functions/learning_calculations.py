import numpy as np

class LearningCalculation:
    def __init__(self, x: float, w: float, b: float):
        self.x = x
        self.w = w
        self.b = b


    def linear_model(self):
        # z = w⋅x + b
        z = np.dot(self.w.T, self.x) + self.b
        return z
    

    def linear_function(self):
        # f(x) = y = 2x - 2
        y = 2 * self.x - 2
        return y


    def mean_squared_error(self, y_true):
        y_pred = self.linear_function()
        mse = np.mean((y_true - y_pred)**2)
        return mse


    def update_weights(self, dw, learning_rate):
        # w := w - A dj(w)/dw
        self.w -= learning_rate * dw


    def forward_propagation(self, weights):
        z = self.x
        activations = [z]
        for i in range(len(weights)):
            z = np.dot(z, weights[i])
            a = self.sigmoid(z)
            activations.append(a)
        return activations


    def weight_updates(self, weights, learning_rate, activations, deltas):
        for i in range(len(weights)):
            weights[i] -= learning_rate * np.dot(activations[i].T, deltas[i])
        return weights


    def back_propagation(self, y_true, weights, learning_rate):
        activations = self.forward_propagation(weights)
        deltas = [activations[-1] - y_true]
        for i in range(len(weights)-1, 0, -1):
            delta = np.dot(deltas[-1], weights[i].T) * self.sigmoid_derivative(activations[i])
            deltas.append(delta)
        deltas.reverse()
        weights = self.weight_updates(weights, learning_rate, activations, deltas)
        return weights


    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))


    def sigmoid_derivative(self, a):
        return a * (1 - a)