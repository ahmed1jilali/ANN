# Results and Discussion

This section presents and discusses the performance of the developed Multilayer Perceptron (MLP) model for forecasting hourly throughput in 4G mobile networks. The model, configured with two input neurons (representing throughput at hour t−1 and hour t), a hidden layer with three neurons using a sigmoid activation function, and an output layer with one neuron (predicting throughput at hour t+1) using a linear activation function, was trained on 90% of a 5000-hour throughput dataset and evaluated on the remaining 10%.

### 1. Overall Model Performance

The primary metric used to evaluate the model's predictive accuracy on the unseen test set is the **Coefficient of Determination (R2)**. The MLP model achieved an R2 score of **0.8198**, as indicated in the `test.txt` file. This signifies that approximately 81.98% of the variance in the next hour's network throughput can be explained by the throughput of the current and previous hours, using the developed MLP model. This level of accuracy suggests a good fit to the data and a considerable predictive capability for short-term traffic fluctuations.

---

### 2. Training Process Analysis

The training process of the MLP model was monitored by observing the Mean Squared Error (MSE) loss function over epochs. Figure 1 (your `80010562dd23a3cfbe270e68166a64d471f86940.png`) illustrates the training loss curve.

*Figure 1: Training Mean Squared Error (MSE) per Epoch.*

As depicted in Figure 1, the MSE shows a rapid decrease during the initial training epochs, followed by a plateau in later epochs. This behavior indicates that the model converged effectively, learning the underlying patterns from the training data without signs of instability. The stabilization of the loss suggests that the model has reached a point where further training on the same data with the current configuration is unlikely to yield significant improvements in fitting the training set.

---

### 3. Prediction Accuracy on Test Data

To assess the model's generalization capability, its predictions on the 10% hold-out test set (500 hours) were compared against the actual recorded throughput values.

#### 3.1. Actual vs. Predicted Throughput Over Time

Figure 2 (your `978489c473d1083a08d0a151a1e1f73d73a2b011.jpg`) provides a time-series comparison of the actual throughput and the MLP model's predictions on the test set.

*Figure 2: Actual vs. Predicted Throughput on the Test Set.*

The plot shows that the predicted throughput (orange line) generally follows the trends and patterns of the actual throughput (blue line). The model appears capable of capturing the cyclical variations and general fluctuations inherent in the mobile network traffic. However, it can be observed that the model's predictions are somewhat smoother than the actual data. Specifically, the model tends to underestimate the peaks (high traffic periods) and overestimate the troughs (low traffic periods). This smoothing effect is common in regression models that learn generalized trends and may indicate an opportunity for further model refinement to capture more extreme values.

#### 3.2. Scatter Plot of Actual vs. Predicted Values

Figure 3 (your `c1cf9c7dfeb81ff71c512286dd7d4fea12699bd1.png`) presents a scatter plot of the predicted throughput values against the actual throughput values for the test set. The red dashed line represents the ideal scenario where predicted values perfectly match actual values (y=x).

*Figure 3: Scatter Plot of Actual vs. Predicted Throughput on the Test Set.*

The concentration of points around the diagonal line visually confirms the strong positive correlation between predicted and actual values, which is quantitatively supported by the R2 score of 0.8198. The plot indicates that the model performs consistently across a range of throughput values. However, a slight tendency for the spread of points to increase at higher throughput values can be observed. This suggests that the model's prediction error might be larger during periods of very high traffic, a phenomenon known as heteroscedasticity. Such behavior is critical in network traffic prediction, as accurately forecasting peak loads is often most important for resource management.

---

### 4. Residual Analysis

A detailed analysis of the residuals (the differences between actual and predicted values) provides deeper insights into the model's behavior and its shortcomings. The `test.txt` file contains the raw residual values for the test set.

#### 4.1. Residuals Histogram

Figure 4 (your `ec8a622adfcfe5f051a42776a832f7d08fa73e72.png`) displays a histogram of the residual errors from the test set.

*Figure 4: Histogram of Residual Errors on the Test Set.*

The histogram shows that the residuals are approximately normally distributed and centered close to zero. This is a desirable characteristic, indicating that the model does not have a significant systematic bias (i.e., it doesn't consistently overpredict or underpredict across the board). The majority of prediction errors are relatively small, clustering around the mean. The spread of the distribution, along with some values in the tails (e.g., residuals ranging up to pm several thousands, as seen in `test.txt` which includes values like `1.74299593e+04`), indicates the typical magnitude of errors the model makes.

#### 4.2. Test Residuals Plot

Figure 5 (your `f005e2dafbd2186623b69043a7a17f9ab3e1fff7.png`) shows the residuals plotted against the predicted throughput values.

*Figure 5: Plot of Residuals vs. Predicted Values on the Test Set.*

Ideally, this plot should exhibit a random scatter of points around the horizontal line y=0, with no discernible patterns. The observed plot largely adheres to this, suggesting that the model's errors are mostly random and not strongly dependent on the magnitude of the predicted throughput. There isn't a clear funnel shape that would strongly indicate heteroscedasticity in this particular visualization against predicted values, although the scatter plot in Figure 3 did hint at larger errors for larger actual values. The absence of distinct patterns (e.g., curves or trends) in this residual plot reinforces that the model has captured the main systematic components of the traffic data based on the provided inputs.

### 4.2. Residuals vs. Predicted Values Analysis

A more rigorous diagnostic of the model's performance involves plotting the residuals against their corresponding predicted values. This analysis helps to identify systematic errors and determine if the model's prediction error is consistent across the range of predicted outputs. Figure 5 presents this scatter plot for the test set.

*Figure 5: Scatter Plot of Residuals vs. Predicted Values on the Test Set.*

**Ideal Behavior vs. Observed Results:**

Ideally, such a plot should display a random cloud of points centered around the horizontal line at `Residuals = 0`, with a constant vertical spread (variance) across the entire range of predicted values. This property is known as **homoscedasticity**, and its presence indicates that the model's error magnitude is independent of the predicted value's size.

As observed in Figure 5, the residuals are indeed centered around the zero line, suggesting the absence of a simple additive bias in the model's predictions. However, the plot exhibits a clear and significant pattern: the vertical spread of the residuals increases as the predicted throughput values increase. This forms a distinct "cone" or "fan" shape, which is a classic sign of **heteroscedasticity**.

**Interpretation and Scientific Implications:**

The presence of heteroscedasticity is a critical finding. It signifies that the variance of the model's error is not constant. In practical terms for 4G network traffic forecasting, this means:

- **The model's reliability is not uniform.** For low predicted throughput values (e.g., below 10,000), the prediction errors are relatively small and contained within a narrow band. In contrast, for high predicted throughput values (e.g., above 20,000), the errors become much larger and more unpredictable, with residuals spanning a significantly wider range (from approximately -20,000 to +40,000).
- **The model struggles most with peak traffic.** The plot clearly demonstrates that the model is least accurate precisely when it matters most: during periods of high network traffic. The ability to accurately forecast peak loads is paramount for network operators to perform crucial tasks like capacity planning, dynamic resource allocation, and congestion prevention. The model's degrading performance at higher traffic levels poses a significant limitation for its use in these critical applications.

This finding strongly confirms the suspicion raised by the initial scatter plot of actual vs. predicted values (Figure 3), which hinted at a larger spread for higher throughputs. This residual plot provides definitive visual evidence of this trend.

This heteroscedastic behavior could stem from several factors. The underlying nature of network traffic may simply be more volatile and less predictable during peak hours. Alternatively, the model's input features (throughput at hours t and t−1) may be insufficient to capture the complex, multiplicative dynamics that drive peak traffic, leading to larger errors when these dynamics are at play.

To address this issue in future work, a common strategy is to apply a variance-stabilizing transformation to the target variable, such as a **log transform** (`log(throughput)`). Training the model to predict the log of the throughput and then transforming the output back to the original scale can often mitigate heteroscedasticity and lead to more consistent and reliable predictions across all traffic levels.

---

### 5. Discussion

The results indicate that the relatively simple MLP model, utilizing only the throughput of the current and previous hour, provides a reasonably accurate forecast for the next hour's 4G network traffic, achieving an R2 of approximately 0.82. This level of accuracy can be valuable for short-term operational decisions in network management, such as dynamic bandwidth allocation or preemptive resource scaling to a certain extent. The sigmoid activation in the hidden layer allowed the model to capture non-linear relationships in the traffic data, while the linear output unit is appropriate for the regression task of predicting continuous throughput values.

Strengths and Limitations:

The model's strength lies in its simplicity and its ability to capture the general trend of traffic with minimal input features. The convergence of the training loss and the characteristics of the residuals suggest a stable and reasonably well-generalized model.

However, some limitations are evident. The model's tendency to smooth out predictions, particularly underestimating peaks and overestimating troughs (as seen in Figure 2), is a key concern. Accurate peak prediction is crucial for preventing network congestion and ensuring Quality of Service (QoS). The observation from the scatter plot (Figure 3) that error magnitudes might increase with higher traffic volumes further underscores this point. This behavior could be attributed to the limited input features (only two preceding hours), which might not be sufficient to capture all the complex dynamics, including abrupt changes or longer-term seasonality (e.g., daily or weekly patterns) influencing traffic peaks. The small number of hidden neurons (three) might also limit the model's capacity to learn more intricate patterns.

Implications for Traffic Forecasting:

For a 4G network operator, an R2 of 0.82 means the model can provide a good baseline for upcoming traffic conditions. This can aid in automated systems for network monitoring and initial resource adjustments. However, the observed underestimation of peak loads implies that relying solely on this model for critical peak-time resource allocation might carry risks. The magnitude of residuals, sometimes in the thousands (as per test.txt), needs to be considered in the context of the network's capacity and typical throughput levels to understand the practical impact of these errors.

Future Work:

Several avenues could be explored to potentially enhance the model's performance:

1. **Feature Engineering:** Incorporating more relevant input features could significantly improve accuracy. These might include:
   - More historical data points (e.g., traffic from T−2,T−3,...,T−N hours).
   - Time-based features like the hour of the day, day of the week, or indicators for holidays/special events, which strongly influence user behavior and network load.
2. **Model Complexity:** Experimenting with a more complex MLP architecture (e.g., more hidden layers or neurons) could be beneficial, though this would require careful regularization to avoid overfitting.
3. **Advanced Models:** For time-series forecasting, Recurrent Neural Networks (RNNs), particularly Long Short-Term Memory (LSTM) or Gated Recurrent Unit (GRU) networks, are often more adept at capturing long-range dependencies and temporal patterns. Comparing the MLP performance with these models would be a valuable exercise.
4. **Hybrid Models:** Combining machine learning models with traditional statistical time-series models (e.g., ARIMA) could potentially leverage the strengths of both approaches.
5. **Error Analysis:** A more detailed analysis of instances where the model performs poorly (e.g., during specific peak events) could provide insights into uncaptured dynamics.
6. **Validation Set:** Employing a separate validation set during training for hyperparameter tuning and early stopping would provide a more robust evaluation of the model's generalization ability and help prevent overfitting.

In conclusion, the developed MLP model demonstrates promising results for short-term 4G traffic forecasting using minimal input data. While it provides a solid foundation, the identified limitations and suggested future work highlight pathways for further improvements to achieve the higher accuracy and reliability often required for critical network management tasks.

---

**Note:**

- Remember to replace placeholders like `Figure X` with the actual figure numbers you use in your thesis.
- You might need to adjust the interpretation slightly if my visual assessment of the image scales or specific details is not perfectly aligned with the true data scales (e.g., the exact MSE value if it's legible, specific ranges on axes if they are crucial).
- The discussion of "units of throughput" is generic; if you know these units (e.g., Mbps, Gbps), you can make the interpretation of error magnitudes more concrete.
- Ensure you add the image files to a `./figures/` directory or adjust the path in the Markdown if you place them elsewhere when compiling your thesis.
