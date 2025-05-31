Great! Here's a draft for **Section 1 – Problem Definition** of your thesis titled *"Traffic forecasting in 4G mobile networks using machine learning techniques"*:

---

## 1. Problem Definition

### 1.1 Nature of the Problem

The growing demand for mobile data services has significantly increased the importance of traffic forecasting in 4G mobile networks. Accurate traffic prediction is essential for effective network planning, resource allocation, and congestion management. This thesis addresses a **regression problem**, where the goal is to predict a continuous value—specifically, the expected network throughput (or traffic volume) in the next hour based on historical data.

Forecasting network traffic allows operators to anticipate periods of high demand and optimize network performance accordingly. Unlike classification tasks that aim to assign categories to input data, regression involves modeling the relationship between numerical inputs and a continuous output variable. In this case, the forecasting model seeks to learn from historical traffic patterns and generalize this knowledge to predict future usage levels.

### 1.2 Input and Output Variables

To simplify the modeling process and focus on temporal patterns, the Multilayer Perceptron (MLP) model developed in this work uses the **traffic values of the current hour and the previous hour** as input features. These values represent the recent history of network usage and are assumed to be highly indicative of short-term future behavior.

- **Input Variables (Features):**
  
  - Traffic at time *t-1*
  
  - Traffic at time *t*

- **Output Variable (Target):**
  
  - Forecasted traffic at time *t+1*

By using a sliding time window approach, the model is trained to recognize sequential dependencies in traffic patterns. The simplicity of this feature set supports fast training and real-time prediction capabilities, which are critical in mobile network environments.

---

The Multilayer Perceptron *(**MLP**)* model developed in this work uses the **throughput values of the current hour and the previous hour** as features. These values represent the history of the network usage, and are assumed to be highly indicative of short-term future behavior.

- **Input Features:**
  
  - Network throughput at time $t-1$
  
  - Network throughput at time $t$

- **Output Target:**
  
  - Forecasted throughput at time $t+1$

The model is trained to recognize sequential dependencies in traffic temporal patterns, where each input includes traffic from two consecutive hours, the model can learn how traffic evolves over time.

---
