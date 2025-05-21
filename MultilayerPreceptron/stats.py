import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

class Stats:
    def __init__(self, y_test_denorm, y_pred_denorm, errors):
        self.y_test_denorm = y_test_denorm
        self.y_pred_denorm = y_pred_denorm
        self.errors = errors

    def plotThroughput(self):
        plt.figure(figsize=(12, 6))
        plt.plot(self.y_test_denorm, label="Actual Throughput", color='dodgerblue')
        plt.plot(self.y_pred_denorm, label="Predicted Throughput", color='coral', linestyle='--')
        plt.title("Network Throughput Prediction (Test Set)")
        plt.xlabel("Hour Index")
        plt.ylabel("Throughput (Kb/s)")

        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('output.png', format='png', dpi=600, transparent=True)
        plt.show()

    def mse(self):
        return mean_squared_error(self.y_test_denorm, self.y_pred_denorm)
    
    def r2(self):
        return r2_score(self.y_test_denorm, self.y_pred_denorm)

    def residuals(self):
        return self.y_test_denorm - self.y_pred_denorm
    
    def plotResiduals(self):
        plt.figure(figsize=(10, 4))
        plt.plot(self.residuals(), label="Residuals", color='purple')
        plt.axhline(0, linestyle='--', color='black')
        plt.title("Residual Errors (y_actual - y_predicted)")
        plt.xlabel("Hour Index")
        plt.ylabel("Error (Kb/s)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def predictionVsActualScatterPlot(self):
        plt.figure(figsize=(6, 6))
        plt.scatter(self.y_test_denorm, self.y_pred_denorm, alpha=0.6, color='green')
        plt.plot([self.y_test_denorm.min(), self.y_test_denorm.max()],
                [self.y_test_denorm.min(), self.y_test_denorm.max()],
                color='red', linestyle='--')
        plt.title("Predicted vs Actual Throughput")
        plt.xlabel("Actual Throughput")
        plt.ylabel("Predicted Throughput")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    def lossCurveOverEpochs(self):
        plt.figure(figsize=(10, 4))
        plt.plot(self.errors, label="Training Loss (MSE)", color='red')
        plt.title("MLP Training Loss Over Iterations")
        plt.xlabel("Iteration")
        plt.ylabel("MSE")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()






# Manual MSE
# mse = np.mean((y_test_denorm - y_pred_denorm) ** 2)

# Manual R²
# ss_res = np.sum((y_test_denorm - y_pred_denorm) ** 2)
# ss_tot = np.sum((y_test_denorm - np.mean(y_test_denorm)) ** 2)
# r2 = 1 - (ss_res / ss_tot)

# print(f"Mean Squared Error (MSE): {mse:.4f}")
# print(f"R-squared (R²): {r2:.4f}")

# Mean Squared Error (MSE): 12298979.3378
# R-squared (R²): 0.8114