# Introduction

Observations from the study of biological systems served as the inspiration for the mathematical creation of artificial neural networks which offer a new approach to problems of perception, learning, memory, and reasoning. They infer emergent properties that allow us to solve problems that were considered complex before and prove to be very promising alternatives for circumventing some of the limitations of conventional computers [1]. 

The brain learning process consists of either establishing new connections or modifying existing ones. Based on this concept, we build artificial models of neurons and train them to eventually perform useful functions, even if the networks we develop possess only a tiny fraction of the power of the human brain. Artificial neural networks are not any more similar to real neurons than feathers are to modern airplanes, despite being modeled after the connections between neurons present in biological systems. Although both biological systems—feathers and neurons—have practical uses, the application of the underlying principles has led to the development of artificial inventions that are very different from the biological systems [2].

Neural networks find applications in various fields. Among them, airplane autopilot, car guidance, signal processing systems, speech synthesis and speaker recognition, computer vision and face recognition, forecasting the monetary markets, assessing financial or insurance risk, medical diagnosis, oil and gas exploration, robotics, telecommunications, etc. 

There are different types of neural networks, each performing a specific function, among them, modeling, classification, and control. The most commonly used type of Neural Networks is the multi-layer perceptron.

In this section, we will introduce neurons and their properties, layered neural networks as well as learning algorithms.

# Neuron Model:

## Biological neuron:

The biological neuron is composed of a cell **body** containing the nucleus, an **axon** that transmit information via its synaptic terminals and **dendrites** that receive inputs from other neurons via synapses.[^3]

![](C:\Users\white\AppData\Roaming\marktext\images\2025-05-21-15-14-10-The-biological-neuron.png)

**Figure 2.1**: biological neruon

## Artificial neuron:

The artificial neuron is inspired by the biological neuron model; it consists of an integrator that performs the weighted sum of its inputs. The result of this sum is then transformed by a transfer function, which produces the output of the neuron; a model of a neuron is presented in **Figure 2.2***. [^4]

![](C:\Users\white\AppData\Roaming\marktext\images\2025-05-21-15-34-06-image.png)

**Figure 2.2** artificial neuron model



[^4] `R ´ESEAUX DE NEURONES
GIF-21140 et GIF-64326
par Marc Parizeau
Automne 2004`

$z$ : is the weighted sum of the input values plus the biases, the output of the neuron will $a$

$$
z = \sum_{i=1}^{n} w_{i,j} x_{i} + b

$$

**Equation N01**



$$
a = f(z)
$$

**Equation N02**



The neural network can be represented in matrix form as 

$$
a = f(\sum_{i=1}^{n} w_{i,j}x_{i} + b)
$$

such that $w$ is the $(n, 1)$ matrix of weights of the neuron connections  

![](C:\Users\white\AppData\Roaming\marktext\images\2025-05-21-16-09-24-image.png)

**Figure 2.3**: matrix representation of an artificial neuron model



## Activation functions:

There exists various types of activation functions, among them, threshhold function, liniar function, sigmoid funciton and hyperbolic function.

The usual activation functions of a neuron are summerised in the table below:


![](C:\Users\white\AppData\Roaming\marktext\images\2025-05-21-16-15-11-image.png)

**Table 2.1**: usual activation functions



## Layerd neural networks:

Neural networks  are structured in layers *(input layer, hidden layers, output layer)*, each layer is composed by a number of neurons.

The structure in **Figure 2.4** presents a neural network scheme with input layer, one hidden layer, and an output layer.

![](C:\Users\white\AppData\Roaming\marktext\images\2025-05-21-16-34-53-image.png)

**Figure 2.4**:  neural network structure with one hidden layer

The weight matrix of a such network is given as:

$$
W =\begin{bmatrix} w_{1,1} & w_{1,2} & ... & w_{1, n}\\
w_{2,1} & w_{2,2}  & ... & w_{2, n} \\
... & ... & ... & ... & \\
w_{m,1} & w_{m,2}  & ... & w_{m, n} \\
\end{bmatrix}




$$



Each row of the matrix represents the number of an input to the network, and each column represents the number of neurons in the hidden layer.

In the case of a connection between two layers of a multilayer network, the rows represent the outputs of the previous layer and the columns represent the inputs of the next layer.



## Learning process:

Learning is an iterative process that update the parameters of a network in response to its environment excitation. The learning type is determined by the way in which the parameter updates.

The learning process is based on minimization of the error between the output calculated by the neural network and the actual output. The connection weights between the different neurons will be adjusted after computing the error.



## Supervised / Unsupervised learning process:

Learning process has been distinguished depending on whether the desired output is present to calculate the difference between it and the outputs computed by the neural network in order to adjust the network's weights *(supervised learning process)* or not *(unsupervised leaning process)*.



![](C:\Users\white\AppData\Roaming\marktext\images\2025-05-21-17-05-17-image.png)

**Figure 2.5**: Supervised learning diagram.




