from bravemath.stat_functions.linreg import linear_regression
from bravemath.stat_functions.evaluate import rmse
import numpy as np

x, y = np.random.default_rng().multivariate_normal(
    [0.0326911, -0.1280782],
    [[5.96202397, -2.85602287], [-2.85602287, 3.47613949]],
    500).T

linreg = linear_regression().fit(x, y)
y_pred = linreg.prediction(x)

print(linreg.r_squared)
print(f"RMSE: {rmse(y, y_pred)}")
