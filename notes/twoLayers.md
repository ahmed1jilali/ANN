Perfect. I’ll update the MLP to include a second hidden layer using sigmoid activation, while keeping the output layer linear for regression. I’ll also allow you to set the number of neurons in this second hidden layer via a new parameter (e.g., `n_neurons2`).

I'll provide the full, corrected Python code with the new `fit()` and `predict()` functions, and follow it with a detailed theoretical explanation: including all matrix shapes, forward propagation, backpropagation, activation functions, and how the loss is computed.

Give me a moment to prepare it all carefully for you.

# Multi-Layer Perceptron (Two Hidden Layers, Sigmoid + Linear Output)

## Python Implementation

```python
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
```

## Theoretical Explanation

### Forward Propagation

1. **Input to first hidden layer:** Given input matrix $X$ of shape $(n_x, m)$ (where $n_x$ is the number of features and $m$ is the number of examples), the first hidden layer pre-activation is
   
   $$
   Z^{[1]} = W^{[1]} X + b^{[1]},
   $$
   
   where $W^{[1]}$ has shape $(n\_{h1}, n_x)$ and $b^{[1]}$ has shape $(n\_{h1},1)$. The result $Z^{[1]}$ has shape $(n\_{h1}, m)$. Each column of $Z^{[1]}$ is the weighted sum of inputs plus bias for one example.

2. **First hidden activation:** Apply the sigmoid function $\sigma$ elementwise:
   
   $$
   A^{[1]} = \sigma(Z^{[1]}) = \frac{1}{1 + e^{-Z^{[1]}}},
   $$
   
   yielding $A^{[1]}$ of shape $(n\_{h1}, m)$.

3. **Second hidden layer linear transform:** The second hidden layer pre-activation is
   
   $$
   Z^{[2]} = W^{[2]} A^{[1]} + b^{[2]},
   $$
   
   where $W^{[2]}$ has shape $(n\_{h2}, n\_{h1})$ and $b^{[2]}$ has shape $(n\_{h2},1)$. Thus $Z^{[2]}$ has shape $(n\_{h2}, m)$.

4. **Second hidden activation:** Apply sigmoid:
   
   $$
   A^{[2]} = \sigma(Z^{[2]}) \quad\text{(shape $(n_{h2}, m)$).}
   $$

5. **Output layer linear transform:** The output layer (no hidden activation in the final layer) is
   
   $$
   Z^{[3]} = W^{[3]} A^{[2]} + b^{[3]},
   $$
   
   where $W^{[3]}$ has shape $(n_y, n\_{h2})$ and $b^{[3]}$ has shape $(n_y,1)$. The output $Z^{[3]}$ has shape $(n_y, m)$.

6. **Output activation (linear):** Because this is a regression task, we use a linear activation (identity function) at the output, so the predicted output is simply
   
   $$
   A^{[3]} = Z^{[3]} \quad\text{(shape $(n_y, m)$).}
   $$

In summary, the **forward propagation equations** are:

- $Z^{[1]} = W^{[1]} X + b^{[1]}$   (shape $(n\_{h1}, m)$)
- $A^{[1]} = \sigma(Z^{[1]})$   (shape $(n\_{h1}, m)$)
- $Z^{[2]} = W^{[2]} A^{[1]} + b^{[2]}$   (shape $(n\_{h2}, m)$)
- $A^{[2]} = \sigma(Z^{[2]})$   (shape $(n\_{h2}, m)$)
- $Z^{[3]} = W^{[3]} A^{[2]} + b^{[3]}$   (shape $(n_y, m)$)
- $A^{[3]} = Z^{[3]}$   (shape $(n_y, m)$)  (linear output)

### Activation Functions

- **Hidden layers:** We use the sigmoid activation function in both hidden layers. For any neuron pre-activation $z$,
  
  $$
  \sigma(z) = \frac{1}{1 + e^{-z}}.
  $$
  
  The derivative of the sigmoid (used in backpropagation) is
  
  $$
  \sigma'(z) = \sigma(z)\bigl(1 - \sigma(z)\bigr)\!,
  $$
  
  which can be computed from the activated output $a = \sigma(z)$ as $a(1-a)$.

- **Output layer:** We use a **linear (identity) activation** for the output. That is, the output is $A^{[3]} = Z^{[3]}$ directly, with no nonlinearity. Its derivative with respect to $Z^{[3]}$ is 1.

### Loss Function (Mean Squared Error)

For regression, we use the **Mean Squared Error (MSE)** as the loss. For $m$ examples, let $Y$ be the true values (shape $(n_y,m)$) and $\hat{Y}=A^{[3]}$ the predictions. The MSE is defined as

$$
J = \frac{1}{m} \sum_{i=1}^m \lVert \hat{y}^{(i)} - y^{(i)}\rVert^2 \,,
$$

or equivalently (with a factor $\frac{1}{2m}$)

$$
L = \frac{1}{2m}\sum_{i=1}^m ( \hat y^{(i)} - y^{(i)} )^2.
$$

Either form measures the average squared error. (Using the $\frac{1}{2m}$ version simplifies the gradient formulas by cancelling the 2 from the derivative.)

### Backpropagation and Gradients

We derive gradients of the loss with respect to all weights and biases using the chain rule. Working backwards from the output:

1. **Output layer gradients (linear output):**
   Since $A^{[3]} = Z^{[3]}$ (identity), the error term at the output is
   
   $$
   \delta^{[3]} \equiv \frac{\partial L}{\partial Z^{[3]}}
= \frac{\partial L}{\partial A^{[3]}} \cdot \frac{\partial A^{[3]}}{\partial Z^{[3]}}
= \frac{1}{m}\bigl(A^{[3]} - Y\bigr)\cdot 1
= \frac{1}{m}(A^{[3]} - Y).
   $$
   
   (Here we used $L=\frac{1}{2m}\sum(A^{[3]}-Y)^2$, so $\partial L/\partial A^{[3]}=(A^{[3]}-Y)/m$.)
   The gradients w\.r.t. $W^{[3]}$ and $b^{[3]}$ are then
   
   $$
   \frac{\partial L}{\partial W^{[3]}} = \delta^{[3]}\, {A^{[2]}}^T,
\qquad
\frac{\partial L}{\partial b^{[3]}} = \sum_{j=1}^m \delta^{[3]}_{\cdot,j},
   $$
   
   where $\delta^{[3]}$ has shape $(n_y,m)$ and $A^{[2]}$ has shape $(n\_{h2},m)$. Thus $\delta^{[3]} {A^{[2]}}^T$ yields a $(n_y\times n\_{h2})$ matrix, matching $W^{[3]}$’s shape, and summing $\delta^{[3]}$ across the $m$ examples (columns) gives a $(n_y\times 1)$ vector for $b^{[3]}$.

2. **Second hidden layer gradients:**
   Propagate the error back into the second hidden layer. First compute
   
   $$
   dA^{[2]} = W^{[3]T}\, \delta^{[3]} \quad\text{(shape $(n_{h2},m)$)}.
   $$
   
   Since $A^{[2]} = \sigma(Z^{[2]})$ with sigmoid activation, we get
   
   $$
   \delta^{[2]} \equiv \frac{\partial L}{\partial Z^{[2]}}
= dA^{[2]} \odot \sigma'(Z^{[2]})
= dA^{[2]} \odot \bigl(A^{[2]}(1-A^{[2]})\bigr),
   $$
   
   where “$\odot$” denotes elementwise multiplication. (We have used $\sigma'(z)=\sigma(z)(1-\sigma(z))$, and $A^{[2]}=\sigma(Z^{[2]})$.) The gradient w\.r.t. $W^{[2]}$ is
   
   $$
   \frac{\partial L}{\partial W^{[2]}} = \delta^{[2]}\,{A^{[1]}}^T,
   $$
   
   of shape $(n\_{h2}\times n\_{h1})$, and w\.r.t. $b^{[2]}$ is
   
   $$
   \frac{\partial L}{\partial b^{[2]}} = \sum_{j=1}^m \delta^{[2]}_{\cdot,j},
   $$
   
   of shape $(n\_{h2}\times 1)$.

3. **First hidden layer gradients:**
   Similarly, propagate into the first hidden layer. Compute
   
   $$
   dA^{[1]} = W^{[2]T}\, \delta^{[2]} \quad\text{(shape $(n_{h1},m)$)}.
   $$
   
   Using the sigmoid at layer 1,
   
   $$
   \delta^{[1]} \equiv \frac{\partial L}{\partial Z^{[1]}}
= dA^{[1]} \odot \bigl(A^{[1]}(1-A^{[1]})\bigr).
   $$
   
   Then
   
   $$
   \frac{\partial L}{\partial W^{[1]}} = \delta^{[1]}\,X^T,
\qquad
\frac{\partial L}{\partial b^{[1]}} = \sum_{j=1}^m \delta^{[1]}_{\cdot,j},
   $$
   
   producing shapes $(n\_{h1}\times n_x)$ and $(n\_{h1}\times 1)$ respectively.

Each gradient expression follows directly from the chain rule: we multiply the error term $\delta^{[\ell]}$ by the activation from the previous layer to get $\partial L/\partial W^{[\ell]}$, and sum $\delta^{[\ell]}$ across examples to get $\partial L/\partial b^{[\ell]}$.

### Error Propagation Through Layers

- **Chain rule:** The backpropagation uses the chain rule of calculus to express how a small change in any weight affects the final loss. The error at the output $\delta^{[3]}$ is propagated backwards: it first influences $W^{[3]}$ and $b^{[3]}$, then flows through $W^{[3]}$ back into the second hidden layer (as $dA^{[2]}$), is scaled by the sigmoid derivative to give $\delta^{[2]}$, and so on. In each hidden layer, the local derivative of the sigmoid activation ($A(1-A)$) modulates how much of the upstream error passes through. This way, the network “blames” each weight in proportion to how much it affected the output error.

- **Layer-by-layer flow:** Concretely,
  
  $$
  \delta^{[3]} = \frac{A^{[3]} - Y}{m},
\quad
\delta^{[2]} = (W^{[3]T}\delta^{[3]}) \odot A^{[2]}(1-A^{[2]}),
\quad
\delta^{[1]} = (W^{[2]T}\delta^{[2]}) \odot A^{[1]}(1-A^{[1]}).
  $$
  
  Each $\delta^{[\ell]}$ is of shape $(n\_{h\ell}\times m)$ (for hidden layers) or $(n_y\times m)$ for the output.

### Effect of Linear Output Layer

Because the output layer uses a **linear activation**, its derivative is $1$. This simplifies the gradient at the output:

$$
\delta^{[3]} = \frac{\partial L}{\partial Z^{[3]}} = \frac{1}{m}(A^{[3]} - Y),
$$

with no extra factor from an activation function (unlike if we had used, say, a sigmoid at the output). In other words, the gradient of the loss w\.r.t. the output pre-activation is just the average error $(\hat{y}-y)/m$. This linear output is standard in regression tasks and makes the final backpropagation step straightforward. If the output layer had a nonlinear activation (e.g. sigmoid), we would need an extra multiplication by that activation’s derivative.

In summary, the two-hidden-layer MLP with sigmoid hidden units and linear output proceeds as follows: _forward pass_ computes $Z^{[1]},A^{[1]}, Z^{[2]},A^{[2]}, Z^{[3]}$ and final output $A^{[3]}=Z^{[3]}$, then _backward pass_ propagates error $\delta^{[3]}$ back through $\delta^{[2]}$ and $\delta^{[1]}$, computing gradients
$\partial L/\partial W^{[\ell]}, \partial L/\partial b^{[\ell]}$ at each layer. These gradients are then used to update the weights (e.g. $W^{[\ell]} \leftarrow W^{[\ell]} - \alpha,\partial L/\partial W^{[\ell]}$). The derived Python code implements exactly these computations.

**Key equations recap:** Forward propagation

$$
\begin{aligned}
Z^{[1]} &= W^{[1]} X + b^{[1]}, & A^{[1]} &= \sigma(Z^{[1]}), \\
Z^{[2]} &= W^{[2]} A^{[1]} + b^{[2]}, & A^{[2]} &= \sigma(Z^{[2]}), \\
Z^{[3]} &= W^{[3]} A^{[2]} + b^{[3]}, & A^{[3]} &= Z^{[3]}.
\end{aligned}
$$

Loss: $L = \frac{1}{2m}\sum (A^{[3]}-Y)^2$.

Backward propagation gradients (by chain rule):

$$
\begin{aligned}
\delta^{[3]} &= \frac{1}{m}(A^{[3]} - Y), \\
\frac{\partial L}{\partial W^{[3]}} &= \delta^{[3]} {A^{[2]}}^T,\quad
\frac{\partial L}{\partial b^{[3]}} = \sum \delta^{[3]}, \\
dA^{[2]} &= W^{[3]T}\delta^{[3]},\quad
\delta^{[2]} = dA^{[2]}\odot A^{[2]}(1-A^{[2]}), \\
\frac{\partial L}{\partial W^{[2]}} &= \delta^{[2]} {A^{[1]}}^T,\quad
\frac{\partial L}{\partial b^{[2]}} = \sum \delta^{[2]}, \\
dA^{[1]} &= W^{[2]T}\delta^{[2]},\quad
\delta^{[1]} = dA^{[1]}\odot A^{[1]}(1-A^{[1]}), \\
\frac{\partial L}{\partial W^{[1]}} &= \delta^{[1]} X^T,\quad
\frac{\partial L}{\partial b^{[1]}} = \sum \delta^{[1]}.
\end{aligned}
$$

Here $\odot$ is elementwise multiplication, and $\sigma'(z)=\sigma(z)(1-\sigma(z))$. Error signals flow backward through the layers, enabling each weight to be updated to reduce the MSE loss.
