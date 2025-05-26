# Activation functions:

## step function

It was used by McCulloch and Pitts in their model of the formal neuron. It causes the neuron's activation to switch from one value to another as soon as the resulting input exceeds a certain threshold (Equation III.2). Thresholding introduces a non-linearity in the behavior of the neuron. However, it limits the range of its possible responses to two values (Figure III.3).  
The drawback of this function is that it is not differentiable, which poses a problem for gradient-based algorithms. The equation that defines the neuron's state is [6].



The step function was used by McCulloch and Pitts in their precptron. It determines whether a neuron should activate or not based on wether the weighted sum of inputs excceds a threshold.

The mathematical equation for the step function is given as:

$$
f(x) = 
\begin{cases}
1 & \text{if } \sum_{i=1}^{n} w_i x_i + b \geq \theta \\
0 & \text{otherwise}
\end{cases}
$$

**Equation** the step function equation

where:

- $x_{i}$ are the inputs of the neuron.

- $w_{i}$ are the weights corresponding to the inputs.

- $b$ is the bias.

- $θ$ is the activation threshold.

- $f(x)$ is the output of the neuron.



<img src="assets/2025-05-25-13-17-02-image.png" title="" alt="" data-align="center">

**Figure** the step function graph





## Identity Function

The state is calculated using the following equation.  
We observe that this function allows **unbounded values** for the state, which can lead to **overflows during simulation**.  
It is used, among others, by **Kohonen, T.**, to construct his model of **associative memories** [6]
































