from preprocessing import minmax_scaler, standard_scaler
from metrics import (
    accuracy_score,
    mean_squared_error,
    mean_absolute_error,
    mean_absolute_percentage_error
)

data = [1, 2, 3, 4, 5]
print("MinMax:", minmax_scaler(data))
print("Standard:", standard_scaler(data))

y_true = [3, 5, 2, 7]
y_pred = [2.5, 5, 4, 8]

print("Accuracy:", accuracy_score([1,0,1], [1,0,0]))
print("MSE:", mean_squared_error(y_true, y_pred))
print("MAE:", mean_absolute_error(y_true, y_pred))
print("MAPE:", mean_absolute_percentage_error(y_true, y_pred))

