## <mark>Results and discussions</mark>

For evaluating the performance of Multilayer perceptron *(**MLP**)* model implemented in forecasting traffic throughput in the 4G mobile network, Several experiments were conducted with varying hidden neuron counts. The dataset used was split using a 90/10 train-test ratio. The **MLP** was trained using Xavier initialization, with a learning rate of 1 and 7000 iterations across all tests to ensure consistency.

### <mark>5.1 Performance comparison</mark>

The following table summarizes the performance *(measured using the $R^2$ metric)* of the **MLP** model wither different neurons in the hidden layer:

| Number of neurons in hidden layer | weight initialization method | Learning rate | number of iterations | $R^2$ metric | RMSE |
|:---------------------------------:|:----------------------------:|:-------------:|:--------------------:|:------------:|:----:|
| 3                                 | Xavier Normal                | 1             | 7000                 | 0.8198       |      |
| 4                                 | Xavier Normal                | 1             | 7000                 | 0.8202       |      |
| 10                                | Xavier Normal                | 1             | 7000                 | 0.8110       |      |

### <mark>5.2 Model selection</mark>

The model with 3 hidden neurons was selected for production deployment, this was due to the model low complexity, which translates to:

- Faster training time

- Lower computational cost

- Simpler architecture 

Although the configuration with 4 hidden neurons slightly outperformed the other configurations in terms of the $R^2$ score *(0.8202)*, the marginal difference in performance of less than *0.005* did not justify the added complexity of additional neurons.

### <mark>5.3 Selected Model performance</mark>

The primary metric used to evaluate the mode's predictive accuracy on the test set is the **Coefficient of determination *($R^2$)***. The MLP model achieved an accuracy of about **81.98%**. This level of accuracy suggests a good fit to the data and a considerable predictive capability for short-term traffic fluctuations.

### <mark>5.4 Training process analysis</mark>

The training process of the **MLP** model was monitored by observing the Mean Squared Error *(**MSE**)* over epochs, **Figure** illustrates the training loss curve.<img title="" src="assets/80010562dd23a3cfbe270e68166a64d471f86940.png" alt="image" data-align="center" width="455">

`Training mean squared error (MSE) per epoch.`

As depicted in the **Figure**, the **MSE** shows a rapid decrease during the initial training epochs, then it levels in the rest, this behavior shows that the model has converged well without signs of instability, though the stabilization of the loss suggests that the model has reached a point where further training on the same data with the current configuration is unlikely to give any more improvements.

### <mark>5.5 Prediction accuracy on test data</mark>

To assess the model's forecasting capability. its predictions on the test set *(500 hours)* were compared against the actual recorded throughput values.

#### <mark>5.5.1 Actual vs predicted throughput over time</mark>

The **Figure** below provides a time series comparison of the actual throughput and the **MLP** model predictions on the test set.

<img title="" src="assets/978489c473d1083a08d0a151a1e1f73d73a2b011.png" alt="image" data-align="center" width="472">

`Actual vs predicted throughput on the test set.`

The plot shows that the predicted throughput *(orange line)* generally follows the trends and patterns of the actual throughput *(blue line)*. The model appears capable of capturing the general fluctuations of the mobile network traffic. However, it can be observed that the model's underestimate the peaks *(low traffic periods)*. `opportunity for further model refinement/ common in regression tasks`

#### <mark>5.5.2 Scatter plot of actual vs predicted values</mark>

The **Figure** below presents a scatter plot of the predicted throughput values against the actual throughput values for the test set. The red line represents the ideal scenario where predicted values perfectly match the actual values.

<img title="" src="assets/c1cf9c7dfeb81ff71c512286dd7d4fea12699bd1.png" alt="image" data-align="center" width="467">

`Scatter plot actual vs predicted throughput on the test set.`

The concentration of points around the diagonal line visually confirms the strong positive correlation between predicted and actual values, which is clearly supported by the $R^2$ score of 0.8198, the plot indicates that the model performs consistently across a range of throughput values. However, a slight tendency for the spread of points to  increase at higher throughput values can be observed.

```
error might be larger during periods of very high traffic
what can you read from scatter plots
heteroscedasticity
```

### <mark>5.6 Residual analysis</mark>

The analysis of the residuals *(the differences between actual and predicted values)* provides deeper insights into the model's behavior and it's shortcomings.

#### <mark>5.6.1 Residuals histogram</mark>

The **Figure** below displays a histogram of the residual errors from the test set.

<img title="" src="assets/ec8a622adfcfe5f051a42776a832f7d08fa73e72.png" alt="image" width="342" data-align="center">

`Histogram of residual errors on the test set.`

From the histogram it's clear that the residuals follow a normal distribution with mean of zero *(center)*. This is a desirable characteristic, indicating that the model accuracy is acceptable, and it also indicate that the model does not consistently make the same type of error, such as always overestimating or underestimating. Another observation is that the majority of prediction errors are relatively small, clustering around the mean, the spread of the distribution along with a few large values at the ends, shows how big the model's prediction errors can be.

#### <mark>5.6.2 Residuals vs. predicted values analysis</mark>

Plotting the residuals against the corresponding predicted values helps to determine if the model's prediction error is consistent across the range of predicted outputs. **Figure** presents this scatter plot for the test set.

<img title="" src="assets/287c32a715a9e9de2a265675ebda3132b44abcd7.png" alt="residuals vs predicted values (scatter plot).png" data-align="center" width="386">

`Scatter plot of residuals vs predicted values on the test set.`

As observed in **Figure** the residuals are centered around the zero line when the throughput value is less then 20000 Kbps, and at lower throughput values the residuals are tightly clustered around zero, which indicates that the model predictions are more accurate at low throughput values where congestion or network performance issues are present. Another observation at higher throughput values the residuals are more spread and taking on large values meaning that the model predictions is not accurate when predicting high throughput values.

### <mark>5.7 Discussion</mark>

The results shows that the relatively simple MLP model utilizing only the throughput of the current and previous hour provides a reasonably accurate forecast for the next hour in the 4G mobile network achieving an accuracy of approximately 82%.

While using the sigmoid activation function in the hidden the model was capable of capturing the non-linear relationships in the traffic data, while the linear activation function in the output unit is appropriate for the regression task of predicting the continuous throughput values.

However, several limitations were identified during the analysis including the model tendency to **underestimate during low traffic periods**, this behavior is visible in both the *actual vs predicted throughput over time plot* see **Figure** and *residuals vs. predicted values scatter plot* see **Figure**.

It's also clear that the model is more reliable at lower throughput values *(higher traffic)*, this can be seen in the normal distribution of the residuals where most of the residuals are centered around zero see **Figure** and the residuals vs. predicted values scatter plot in **Figure**.

Although this model is quite good at predicting the high traffic on the 4G network, more improvements can still be done, some of them are listed bellow:

- Increasing the inputs of the model *(more previous hours)*.

- Increasing the number of hidden layers.

- Incorporating additional features such as time of the day, day of the week, external factors *(weather, scheduled events, know maintenance, etc.)*

In summary the results show that the lightweight **MLP** model can be used effectively to forecast short-term mobile traffic, with clear strengths such as the models simplicity and fast training. Nonetheless the analysis also reveals areas where performance could also be improved to enhance the model robustness.

---

### 5.7 Discussion (continued)

The results indicate that even a relatively simple MLP architecture, trained with a limited input window (current and previous hour throughput), can achieve a predictive accuracy of approximately **82%**, as measured by the $R^2$ metric. This level of performance demonstrates that mobile network traffic exhibits patterns that can be effectively captured with basic neural network models and minimal input features.

However, several limitations were identified during the analysis. Firstly, the model showed a tendency to **underestimate during peak traffic periods** and **overestimate during low traffic periods**. This behavior, visible in both the time series comparison and the residual plots, suggests that the model may not be fully capturing the dynamics associated with traffic extremes. Such systematic deviations can be indicative of **nonlinearities** or **seasonal patterns** that are not fully represented in the current feature set or model complexity.

The scatter plots of actual versus predicted throughput and residuals versus predicted values also highlight a slight **heteroscedasticity**, where prediction errors increase with larger throughput values. While the residuals appear normally distributed and centered around zero — an indicator of unbiased estimation — this variance pattern suggests the model is more reliable at lower traffic volumes. This limitation is common in regression tasks and may warrant further investigation through **data transformation techniques**, **variance-stabilizing methods**, or **advanced architectures**.

Furthermore, the use of a **fixed train-test split** (90/10) without cross-validation, while sufficient for initial experimentation, may not fully account for **temporal variability or data drift** in real-world mobile networks. Incorporating **K-fold cross-validation** or **time series-aware validation methods** (e.g., walk-forward validation) in future work would enhance the robustness and generalizability of the findings.

The current MLP model employed a **sigmoid activation function** in the hidden layer and a **linear output**, both of which are appropriate for modeling nonlinear relationships in continuous-valued outputs. However, alternative architectures such as **recurrent neural networks (RNNs)**, **long short-term memory (LSTM)** networks, or even **temporal convolutional networks (TCNs)** could be explored to better exploit the temporal structure of network traffic data.

Another potential enhancement lies in **feature engineering**. While this study used only the current and previous hour throughput, incorporating additional features — such as **time-of-day**, **day-of-week**, **historical lag windows**, or **exogenous variables** (e.g., weather, scheduled events, or known maintenance) — may improve forecasting accuracy and help address the model’s limitations during high-traffic fluctuations.

In summary, the experimental results demonstrate that a lightweight MLP model can serve as a viable baseline for short-term mobile traffic prediction, with clear strengths in model simplicity, fast training, and interpretable behavior. Nonetheless, the analysis also reveals areas where performance could be improved, particularly in capturing extreme values and enhancing model robustness through richer inputs and more advanced validation strategies.

---

#### 5.6.2 Test residuals plot

Presented below is a **Figure** that shows the residuals plotted against the predicted throughput values.

<img title="" src="assets/f005e2dafbd2186623b69043a7a17f9ab3e1fff7.png" alt="image" data-align="center" width="435">

`Plot of residuals vs predicted values on the test set.`

This is a jagged meaningless line. The error for a prediction at a point is not sequentially relat4ed to the error for a prediction of another point. They are independent events. Connecting them with a line would imply a trend that doesn't exist.

---

---

before denormalization $RMSE = \sqrt{\frac{1}{2n}\sum_{i=1}^{n}(\hat{y_{i}}-y_{i})^2}$

```
hidden_neurons=4
Test R² Score: 0.8202

hidden_neurons=10
Test R² Score: 0.8110

hidden_neurons=3
Test R² Score: 0.8198
```

```

```

![image](assets/978489c473d1083a08d0a151a1e1f73d73a2b011.png)![image](assets/80010562dd23a3cfbe270e68166a64d471f86940.png)![image](assets/c1cf9c7dfeb81ff71c512286dd7d4fea12699bd1.png)![image](assets/ec8a622adfcfe5f051a42776a832f7d08fa73e72.png)![image](assets/f005e2dafbd2186623b69043a7a17f9ab3e1fff7.png)

![residuals vs predicted values (scatter plot).png](assets/287c32a715a9e9de2a265675ebda3132b44abcd7.png)

---

---

## heteroscedasticity

![Heteroscedasticity](https://pro.arcgis.com/en/pro-app/latest/tool-reference/spatial-statistics/GUID-7C48F030-BC6E-42B6-97E4-4056CF6B8E6C-web.png)

The cone-shaped scatterplot indicates that the model performs differently depending on the magnitude of the estimated value. In this case, the model performs better (the residuals are smaller) for tracts with fewer crimes than for tracts with many crimes.

![](assets/2025-06-04-21-16-47-image.png)

| Issue                    | Suggestion                                                        |
| ------------------------ | ----------------------------------------------------------------- |
| Missing RMSE values      | Add RMSE to performance table                                     |
| High learning rate       | Justify or adjust                                                 |
| Feature selection        | Explain input choice                                              |
| Lack of cross-validation | Discuss or acknowledge                                            |
| Grammar/typos            | Proofread and correct                                             |
| Figure references        | Number and cite consistently                                      |
| Statistical significance | Add or acknowledge                                                |
| Residual analysis        | Link observations to model assumptions (e.g., heteroscedasticity) |
