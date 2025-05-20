import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# === MLP Functions ===

def init_parameters(n_features, n_neurons, n_output):
    np.random.seed(100)
    W1 = np.random.randn(n_features, n_neurons) * np.sqrt(1. / n_features)
    b1 = np.zeros((1, n_neurons))
    W2 = np.random.randn(n_neurons, n_output) * np.sqrt(1. / n_neurons)
    b2 = np.zeros((1, n_output))
    return {"W1": W1, "b1": b1, "W2": W2, "b2": b2}

def linear_function(W, X, b):
    return (X @ W) + b

def sigmoid_function(Z):
    Z = np.clip(Z, -500, 500)  # prevent overflow
    return 1 / (1 + np.exp(-Z))

def cost_function(A, y):
    return (np.mean(np.power(A - y, 2))) / 2

def predict(X, W1, W2, b1, b2):
    Z1 = linear_function(W1, X, b1)
    S1 = sigmoid_function(Z1)
    Z2 = linear_function(W2, S1, b2)
    return Z2  # regression output

def fit(X, y, n_features=2, n_neurons=3, n_output=1, iterations=1000, eta=0.001, grad_clip=1.0):
    param = init_parameters(n_features, n_neurons, n_output)
    errors = []

    for _ in range(iterations):
        # Forward
        Z1 = linear_function(param['W1'], X, param['b1'])
        S1 = sigmoid_function(Z1)
        Z2 = linear_function(param['W2'], S1, param['b2'])
        S2 = Z2

        # Cost
        error = cost_function(S2, y)
        errors.append(error)

        # Backpropagation
        delta2 = S2 - y
        W2_gradients = S1.T @ delta2
        b2_gradients = np.sum(delta2, axis=0, keepdims=True)

        delta1 = (delta2 @ param["W2"].T) * S1 * (1 - S1)
        W1_gradients = X.T @ delta1
        b1_gradients = np.sum(delta1, axis=0, keepdims=True)

        # Gradient Clipping
        W2_gradients = np.clip(W2_gradients, -grad_clip, grad_clip)
        b2_gradients = np.clip(b2_gradients, -grad_clip, grad_clip)
        W1_gradients = np.clip(W1_gradients, -grad_clip, grad_clip)
        b1_gradients = np.clip(b1_gradients, -grad_clip, grad_clip)

        # Update
        param["W2"] -= W2_gradients * eta
        param["b2"] -= b2_gradients * eta
        param["W1"] -= W1_gradients * eta
        param["b1"] -= b1_gradients * eta

    return param

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
param = fit(X_train, y_train, iterations=1000, eta=0.001)

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

# === Plot ===
plt.figure(figsize=(12, 6))
plt.plot(y_test_denorm, label="Actual Throughput", color='dodgerblue')
plt.plot(y_pred_denorm, label="Predicted Throughput", color='coral', linestyle='--')
plt.title("Network Throughput Prediction (Test Set)", color='white')
plt.xlabel("Hour Index", color='white')
plt.ylabel("Throughput (Kb/s)", color='white')
plt.tick_params(colors='white')

ax = plt.gca()
for spine in ax.spines.values():
    spine.set_color('white')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('output.png', format='png', dpi=600, transparent=True)
plt.show()
