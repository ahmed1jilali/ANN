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

## 2. Data Preprocessing

Data preprocessing is a crucial step in the machine learning pipeline, particularly in time series forecasting tasks such as traffic prediction. Properly preparing the dataset ensures the model can learn effectively and generalize well to unseen data. The preprocessing steps followed in this thesis are outlined below.

### 2.1 Selection of Inputs

To maintain a balance between model simplicity and performance, only two features were selected as inputs: the traffic at the current hour (*t*) and the previous hour (*t-1*). These features were chosen based on the assumption that short-term past values are highly predictive of near-future traffic, which is common in mobile network traffic patterns.

This selection process reduces noise from irrelevant variables and minimizes the complexity of the model, allowing the Multilayer Perceptron to focus on learning temporal trends without overfitting to extraneous data.

### 2.2 Normalization

The raw traffic data exhibited variations in scale and magnitude that could negatively impact the learning process. To address this, **Min-Max normalization** was applied to scale all values into the [0, 1] range:

where:

- is the original traffic value,

- and are the minimum and maximum values in the dataset, respectively,

- is the normalized value.

This transformation ensures that all features contribute equally to the learning process and helps accelerate the convergence of the optimization algorithm.

### 2.3 Splitting

The dataset consisted of **2000 hourly traffic records**, representing approximately 83 days of continuous traffic monitoring. This dataset was split into three subsets:

- **Training Set (70%)** – Used to train the model and update weights.

- **Testing Set (30%)** - Used to evaluate the final model’s performance on unseen data.

The splitting was performed chronologically to preserve the temporal order of the data, avoiding any data leakage from the future into the past. This is particularly important in time series forecasting, where the sequence of observations is a key factor.

---

Great! Here's the draft for **Section 3 – Network Architecture Design** of your thesis:

---

## 3. Network Architecture Design

The performance of a neural network depends heavily on its architecture. This section outlines the design decisions made for the Multilayer Perceptron (MLP) model used to forecast traffic in 4G mobile networks.

### 3.1 Input Layer

The input layer is configured with **2 neurons**, corresponding to the two selected input features:

- Traffic at time *t-1*

- Traffic at time *t*

These neurons serve as the entry point for the model, encoding the recent traffic history necessary for predicting the next value.

### 3.2 Hidden Layers

The hidden layer configuration was determined through a combination of **trial-and-error and empirical rules of thumb**. Initially, several architectures were tested, and the following was found to provide a good balance between accuracy and training time:

- **1 hidden layer**

- **8 neurons** in the hidden layer

This configuration was sufficient to capture the nonlinear relationships in the data without leading to overfitting. The relatively small number of neurons was chosen deliberately to reduce computational complexity and promote generalization.

### 3.3 Output Layer

The output layer consists of **1 neuron**, which produces a single continuous value: the **predicted traffic at time *t+1***. This aligns with the regression nature of the task, where the model must output a real-valued estimate rather than a class label.

### 3.4 Activation Functions

Activation functions were chosen to introduce nonlinearity into the network and allow it to model complex relationships in the data.

- **Hidden Layer:** The **hyperbolic tangent (tanh)** activation function was used. Tanh outputs values in the range [-1, 1], which works well with normalized data and provides stronger gradients compared to sigmoid functions.

- **Output Layer:** A **linear activation** function was used, as it is standard practice in regression tasks where the output is a continuous variable.

This simple yet effective architecture allowed the model to learn temporal dependencies in traffic patterns without the need for more complex recurrent or convolutional structures.

---

Let me know if you'd like to visualize the architecture with a diagram or move on to **Section 4: Training the Network**.
