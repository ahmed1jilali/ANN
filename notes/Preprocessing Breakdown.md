Certainly! Let's walk through the **data preprocessing** step-by-step, focusing on what it's doing and **why it's necessary** for training a neural network, especially for a time series prediction problem like this one.

---

## 🔄 Step-by-Step Preprocessing Breakdown

---

### 📂 1. **Reading the Data**

```python
df = pd.read_csv("throughput.csv", header=None)
values = df.values.flatten()
```

- **What it does**:
  
  - Loads a CSV file containing a single column of throughput measurements (probably one per hour).
  
  - `flatten()` converts it from a 2D array to a 1D array, which makes it easier to index.

- **Why it matters**: Neural networks work with numeric arrays, so loading and flattening the data makes it suitable for processing.

---

### 📉 2. **Normalization to [0, 1]**

```python
min_val, max_val = values.min(), values.max()
normalized = (values - min_val) / (max_val - min_val)
```

- **What it does**:
  
  - Scales the throughput values to fall between 0 and 1 using **min-max normalization**.

- **Why it's necessary**:
  
  - Neural networks (especially with sigmoid/tanh activations) train much more effectively when inputs are scaled to a standard range.
  
  - Helps avoid exploding/vanishing gradients and improves convergence speed.

---

### 📊 3. **Splitting Data into Train/Test Sets**

```python
split_point = int(0.7 * len(normalized))
train_series = normalized[:split_point]
test_series = normalized[split_point - 2:]  # include 2 back steps for sliding window
```

- **What it does**:
  
  - Splits the data into 70% training and 30% testing.
  
  - `test_series` starts 2 steps earlier to ensure that the input window (of 2 values) is valid at the start of test data.

- **Why it's necessary**:
  
  - Prevents information leakage from future points (you train on past data and predict future data).
  
  - Maintains temporal structure, which is critical for time series.

---

### 🧩 4. **Creating Sliding Windows for Inputs and Targets (Train)**

```python
X_train, y_train = [], []
for i in range(len(train_series) - 2):
    X_train.append([train_series[i], train_series[i + 1]])
    y_train.append([train_series[i + 2]])
X_train = np.array(X_train)
y_train = np.array(y_train)
```

- **What it does**:
  
  - Builds training samples using a sliding window of **2 inputs to predict the 3rd**.
  
  - For example:
    
    - Input: `[x₀, x₁]`, Target: `x₂`
    
    - Input: `[x₁, x₂]`, Target: `x₃`
    
    - etc.

- **Why it's necessary**:
  
  - Converts the 1D time series into a **supervised learning format**, which MLPs require.
  
  - This allows the model to learn a mapping from past values to the future value.

---

### 🧪 5. **Same Sliding Window for Test Set**

```python
X_test, y_test = [], []
for i in range(len(test_series) - 2):
    X_test.append([test_series[i], test_series[i + 1]])
    y_test.append([test_series[i + 2]])
X_test = np.array(X_test)
y_test = np.array(y_test)
```

- **Same logic** as above, just applied to the test set.

- Ensures consistency between training and test features.

---

### 📈 6. **Denormalizing the Predictions**

```python
y_pred_denorm = y_pred.flatten() * (max_val - min_val) + min_val
y_test_denorm = y_test.flatten() * (max_val - min_val) + min_val
```

- **What it does**:
  
  - Converts the normalized predictions and actual test values back to their original scale.

- **Why it's necessary**:
  
  - To interpret and compare predictions in real-world units (e.g. throughput in Kb/s).
  
  - Ensures the evaluation (e.g., MSE, plots) is meaningful.

---

## 🔚 Summary

| Step               | Action               | Purpose                                 |
| ------------------ | -------------------- | --------------------------------------- |
| 📥 Load            | CSV → 1D array       | Extract raw throughput values           |
| ⚖ Normalize        | [0, 1]               | Stabilize training, improve convergence |
| 🔀 Split           | 70% train / 30% test | Ensure proper evaluation                |
| 🔄 Windowing       | 2 inputs → 1 output  | Format for MLP training                 |
| 🧪 Repeat for test | Apply same format    | Ensure consistent evaluation            |
| ↩ Denormalize      | Undo scaling         | Get results in real-world units         |

---

Let me know if you'd like to visualize the sliding window or see how to generalize this for `n` past steps instead of just 2!

---

## 🎯 Goal of Normalization

The purpose of normalization (specifically **min-max scaling**) is to transform the data so that all values lie in the range . This is particularly helpful for neural networks, which tend to train more efficiently on uniformly scaled input data.

---

## 🧮 The Math Behind Min-Max Normalization

Given a vector of values:

Let:

Each individual value is normalized using the formula:

---

### 📌 Example

Suppose your data is:

Then:

Normalize each value:

So your normalized vector becomes:

---

## 🔁 Denormalization

To reverse this process (e.g., to get predictions back to their original scale):

---

## ✅ Why It Works

This transformation:

- Keeps the **relative distances** between data points the same.

- Guarantees that all values fall in the range.

- Makes gradients more stable during training in MLPs.

---

---

## 🔢 Your Code:

```python
min_val, max_val = values.min(), values.max()
normalized = (values - min_val) / (max_val - min_val)
```

---

## 🔁 Mathematical Equivalent:

### Step-by-step mapping:

| **Math** | **Code**                                                |
| -------- | ------------------------------------------------------- |
|          | `min_val = values.min()`                                |
|          | `max_val = values.max()`                                |
|          | `normalized = (values - min_val) / (max_val - min_val)` |

✅ **Yes**, this line in your code:

```python
normalized = (values - min_val) / (max_val - min_val)
```

**implements the exact formula**:

---

## 🔁 Denormalization in Your Code:

```python
y_pred_denorm = y_pred.flatten() * (max_val - min_val) + min_val
y_test_denorm = y_test.flatten() * (max_val - min_val) + min_val
```

This is the inverse of the normalization formula:

✅ Again, **perfect match** to the mathematical inverse operation.

---

### 🔍 Summary

| Purpose     | Math | Code                                       |
| ----------- | ---- | ------------------------------------------ |
| Normalize   |      | `(values - min_val) / (max_val - min_val)` |
| Denormalize |      | `x * (max_val - min_val) + min_val`        |

The plot shows the three stages:

1. **Original Values** (blue): These are the raw throughput data points.

2. **Normalized (0–1)** (orange): Values have been scaled to the range using min-max normalization.

3. **Denormalized** (green dashed): These values have been converted back to their original scale from the normalized data.

As you can see, the **denormalized values exactly match the original values**, confirming that the normalization and denormalization math works as intended.
