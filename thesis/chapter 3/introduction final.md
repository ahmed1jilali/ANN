### Introduction

In this chapter we'll present the development of a machine learning model for traffic forecasting in 4G mobile networks. It is know that accurate forecasting helps in ensuring quality of service such as preventing congestion in the network and optimizing resource allocation. The chosen approach is a Multilayer Perceptron \textit{(textbf{MLP})}, a type of feedforward neural network known for its ability to model nonlinear relationships see \textbf{Subsection \ref{subsec:MLP}}. The final objective is to predict the network \textbf{throughput} of the next hour based on the current and previous hours, using minimal yet effective architecture. The roadmap we took to achieve such objective is illustrated in the \textbf{Figure \ref{fig:MLPDevRoadMap}} below.



![methodology.png](assets/395de7384284752513d9150b4e206d129c677ac3.png)

`Multilayer Perceptron development roadmap.`



### Conclusion

In this chapter we outlined the complete process of building a Multilayer Perceptron for traffic forecasting in 4G mobile networks, starting from the definition of the problem and selecting the input-output variables, we then proceeded through data preprocessing and weight initialization, we also demonstrated the model training using different architectures and choosing the best architecture for the objective use case, then we evaluated the chosen architecture using different techniques and plots, finally we discussed the chosen architecture reliability and further optimizations.
From the work presented in this chapter it's safe to conclude that the final results achieved the objective of forecasting the throughput in the 4th generation mobile network, especially predicting the low levels of throughput to prevent congestion.
