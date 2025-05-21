import numpy as np

def sigmoid(Z):
    """Sigmoid activation function."""
    return 1 / (1 + np.exp(-Z))

def init_parameters(n_x, n_h1, n_h2, n_y):
    """
    Initialize weights and biases for a 2-hidden-layer neural network.
    n_x: number of input features
    n_h1: number of neurons in the first hidden layer
    n_h2: number of neurons in the second hidden layer
    n_y: number of outputs
    """
    np.random.seed(1)  # for reproducibility
    W1 = np.random.randn(n_h1, n_x) * 0.01
    b1 = np.zeros((n_h1, 1))
    W2 = np.random.randn(n_h2, n_h1) * 0.01
    b2 = np.zeros((n_h2, 1))
    W3 = np.random.randn(n_y, n_h2) * 0.01
    b3 = np.zeros((n_y, 1))
    return {"W1": W1, "b1": b1,
            "W2": W2, "b2": b2,
            "W3": W3, "b3": b3}

def fit(X, Y, n_h1, n_h2, learning_rate=0.01, num_iterations=1000, verbose=False):
    """
    Train a 2-hidden-layer MLP with sigmoid activations (hidden) and linear output (regression).
    X: input data, shape (m, n_x) or (n_x, m)
    Y: target values, shape (m, n_y) or (n_y, m)
    n_h1: number of neurons in first hidden layer
    n_h2: number of neurons in second hidden layer
    learning_rate: learning rate for gradient descent
    num_iterations: number of training iterations (epochs)
    """
    # Ensure X, Y have shape (n_x, m) and (n_y, m)
    X = X.T if X.shape[0] > X.shape[1] else X
    Y = Y.T if Y.shape[0] > Y.shape[1] else Y
    n_x, m = X.shape
    n_y, _ = Y.shape

    # Initialize parameters (weights and biases)
    params = init_parameters(n_x, n_h1, n_h2, n_y)
    W1, b1 = params["W1"], params["b1"]
    W2, b2 = params["W2"], params["b2"]
    W3, b3 = params["W3"], params["b3"]

    # Gradient descent loop
    for i in range(num_iterations):
        # --- Forward propagation ---
        Z1 = np.dot(W1, X) + b1           # First hidden layer linear transform (n_h1 x m)
        A1 = sigmoid(Z1)                 # First hidden activation (n_h1 x m)
        Z2 = np.dot(W2, A1) + b2         # Second hidden layer linear transform (n_h2 x m)
        A2 = sigmoid(Z2)                 # Second hidden activation (n_h2 x m)
        Z3 = np.dot(W3, A2) + b3         # Output layer linear transform (n_y x m)
        A3 = Z3                          # Linear output (identity activation, n_y x m)

        # Compute cost (Mean Squared Error)
        cost = (1 / (2 * m)) * np.sum((A3 - Y)**2)

        # --- Backward propagation ---
        # Output layer gradients (linear output)
        dZ3 = (A3 - Y) / m               # (n_y x m)
        dW3 = np.dot(dZ3, A2.T)          # (n_y x n_h2)
        db3 = np.sum(dZ3, axis=1, keepdims=True)  # (n_y x 1)

        # Backprop into second hidden layer
        dA2 = np.dot(W3.T, dZ3)          # (n_h2 x m)
        dZ2 = dA2 * A2 * (1 - A2)        # Sigmoid derivative (n_h2 x m)
        dW2 = np.dot(dZ2, A1.T)          # (n_h2 x n_h1)
        db2 = np.sum(dZ2, axis=1, keepdims=True)  # (n_h2 x 1)

        # Backprop into first hidden layer
        dA1 = np.dot(W2.T, dZ2)          # (n_h1 x m)
        dZ1 = dA1 * A1 * (1 - A1)        # Sigmoid derivative (n_h1 x m)
        dW1 = np.dot(dZ1, X.T)           # (n_h1 x n_x)
        db1 = np.sum(dZ1, axis=1, keepdims=True)  # (n_h1 x 1)

        # --- Update parameters ---
        W3 -= learning_rate * dW3
        b3 -= learning_rate * db3
        W2 -= learning_rate * dW2
        b2 -= learning_rate * db2
        W1 -= learning_rate * dW1
        b1 -= learning_rate * db1

        if verbose and i % 100 == 0:
            print(f"Iteration {i}: cost = {cost:.6f}")

    # Store updated parameters
    params["W1"], params["b1"] = W1, b1
    params["W2"], params["b2"] = W2, b2
    params["W3"], params["b3"] = W3, b3
    return params

def predict(X, params):
    """
    Compute predictions using the trained network parameters.
    X: input data, shape (m, n_x) or (n_x, m)
    params: dictionary of learned weights and biases
    Returns predictions of shape (m, n_y).
    """
    X = X.T if X.shape[0] > X.shape[1] else X
    W1, b1 = params["W1"], params["b1"]
    W2, b2 = params["W2"], params["b2"]
    W3, b3 = params["W3"], params["b3"]

    Z1 = np.dot(W1, X) + b1
    A1 = sigmoid(Z1)
    Z2 = np.dot(W2, A1) + b2
    A2 = sigmoid(Z2)
    Z3 = np.dot(W3, A2) + b3
    A3 = Z3  # linear output

    return A3.T
