# Traffic forecasting in ...

## 1. Problem definition

### 1.1 Nature of the problem

With 4G mobile devices becoming more affordable and widely available, and the population using it getting larger, better ways to manage the 4G mobile network needs to emerge. Accurate traffic prediction is essential for effective network planning, resource allocation, and congestion management.

This thesis addresses a **regression problem**, where the goal is to predict a continuous value, more specifically the expected network throughput in the next hour based on historical data, where the forecasting model seeks to learn from previous traffic patterns and generalize this knowledge to predict future usage levels. We saw a Multilayer perceptron best fit for that role.

Forecasting the network traffic allows the anticipation of high demand periods, and optimizing the network performance accordingly, and thus preventing the congestion of the cellular network. We used a Multilayer perceptron for this task because it is a type of neural network that can learn patterns in data and make predictions based on them, even when the relationships between the input and output are nonlinear, which makes it well-suited for modeling the complex behavior of network throughput over time.

### 1.2 Input and output variables

The Multilayer Perceptron *(**MLP**)* model developed in this work uses the **throughput values of the current hour and the previous hour** as features. These values represent the history of the network usage, and are assumed to be highly indicative of short-term future behavior.

- **Input Features:**
  
  - Network throughput at time t-1
  
  - Network throughput at time t

- **Output Target:**
  
  - Forecasted throughput at time t+1

The model is trained to recognize sequential dependencies in traffic temporal patterns, where each input includes traffic from two consecutive hours, the model can learn how traffic evolves over time.

---

## 2. Data preprocessing

Preprocessing is a crucial step after gathering data, which makes the modeling more effective. This step depends on what task is to be performed and the characteristics of the data being handled.

### 2.1 Selection of inputs

To maintain a balance between  model simplicity and performance, only two features were selected as inputs: the throughput at the current hour $(t)$ and the previous hour $(t-1)$. These features were chosen based on the assumption that short-term past values are highly predictive of near-future traffic.

### 2.2 Normalization

A key step in preprocessing is normalizing the data, so that all values lie in the range [0,1], this is very helpful for neural networks, which tend to train more efficiently on uniformly scaled input data.

It also helps avoid exploding or vanishing gradients and improves convergence speed.

The normalization is shown in **Equation N03** where:

- $x_{i}^{normalized}$​ is the normalized value.

- $x_{i}$ is the current value to normalize.

- $x_{max}$ is the maximum value in the data.

- $x_{min}$ is the minimum value in the data.

$$
x_{i}^{normalized}​ = \frac{​x_{i}​−x_{min}}{x_{max}​−x_{min}}​​
$$

**Equation**: Normalization formula.

### 2.3 Splitting

The dataset used is consisted of **2000 hourly traffic records**, representing approximately 83 days of continuous traffic monitoring. This dataset was split into two subsets:

- **Training Set (70%)** – Used to train the model and update weights.
- **Testing Set (30%)** - Used to evaluate the final model’s performance on unseen data.

the splitting was performed chronologically to preserve the temporal order of the data. This is particularly important in time series forecasting, where the sequence of observations is a key factor.

## 3. Network architecture design

This section outlines the design decisions made for the Multilayer Perceptron (MLP) model used to forecast traffic in 4G mobile networks.

### 3.1 Input layer

The input layer is configured with 2 neurons, corresponding to the two selected input features:

- Throughput at time $t-1$

- Throughput at time $t$

These neurons serve as the entry point for the model.

### 3.2 Hidden layer

The hidden layer configuration was determined through a combination of trial-and-error, by varying the number of neurons in the hidden layer, **7 neurons** gave the best result, but this is heavily impacted by other factors like weight initialization and activation functions used. The small number of neurons was chosen deliberately to reduce computational complexity.

### 3.3 Output layer

The output layer consists of **1 neuron**, which produces a single normalized value *(the predicted traffic at time $t-1$)*.

### 3.4 Activation functions

Activation functions are chosen to introduce nonlinearity into the network and allow it to model complex relationships in the data.

**Hidden layer:** The **sigmoid** activation function was used. sigmoid maps input values to a ranger between 0 and 1, see [chapter 2 section 3 subsection 4]. While it can suffer from vanishing gradient issues in deeper networks, sigmoid is generally effective in small shallow networks like the one used in this study.

**Output layer:** A **Linear activation** function was used in the output layer to allow the model to produce a continues numerical output appropriate for regression tasks.

## 4. Training the network

Training a neural network involves adjusting its internal parameters *(weights and biases)* so that it can learn the relationship between inputs and outputs from data. This section details the approach taken to train the Multilayer Perceptron *(**MLP**)* for traffic forecasting.

### 4.1 Cost function

To measure the difference between the predicted and actual traffic values, the **Mean squared error** *(**MSE**)* was used as the cost function:

$$
MSE = \frac{1}{n}\sum_{i=1}^{n}(\hat{y_{i}} - y_{i})^2
$$

Where $\hat{y}$ is the predicted data, and the $y$ is the actual data. **MSE** is commonly used in regression proble3ms because it penalizes larger errors more heavily, encouraging the network to minimize deviations in predictions.

### 4.2 Weights initialization

Weights are adjusted during the training phase in the aim to minimize the difference between the predicted and desired outputs. Setting these weights correctly, called weight initialization, plays a critical role in speeding up the training process. Improper initialization can leads to issues like the vanishing and exploding gradients.

#### Vanishing Gradients:

When weights are very small, the gradients can become tiny, preventing the network from learning effectively.

#### Exploding Gradients:

When weights are too large, gradients can grow too fast, making the model unstable or causing it to fail to converge.
To counter these issues, two main techniques have emerged: Xavier Initialization and He Initialization.

#### Xavier Initialization:

Named after its creator, Xavier Glorot, this initialization method based on variance equality between input values and the output value of each layer, the variance of the weight in the forward propagation process should be:

$$
var(w_{i}) = \frac{1}{n_{in}}
$$

where $n_{in}$ is the number of input neurons 

if we go through backpropagation we get:

$$
var(w_{i}) = \frac{1}{n_{out}}
$$

where $n_{out}$ is the number of output neurons.

In the general case, the $n_{in}$ and $n_{out}$ of a layer may not be equal, Xavier and Bengio found a compromise using the average of the $n_{in}$ and the $n_{out}$ proposing that:

$$
var(w_{i}) = \frac{1}{n_{avg}}
$$

where $n_{avg} = \frac{n_{in} + n_{out}}{2}$

One good way is to assign the weights from a Gaussian distribution. The idea is to initialize weights using zero mean gaussian distribution with variance:

$$
\sigma^2 = \frac{2}{n_{in}+n_{out}}
$$

when the uniform distribution in the interval $[-a, a]$ is used such that:

$$
a = \sqrt{\frac{6}{n_{in}+{n_{out}}}}
$$

we get the same results as zero mean gaussian distribution described above.

Xavier and Bengio considered sigmoid activation function. The initialization strategy for **ReLU** activation function, sometimes called He initialization is to multiply the variance of the weights by 2, which gave in the case of zero mean gaussian distribution with variance:

$$
\sigma^2 = \frac{4}{n_{in}+n_{out}}
$$

In the case of uniform distribution the weights are generated in the interval $[-a, a]$ such that:

$$
a = \sqrt{\frac{12}{n_{in}+{n_{out}}}}
$$

### 4.3 Backpropagation *(gradient decent)*

The backpropagation algorithm was used to train the network by propagating the error from the output layer back through the hidden layers. for more details about the backpropagation algorithm the reader is invited to see `[chapter 2, section 4, subsection 4]`





## Results and discussions
