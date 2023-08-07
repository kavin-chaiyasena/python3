import numpy as np

def MSE(pred: np.ndarray, target: np.ndarray) -> np.ndarray:
    err = pred - target
    sq_err = err ** 2
    return np.mean(sq_err, axis=1)

def MAE(pred: np.ndarray, target: np.ndarray) -> np.ndarray:
    err = pred - target
    abs_err = np.abs(err)
    return np.mean(abs_err, axis=1)

def Accuracy(pred: np.ndarray, target: np.ndarray) -> float:
    correct_predictions = np.sum(pred == target, axis=1)
    data_num = pred.shape[1]
    return correct_predictions / data_num

pred = np.array([[1, 2, 3, 2, 1], [3, 2, 1, 1, 3]])
target = np.array([[1, 2, 2, 3, 0], [3, 2, 1, 3, 3]])

print("MSE:", MSE(pred, target))
print("MAE:", MAE(pred, target))
print("Accuracy:", Accuracy(pred, target))