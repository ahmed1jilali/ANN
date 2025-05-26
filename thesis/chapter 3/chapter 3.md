# Throughput forecasting for LTE network



Implementation Steps for an MLP

1. Identify relevant inputs (variables that significantly impact the target phenomenon).

2. Normalize data.

3. Determine the optimal number of hidden neurons.

4. Train the network (minimize the cost function).

5. Evaluate performance post-training.

6. Apply the trained model.

7. De-normalize the output data.

This process may require several iterations for optimal results.

## Data preprocessing:

Preprocessing is a crucial step after gathering data, which makes the modeling more effective. This step depends on what task is to be performed and the characteristics of the data being handled.

Preprocessing involves normalizing the data, so that all values lie in the range [0,1], this is very helpful for neural networks, which tend to train more efficiently on uniformly scaled input data.

It also helps avoid exploding or vanishing gradients and improves convergence speed.

The normalization is shown in **Equation N03** where:

- x_{i}^{normalized}​ is the normalized value.

- x_{i} is the original value.

- x_{max} is the maximum value in the data.

- x_{min} is the minimum value in the data.

$$
x_{i}^{normalized}​ = \frac{x_{max}​−x_{min}}{​x_{i}​−x_{min}}​​
$$

**Equation N04**: Normalization formula.

Another step is to split the data into a training set and a testing set, for example 70\% goes for training the model, and the remaining 30\% of the data goes for testing.

---

# Learning in Multi-Layer Perceptron

Training involves:

1. Forward propagation of input data.

2. Comparing computed output with the desired output.

3. Backpropagating the error to update weights.

This is repeated until the output error becomes negligible.
