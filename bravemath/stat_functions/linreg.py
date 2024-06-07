import numpy as np
from bravemath import stat_functions


class LinearRegression:
    def __init__(self, coef=None, intercept=None, model=None):
        self.coef = coef
        self.intercept = intercept
        self.model = model
    @classmethod
    def fit(cls, x_var, y_var):
        r_corr = stat_functions.correlation(x_var, y_var)
        cls.coef = r_corr * (np.std(y_var, ddof=1) / np.std(x_var, ddof=1))
        cls.intercept = np.mean(y_var) - (cls.coef * np.mean(x_var))
        if cls.intercept < 0:
            cls.model = f"linearmodel = {cls.coef:.3f}x {cls.intercept:.3f}"
        else:
            cls.model = f"linearmodel = {cls.coef:.3f}x + {cls.intercept:.3f}"
        return cls


if __name__ == '__main__':
    x = [1, 2, 2, 3]
    y = [1, 2, 3, 6]

    linreg = LinearRegression().fit(x, y)
    print(linreg.model, linreg.coef, linreg.intercept)