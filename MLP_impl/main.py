import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from tqdm import tqdm
# Neural network functions
def initialisation(n0, n1, n2):
    np.random.seed(0)
    return {
        'W1': np.random.randn(n1, n0),
        'b1': np.zeros((n1, 1)),
        'W2': np.random.randn(n2, n1),
        'b2': np.zeros((n2, 1))
    }

def forward_propagation(X, params):
    Z1 = params['W1'].dot(X) + params['b1'] #(n1,1)
    A1 = 1 / (1 + np.exp(-Z1))#(n1,1)
    Z2 = params['W2'].dot(A1) + params['b2']#(n2,1)
    return {'A1': A1, 'A2': Z2}  # Linear output for regression

def back_propagation(X, y, params, activations):
    A1, A2 = activations['A1'], activations['A2']
    m = y.shape[1]
    dZ2 = A2 - y #(1,1)
    dW2 = (1 / m) * dZ2.dot(A1.T) #(1,n1)
    db2 = (1 / m) * np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = params['W2'].T.dot(dZ2) * A1 * (1 - A1)#
    dW1 = (1 / m) * dZ1.dot(X.T)
    db1 = (1 / m) * np.sum(dZ1, axis=1, keepdims=True)
    return {'dW1': dW1, 'db1': db1, 'dW2': dW2, 'db2': db2}

def update(params, grads, lr):
    for key in params:
        params[key] -= lr * grads['d' + key]
    return params

def predict(X, params):
    return forward_propagation(X, params)['A2']

def train_nn(X, y, hidden_neurons=10, lr=0.1, iterations=1000):
    n0, n2 = X.shape[0], y.shape[0]
    params = initialisation(n0, hidden_neurons, n2)
    loss_history = []

    for _ in tqdm(range(iterations)):
        activations = forward_propagation(X, params)
        loss = np.mean((activations['A2'] - y) ** 2)
        loss_history.append(loss)
        grads = back_propagation(X, y, params, activations)
        params = update(params, grads, lr)

    return params, loss_history
# Load CSV data (replace filename)
data = pd.read_csv("Throughput_Mbps.csv")  #  filename

# Split input/output
X = data.iloc[:, :2].values  # First 2 columns as input
y = data.iloc[:, 2].values   # Last column as output

# Normalize data
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()
X = scaler_X.fit_transform(X)
y = scaler_y.fit_transform(y.reshape(-1, 1)).flatten()

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Transpose for our neural network shape: (features, samples)
X_train, X_test = X_train.T, X_test.T
y_train, y_test = y_train.reshape(1, -1), y_test.reshape(1, -1)

# Train
params, loss_history = train_nn(X_train, y_train, hidden_neurons=5, lr=0.01, iterations=5000)

# Predict
y_pred_train = predict(X_train, params)
y_pred_test = predict(X_test, params)

# Inverse scale
y_train_true = scaler_y.inverse_transform(y_train.T).flatten()
y_test_true = scaler_y.inverse_transform(y_test.T).flatten()
y_train_pred = scaler_y.inverse_transform(y_pred_train.T).flatten()
y_test_pred = scaler_y.inverse_transform(y_pred_test.T).flatten()
residuals_test = y_test_true - y_test_pred
# Metrics
# mse_test = mean_squared_error(y_test_true, y_test_pred)
r2_test = r2_score(y_test_true, y_test_pred)

# === PLOTS ===
plt.figure(figsize=(14, 10))

# 1. Training Loss
plt.subplot(2, 2, 1)
plt.plot(loss_history)
plt.title("Training Loss (MSE)")
plt.xlabel("Iterations")
plt.ylabel("MSE")
plt.grid(True)

# 2. Predicted vs Actual (Test)
plt.subplot(2, 2, 2)
plt.plot(y_test_true, label='Actual')
plt.plot(y_test_pred, label='Predicted', alpha=0.7)
plt.title("Test Set: Predicted vs Actual")
plt.legend()
plt.grid(True)

# 3. Residuals (Test)
plt.subplot(2, 2, 3)
plt.plot(residuals_test, label='Residuals')
plt.axhline(0, color='red', linestyle='--')
plt.title("Test Residuals")
plt.grid(True)

# 4. Scatter Plot (Test)
plt.subplot(2, 2, 4)
plt.scatter(y_test_true, y_test_pred, alpha=0.6)
plt.plot([min(y_test_true), max(y_test_true)], [min(y_test_true), max(y_test_true)], color='red')
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Scatter Plot: Actual vs Predicted (Test)")
plt.grid(True)

plt.tight_layout()
plt.show()

# === METRICS ===
print(f"Test R² Score: {r2_test:.4f}")
# print(f"Test MSE: {mse_test:.4f}")

