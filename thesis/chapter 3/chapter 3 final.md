# Traffic forecasting in ...

## 1. Problem Definition

### 1.1 Nature of the Problem

With 4G mobile devices becoming more affordable and widely available, and the population using it getting larger, better ways to manage the 4G mobile network needs to emerge. Accurate traffic prediction is essential for effective network planning, resource allocation, and congestion management.

This thesis addresses a **regression problem**, where the goal is to predict a continuous value, more specifically the expected network throughput in the next hour based on historical data, where the forecasting model seeks to learn from previous traffic patterns and generalize this knowledge to predict future usage levels. We saw a Multilayer perceptron best fit for that role.

Forecasting the network traffic allows the anticipation of high demand periods, and optimizing the network performance accordingly, and thus preventing the congestion of the cellular network. We used a Multilayer perceptron for this task because it is a type of neural network that can learn patterns in data and make predictions based on them, even when the relationships between the input and output are nonlinear, which makes it well-suited for modeling the complex behavior of network throughput over time.

---



### 1.2 Input and Output Variables

The Multilayer Perceptron *(**MLP**)* model developed in this work uses the **throughput values of the current hour and the previous hour** as features. These values represent the history of the network usage, and are assumed to be highly indicative of short-term future behavior.

- **Input Features:**
  
  - Network throughput at time t-1
  
  - Network throughput at time t

- **Output Target:**
  
  - Forecasted throughput at time t+1

The model is trained to recognize sequential dependencies in traffic temporal patterns, where each input includes traffic from two consecutive hours, the model can learn how traffic evolves over time.
