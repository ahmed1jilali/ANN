# Traffic forecasting in ...

## 1. Problem Definition

### 1.1 Nature of the Problem

With 4G mobile devices becoming more affordable and widely available, and the population using it getting larger, better ways to manage the 4G mobile network needs to emerge. Accurate traffic prediction is essential for effective network planning, resource allocation, and congestion management.

This thesis addresses a **regression problem**, where the goal is to predict a continuous value, more specifically the expected network throughput in the next hour based on historical data, where the forecasting model seeks to learn from previous traffic patterns and generalize this knowledge to predict future usage levels. We saw a Multilayer perceptron best fit for that role.

Forecasting the network traffic allows the anticipation of high demand periods, and optimizing the network performance accordingly, and thus preventing the congestion of the cellular network. We used a Multilayer perceptron for this task because it is a type of neural network that can learn patterns in data and make predictions based on them, even when the relationships between the input and output are nonlinear, which makes it well-suited for modeling the complex behavior of network throughput over time.

### 1.2 Input and Output Variables

The Multilayer Perceptron *(**MLP**)* model developed in this work uses the **throughput values of the current hour and the previous hour** as features. These values represent the history of the network usage, and are assumed to be highly indicative of short-term future behavior.

- **Input Features:**
  
  - Network throughput at time t-1
  
  - Network throughput at time t

- **Output Target:**
  
  - Forecasted throughput at time t+1

The model is trained to recognize sequential dependencies in traffic temporal patterns, where each input includes traffic from two consecutive hours, the model can learn how traffic evolves over time.

---

## 2. Data Preprocessing

Preprocessing is a crucial step after gathering data, which makes the modeling more effective. This step depends on what task is to be performed and the characteristics of the data being handled.

### 2.1 Selection of Inputs

To maintain a balance between  model simplicity and performance, only two features were selected as inputs: the throughput at the current hour $(t)$ and the previous hour $(t-1)$. These features were chosen based on the assumption that short-term past values are highly predictive of near-future traffic.

### 2.2 Normalization

A key step in preprocessing is normalizing the data, so that all values lie in the range [0,1], this is very helpful for neural networks, which tend to train more efficiently on uniformly scaled input data.

It also helps avoid exploding or vanishing gradients and improves convergence speed.

The normalization is shown in **Equation N03** where:

- x_{i}^{normalized}​ is the normalized value.

- x_{i} is the current value to normalize.

- x_{max} is the maximum value in the data.

- x_{min} is the minimum value in the data.

$$
x_{i}^{normalized}​ = \frac{​x_{i}​−x_{min}}{x_{max}​−x_{min}}​​
$$

**Equation**: Normalization formula.

### 2.3 Splitting

---
