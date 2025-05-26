def fit(X, y, n_features=2, n_hidden1=5, n_hidden2=4, n_output=1, 
        iterations=1000, eta=0.001, grad_clip=1.0, 
        target_mse=None, target_r2=None, 
        X_val=None, y_val=None):
    
    param = init_parameters(n_features, n_hidden1, n_hidden2, n_output)
    errors = []

    for i in range(iterations):
        # === Forward pass ===
        Z1 = linear_function(param['W1'], X, param['b1'])
        A1 = sigmoid_function(Z1)

        Z2 = linear_function(param['W2'], A1, param['b2'])
        A2 = sigmoid_function(Z2)

        Z3 = linear_function(param['W3'], A2, param['b3'])
        A3 = Z3  # linear output

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

        # === Check for early stopping ===
        if (target_mse is not None or target_r2 is not None) and X_val is not None and y_val is not None:
            y_val_pred = predict(X_val, param["W1"], param["W2"], param["W3"], 
                                 param["b1"], param["b2"], param["b3"])
            mse = np.mean((y_val_pred - y_val) ** 2)
            if target_mse is not None and mse < target_mse:
                print(f"Early stopping at epoch {i+1}: MSE < {target_mse}")
                break
            if target_r2 is not None:
                ss_res = np.sum((y_val - y_val_pred) ** 2)
                ss_tot = np.sum((y_val - np.mean(y_val)) ** 2)
                r2 = 1 - (ss_res / ss_tot)
                if r2 > target_r2:
                    print(f"Early stopping at epoch {i+1}: R² > {target_r2}")
                    break

    return param, errors
