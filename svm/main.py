import pandas as pd
import numpy as np

# Load your data
df = pd.read_csv("throughput.csv")  # This file should have a column named 'throughput'
throughput_series = df["throughput"].values

# Create sequences: use last N hours to predict next hour
def create_sequences(data, window_size=24):
    X, y = [], []
    for i in range(len(data) - window_size):
        X.append(data[i:i+window_size])
        y.append(data[i+window_size])
    return np.array(X), np.array(y)

X, y = create_sequences(throughput_series, window_size=24)  # Using 24 past hours


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, shuffle=False  # Don't shuffle for time series
)


from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

# SVM works better with normalized data
model = make_pipeline(StandardScaler(), SVR(kernel='rbf', C=100, gamma=0.1, epsilon=0.1))
model.fit(X_train, y_train)


from sklearn.metrics import mean_squared_error, r2_score

y_pred = model.predict(X_test)

print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
print("R² Score:", r2_score(y_test, y_pred))


import matplotlib.pyplot as plt

plt.plot(y_test, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.title('SVM Throughput Prediction')
plt.xlabel('Time')
plt.ylabel('Throughput')
plt.legend()
plt.show()
