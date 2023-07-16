import numpy as np

def MSE_2D(pred, target):
    return np.mean((np.array(pred) - np.array(target)) ** 2, axis=1)

def MAE_2D(pred, target):
    return np.mean(np.abs(np.array(pred) - np.array(target)), axis=1)

def Accuracy_2D(pred, target):
    return np.mean(np.array(pred) == np.array(target), axis=1)

pred = [[1, 0, 1], [0, 1, 1]]
target = [[1, 1, 1], [0, 0, 1]]

print("MSE:", MSE_2D(pred, target))
print("MAE:", MAE_2D(pred, target))
print("Accuracy:", Accuracy_2D(pred, target))