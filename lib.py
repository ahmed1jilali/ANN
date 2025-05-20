import numpy as np
# from matplotlib import pyplot as plt


def random_weights(X, random_state: int):
    rand = np.random.RandomState(random_state)
    w = rand.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
    return w

def net_input(X, w):
    return np.dot(X, w[1:]) + w[0]

# def net_input(X, w):
#     result = []
#     for i in range(len(X)):
#         ws =  w[0]
#         for j in  range(len(X[i])):
#             ws += X[i][j] * w[j+1]
#         result.append(ws)
#     return result

# def predict(X, w):
#     net = net_input(X, w)
#     results = []
#     for i in range(len(net)):
#         if net[i] >= 0:
#             results.append(1)
#         else:
#             results.append(-1)
#     return results

def predict(X, w):
    return np.where(net_input(X, w) >= 0.0, 1, -1)

def fit(X, y, eta=0.001, n_iter=100):
    errors = []
    w = random_weights(X, random_state=1)
    for exemplar in range(n_iter):
        error = 0
        for xi, target in zip(X, y):
            delta = eta * (target - predict(xi, w))
            w[1:] += delta * xi
            w[0] += delta
            error += int(delta != 0.0)
        errors.append(error)
    return w, errors



# X = np.array(
#     [
#         [1.5, 2.3],
#         [3.1, 4.7],
#         [5.4, 6.8]
#     ]
# )


# weights = random_weights(X, 3)
# print(predict(X, weights))

#___random_weights
# [0.01788628 0.01788628  0.00096497]

#___net_input
# [
#     0.01788628 + (1.5 *0.0043651) +  (2.3 *  0.00096497),
#     0.01788628 + (3.1 *0.0043651) +  (4.7 *  0.00096497),
#     0.01788628 + (5.4 *0.0043651) +  (6.8 *  0.00096497)
# ]
# [
#     0.026653361,
#     0.035953449,
#     0.048019616
# ]

#___predict
# [
#     1,
#     1,
#     1
# ]

# print(weights)
# plt.plot(weights)
# plt.show()



