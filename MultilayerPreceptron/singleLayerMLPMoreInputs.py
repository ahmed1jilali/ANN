import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from stats import Stats

# === Configurable Window Size ===
window_size = 6  # number of past steps to use as input

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
    Z = np.clip(Z, -500, 500)
    return 1 / (1 + np.exp(-Z))

def cost_function(A, y):
    return (np.mean(np.power(A - y, 2))) / 2

def predict(X, W1, W2, W3, b1, b2, b3):
    A1 = sigmoid_function(linear_function(W1, X, b1))
    A2 = sigmoid_function(linear_function(W2, A1, b2))
    Z3 = linear_function(W3, A2, b3)
    return Z3  # linear output

def fit(X, y, n_features, n_hidden1=8, n_hidden2=6, n_output=1,
        iterations=2000, eta=0.005, grad_clip=1.0):
    param = init_parameters(n_features, n_hidden1, n_hidden2, n_output)
    errors = []

    for _ in range(iterations):
        # Forward
        A1 = sigmoid_function(linear_function(param['W1'], X, param['b1']))
        A2 = sigmoid_function(linear_function(param['W2'], A1, param['b2']))
        A3 = linear_function(param['W3'], A2, param['b3'])

        # Cost
        errors.append(cost_function(A3, y))

        # Backprop
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

        # Clip
        for grad in [dW1, db1, dW2, db2, dW3, db3]:
            np.clip(grad, -grad_clip, grad_clip, out=grad)

        # Update
        for key, grad in zip(['W1','b1','W2','b2','W3','b3'],
                             [dW1, db1, dW2, db2, dW3, db3]):
            param[key] -= eta * grad

    return param, errors

# === Load and Normalize ===
df = pd.read_csv("throughput.csv", header=None)
values = df.values.flatten()
min_val, max_val = values.min(), values.max()
normalized = (values - min_val) / (max_val - min_val)

# === Split ===
split_point = int(0.7 * len(normalized))
train_series = normalized[:split_point]
test_series = normalized[split_point - window_size:]

# === Prepare Samples ===
X_train, y_train = [], []
for i in range(len(train_series) - window_size):
    X_train.append(train_series[i:i + window_size])
    y_train.append([train_series[i + window_size]])
X_train = np.array(X_train)
y_train = np.array(y_train)

# === Train ===
param, errors = fit(X_train, y_train, n_features=window_size)

# === Test Samples ===
X_test, y_test = [], []
for i in range(len(test_series) - window_size):
    X_test.append(test_series[i:i + window_size])
    y_test.append([test_series[i + window_size]])
X_test = np.array(X_test)
y_test = np.array(y_test)

# === Predict and Denormalize ===
y_pred = predict(X_test, param["W1"], param["W2"], param["W3"], param["b1"], param["b2"], param["b3"])
y_pred_denorm = y_pred.flatten() * (max_val - min_val) + min_val
y_test_denorm = y_test.flatten() * (max_val - min_val) + min_val

# === Metrics ===
stats = Stats(y_test_denorm, y_pred_denorm, errors)
print(f"MSE: {stats.mse():.4f}")
print(f"R²: {stats.r2():.4f}")
