import numpy as np
def standard_scaler(data):
    data = np.array(data, dtype=float)
    return (data - data.mean()) / data.std()