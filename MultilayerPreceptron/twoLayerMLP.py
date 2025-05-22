import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stats import Stats

# === MLP Functions ===

def init_parameters(n_features, n_hidden1, n_hidden2, n_output):
    np.random.seed(100)
    W1 = np.random.randn(n_features, n_hidden1) * np.sqrt(1. / n_features)
    b1 = np.zeros((1, n_hidden1))

    W2 = np.random.randn(n_hidden1, n_hidden2) * np.sqrt(1. / n_hidden1)
    b2 = np.zeros((1, n_hidden2))

    W3 = np.random.randn(n_hidden2, n_output) * np.sqrt(1. / n_hidden2)
    b3 = np.zeros((1, n_output))

    return {"W1": W1, "b1": b1,
            "W2": W2, "b2": b2,
            "W3": W3, "b3": b3}

def linear_function(W, X, b):
    return (X @ W) + b

def sigmoid_function(Z):
    Z = np.clip(Z, -500, 500)  # prevent overflow
    return 1 / (1 + np.exp(-Z))

def cost_function(A, y):
    return (np.mean(np.power(A - y, 2))) / 2

def predict(X, W1, W2, W3, b1, b2, b3):
    Z1 = linear_function(W1, X, b1)
    A1 = sigmoid_function(Z1)

    Z2 = linear_function(W2, A1, b2)
    A2 = sigmoid_function(Z2)

    Z3 = linear_function(W3, A2, b3)
    return Z3  # linear output


def fit(X, y, n_features=2, n_hidden1=5, n_hidden2=4, n_output=1, iterations=1000, eta=0.001, grad_clip=1.0):
    param = init_parameters(n_features, n_hidden1, n_hidden2, n_output)
    errors = []

    for _ in range(iterations):
        # === Forward pass ===
        Z1 = linear_function(param['W1'], X, param['b1'])
        A1 = sigmoid_function(Z1)

        Z2 = linear_function(param['W2'], A1, param['b2'])
        A2 = sigmoid_function(Z2)

        Z3 = linear_function(param['W3'], A2, param['b3'])
        A3 = Z3  # linear output for regression

        # === Cost ===
        error = cost_function(A3, y)
        errors.append(error)

        # === Backpropagation ===
        dZ3 = A3 - y
        dW3 = A2.T @ dZ3
        db3 = np.sum(dZ3, axis=0, keepdims=True)

        dA2 = dZ3 @ param['W3'].T
        dZ2 = dA2 * A2 * (1 - A2)
        dW2 = A1.T @ dZ2
        db2 = np.sum(dZ2, axis=0, keepdims=True)

        dA1 = dZ2 @ param['W2'].T
        dZ1 = dA1 * A1 * (1 - A1)
        dW1 = X.T @ dZ1
        db1 = np.sum(dZ1, axis=0, keepdims=True)

        # === Gradient Clipping ===
        for grad in [dW1, db1, dW2, db2, dW3, db3]:
            np.clip(grad, -grad_clip, grad_clip, out=grad)

        # === Update Parameters ===
        param["W1"] -= eta * dW1
        param["b1"] -= eta * db1
        param["W2"] -= eta * dW2
        param["b2"] -= eta * db2
        param["W3"] -= eta * dW3
        param["b3"] -= eta * db3

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
#param, errors = fit(X_train, y_train, iterations=1000, eta=0.001)
param, errors = fit(X_train, y_train, n_hidden1=8, n_hidden2=6, iterations=2000, eta=0.005)

# Prepare test samples
X_test, y_test = [], []
for i in range(len(test_series) - 2):
    X_test.append([test_series[i], test_series[i + 1]])
    y_test.append([test_series[i + 2]])
X_test = np.array(X_test)
y_test = np.array(y_test)

# === Predict ===
#y_pred = predict(X_test, param["W1"], param["W2"], param["b1"], param["b2"])
y_pred = predict(X_test, param["W1"], param["W2"], param["W3"], param["b1"], param["b2"], param["b3"])

# Denormalize
y_pred_denorm = y_pred.flatten() * (max_val - min_val) + min_val
y_test_denorm = y_test.flatten() * (max_val - min_val) + min_val


stats = Stats(y_test_denorm, y_pred_denorm, errors)
# stats.plotThroughput()
# stats.plotResiduals()
# stats.predictionVsActualScatterPlot()
# stats.lossCurveOverEpochs()
# stats.plotResidualsHistogram()
# print(stats.mse())
# print(stats.r2())

print(f"Mean Squared Error (MSE): {stats.mse():.4f}")
print(f"R-squared (R²): {stats.r2():.4f}")

# Mean Squared Error (MSE): 12298979.3378
# R-squared (R²): 0.8114