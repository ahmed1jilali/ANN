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

def initialisationXavierGuassian(n0, n1, n2):
    np.random.seed(0)
    return {
        'W1': np.random.normal(0, (2 / (n0 + n1)), (n1, n0)),
        'b1': np.zeros((n1, 1)),
        'W2': np.random.normal(0, (2 / (n1 + n2)), (n2, n1)),
        'b2': np.zeros((n2, 1))
    }

def initialisationXavierUniform(n0, n1, n2):
    np.random.seed(0)
    limit1 = np.sqrt(6 / (n0 + n1))
    limit2 = np.sqrt(6 / (n1 + n2))
    return {
        'W1': np.random.uniform(-limit1, limit1, (n1, n0)),
        'b1': np.zeros((n1, 1)),
        'W2': np.random.uniform(-limit2, limit2, (n2, n1)),
        'b2': np.zeros((n2, 1))
    }

def initialisationHeGuassian(n0, n1, n2):
    np.random.seed(0)
    return {
        'W1': np.random.normal(0, (4 / (n0 + n1)), (n1, n0)),
        'b1': np.zeros((n1, 1)),
        'W2': np.random.normal(0, (4 / (n1 + n2)), (n2, n1)),
        'b2': np.zeros((n2, 1))
    }

def initialisationHeUniform(n0, n1, n2):
    np.random.seed(0)
    limit1 = np.sqrt(12 / (n0 + n1))
    limit2 = np.sqrt(12 / (n1 + n2))
    return {
        'W1': np.random.uniform(-limit1, limit1, (n1, n0)),
        'b1': np.zeros((n1, 1)),
        'W2': np.random.uniform(-limit2, limit2, (n2, n1)),
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
    # E = (1/n)*(1/2)*(a-y)
    dZ2 = (A2 - y)/m #(1,1)
    dW2 = dZ2.dot(A1.T) #(1,n1)
    db2 = np.sum(dZ2, axis=1, keepdims=True)
    dZ1 = params['W2'].T.dot(dZ2) * A1 * (1 - A1)#
    dW1 = dZ1.dot(X.T)
    db1 = np.sum(dZ1, axis=1, keepdims=True)
    return {'dW1': dW1, 'db1': db1, 'dW2': dW2, 'db2': db2}

def update(params, grads, lr):
    for key in params:
        params[key] -= lr * grads['d' + key]
    return params

def predict(X, params):
    return forward_propagation(X, params)['A2']

def train_nn(X, y, hidden_neurons=10, lr=0.1, iterations=1000, init=""):
    n0, n2 = X.shape[0], y.shape[0]
    if init == "XU":
        params = initialisationXavierUniform(n0, hidden_neurons, n2)
    elif init == "XG":
        params = initialisationXavierGuassian(n0, hidden_neurons, n2)
    elif init == "HU":
        params = initialisationHeUniform(n0, hidden_neurons, n2)
    elif init == "HG":
        params = initialisationHeGuassian(n0, hidden_neurons, n2)
    else:
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
data = pd.read_csv("Throughput_Mbps_5000.csv")  #  filename

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
params, loss_history = train_nn(X_train, y_train, hidden_neurons=3, lr=1, iterations=7000, init="XG")

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

print(f"Test R² Score: {r2_test:.4f}")

# === PLOTS ===
#plt.figure(figsize=(14, 10))

# 1. Training Loss
#plt.subplot(2, 2, 1)
plt.figure()
plt.plot(loss_history)
plt.title("Training Loss (MSE)")
plt.xlabel("Iterations")
plt.ylabel("MSE")
plt.grid(True)

# 2. Predicted vs Actual (Test)
#plt.subplot(2, 2, 2)
plt.figure()
plt.plot(y_test_true, label='Actual')
plt.plot(y_test_pred, label='Predicted', alpha=0.7)
plt.title("Test Set: Predicted vs Actual")
plt.legend()
plt.grid(True)

# 3. Residuals (Test)
#plt.subplot(2, 2, 3)
plt.figure()
plt.plot(residuals_test, label='Residuals')
plt.axhline(0, color='red', linestyle='--')
plt.title("Test Residuals")
plt.grid(True)

# 4. Scatter Plot (Test)
#plt.subplot(2, 2, 4)
plt.figure()
plt.scatter(y_test_true, y_test_pred, alpha=0.6)
plt.plot([min(y_test_true), max(y_test_true)], [min(y_test_true), max(y_test_true)], color='red')
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Scatter Plot: Actual vs Predicted (Test)")
plt.grid(True)

# Adjust the number of bins depending on your dataset size for better granularity.
plt.figure(figsize=(8, 5))
plt.hist(residuals_test, bins=30, color='purple', edgecolor='black', alpha=1)
# A vertical line at zero to show bias (left = underprediction, right = overprediction).
plt.axvline(0, color='black', linestyle='--')
plt.title("Residual Errors Histogram")
plt.xlabel("Residual (y_actual - y_predicted)")
plt.ylabel("Frequency")
plt.grid(True)
plt.tight_layout()


#plt.tight_layout()
plt.show()
print("residuals_test")
print(residuals_test)
print()
print("-"*10)
print("loss_history")
print(loss_history)
print()
print("-"*10)
print("y_test_true")
print(y_test_true)
print()
print("-"*10)
print("y_test_pred")
print(y_test_pred)
# === METRICS ===
# print(f"Test MSE: {mse_test:.4f}")


# plt.scatter(y_pred_test, residuals_test, alpha=0.5) # alpha helps visualize dense areas
plt.scatter(y_test_pred, residuals_test, alpha=0.5) # alpha helps visualize dense areas
plt.axhline(0, color='red', linestyle='--')
plt.title("Residuals vs. Predicted Values (Scatter Plot)")
plt.xlabel("Predicted Values")
plt.ylabel("Residuals")
plt.grid(True)
plt.show()
