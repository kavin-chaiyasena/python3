import numpy as np

def MSE(pred: np.array, target: np.array) -> float:
    return np.mean((pred - target) ** 2)

def MAE(pred, target) -> float:
    return np.mean(np.abs(pred - target))

def Accuracy(pred, target):
    return np.mean(pred == target)

pred = np.array([1,2,3,2,1])
target = np.array([1,2,2,3,0])

print("MSE:", MSE(pred, target))
print("MAE:", MAE(pred, target))
print("Accuracy:", Accuracy(pred, target))