import numpy as np

def minmax_scaler(data):
    data = np.array(data, dtype=float)
    return (data - data.min()) / (data.max() - data.min())
