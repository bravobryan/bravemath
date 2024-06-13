from bravemath.stat_functions.linreg import linear_regression
from bravemath.stat_functions.evaluate import rmse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


x = np.array([3.46, 3.36, 1.37, 3.82, 2.75, 0.73, 0.17, 1.20, 2.30, 2.06,
     2.56, 2.04, 3.70, 2.50, 1.02, 2.11, 3.15, 0.83, 2.81, 0.23])
y = np.array([2307.23, 2290.87, 23.44, 5285.55, 562.34, 6.44, 1.77, 19.02, 199.53,
     114.82, 363.08, 131.58, 6014.25, 316.23, 12.57, 128.82, 1412.54, 5.41, 516.52,  1.70])
y_log = np.log(y)

linreg = linear_regression().fit(x_var=x, y_var=y)
linreg.visualize()

linreg_log = linear_regression.fit(x, y_log)
linreg_log.visualize()