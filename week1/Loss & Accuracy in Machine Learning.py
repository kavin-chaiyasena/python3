import numpy as np

def MSE(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    return np.mean((pred - target) ** 2)

def MAE(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    return np.mean(np.abs(pred - target))

def Accuracy(pred, target):
    pred = np.array(pred)
    target = np.array(target)
    return np.mean(pred == target)

pred = [1, 2, 3, 4, 5]
target = [1, 2, 3, 0, 0]

print("MSE:", MSE(pred, target))
print("MAE:", MAE(pred, target))
print("Accuracy:", Accuracy(pred, target))
