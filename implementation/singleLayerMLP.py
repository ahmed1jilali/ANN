import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stats import Stats

# === MLP Functions ===
class SingleLayerMLP:
    def __init__(self, x_train, y_train, n_features, n_neurons, n_output, iterations=1000, eta=0.001, grad_clip=1.0):
        self.x_train = x_train
        self.y_train = y_train
        self.iterations = iterations
        self.eta = eta
        self.n_features = n_features
        self.n_neurons = n_neurons
        self.n_output = n_output
        self.grad_clip = grad_clip
        
    def init_parameters(self, n_features, n_neurons, n_output):
        np.random.seed(100)
        W1 = np.random.randn(n_features, n_neurons) * np.sqrt(1. / n_features)
        b1 = np.zeros((1, n_neurons))
        W2 = np.random.randn(n_neurons, n_output) * np.sqrt(1. / n_neurons)
        b2 = np.zeros((1, n_output))
        return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

    def linear_function(self, W, X, b):
        return (X @ W) + b

    def sigmoid_function(self, Z):
        Z = np.clip(Z, -500, 500)
        return 1 / (1 + np.exp(-Z))

    def cost_function(self, A, y):
        return (np.mean(np.power(A - y, 2))) / 2

    def predict(self, X, W1, W2, b1, b2):
        Z1 = self.linear_function(W1, X, b1)
        S1 = self.sigmoid_function(Z1)
        Z2 = self.linear_function(W2, S1, b2)
        return Z2

    def fit(self, X, y,):
        param = self.init_parameters(self.n_features, self.n_neurons, self.n_output)
        errors = []
        for _ in range(self.iterations):
            # Forward
            Z1 = self.linear_function(param['W1'], X, param['b1'])
            S1 = self.sigmoid_function(Z1)
            Z2 = self.linear_function(param['W2'], S1, param['b2'])
            S2 = Z2
            # Cost
            error = self.cost_function(S2, y)
            errors.append(error)
            # Backpropagation
            delta2 = S2 - y
            W2_gradients = S1.T @ delta2
            b2_gradients = np.sum(delta2, axis=0, keepdims=True)
            delta1 = (delta2 @ param["W2"].T) * S1 * (1 - S1)
            W1_gradients = X.T @ delta1
            b1_gradients = np.sum(delta1, axis=0, keepdims=True)
            # Gradient Clipping
            W2_gradients = np.clip(W2_gradients, -self.grad_clip, self.grad_clip)
            b2_gradients = np.clip(b2_gradients, -self.grad_clip, self.grad_clip)
            W1_gradients = np.clip(W1_gradients, -self.grad_clip, self.grad_clip)
            b1_gradients = np.clip(b1_gradients, -self.grad_clip, self.grad_clip)
            # Update
            param["W2"] -= W2_gradients * self.eta
            param["b2"] -= b2_gradients * self.eta
            param["W1"] -= W1_gradients * self.eta
            param["b1"] -= b1_gradients * self.eta
        return param, errors



# === Load and Prepare Data ===
df = pd.read_csv("throughput.csv", header=None)
values = df.values.flatten()

# Normalize to [0, 1]
min_val, max_val = values.min(), values.max()
normalized = (values - min_val) / (max_val - min_val)

# 70/30 Split
split_point = int(0.7 * len(normalized))
train_series = normalized[:split_point]
test_series = normalized[split_point - 2:]  # include 2 back steps for sliding window

# Prepare training samples
X_train, y_train = [], []
for i in range(len(train_series) - 2):
    X_train.append([train_series[i], train_series[i + 1]])
    y_train.append([train_series[i + 2]])
X_train = np.array(X_train)
y_train = np.array(y_train)

# === Train MLP ===
mlp = SingleLayerMLP(X_train, y_train, n_features, n_neurons, n_output, y_train, )
param, errors = fit(X_train, y_train, iterations=1000, eta=0.001)

# Prepare test samples
X_test, y_test = [], []
for i in range(len(test_series) - 2):
    X_test.append([test_series[i], test_series[i + 1]])
    y_test.append([test_series[i + 2]])
X_test = np.array(X_test)
y_test = np.array(y_test)

# === Predict ===
y_pred = predict(X_test, param["W1"], param["W2"], param["b1"], param["b2"])

# Denormalize
y_pred_denorm = y_pred.flatten() * (max_val - min_val) + min_val
y_test_denorm = y_test.flatten() * (max_val - min_val) + min_val


stats = Stats(y_test_denorm, y_pred_denorm, errors, save=True, saveFolder="./results")
# stats.plotThroughput()
# stats.plotResiduals()
# stats.predictionVsActualScatterPlot()
# stats.lossCurveOverEpochs()
stats.plotResidualsHistogram()

# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R-squared (R²): {r2:.4f}")

# Mean Squared Error (MSE): 12298979.3378
# R-squared (R²): 0.8114