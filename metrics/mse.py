import numpy as np
def mean_squared_error(y_true, y_pred):
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    return ((y_true - y_pred) ** 2).mean()