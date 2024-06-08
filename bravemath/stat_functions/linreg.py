import numpy as np
from bravemath import stat_functions


class linear_regression:
    def __init__(self, coef=None, intercept=None, model=None):
        """ Instantiates the linear regression object.
        Note: Please don't use this for analysis.
        This object class was created to help solidify my understanding in creating a least squares
        linear regression model. There are better library packages out there that provide better
        analysis tools. """
        self.coef = coef
        self.intercept = intercept
        self.model = model
    @classmethod
    def fit(cls, x_var, y_var):
        r_corr = stat_functions.correlation(x_var, y_var)
        cls.coef = r_corr * (np.std(y_var, ddof=1) / np.std(x_var, ddof=1))
        cls.intercept = np.mean(y_var) - (cls.coef * np.mean(x_var))
        cls.model = f"y_hat = {cls.intercept:.2f} + {cls.coef:.2f}x"
        return cls


if __name__ == '__main__':
    from sklearn.linear_model import LinearRegression
    print(help(linear_regression))
    x = [1, 2, 2, 3]
    y = [1, 2, 3, 6]

    # -- Code to test if my linear regression algorithm is correct using SciKit Learn's LinearRegression Object class.
    mylinreg = linear_regression().fit(x, y)

    x = np.reshape(x, (-1, 1))
    sklinreg = LinearRegression().fit(x, y)
    print(f"My regression model:            {mylinreg.model}")
    print(f"Sklearn's regression model:     y_hat = {sklinreg.intercept_:.2f} + {sklinreg.coef_[0]:.2f}x")