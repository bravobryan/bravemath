import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bravemath import stat_functions


class linear_regression:
    def __init__(
            self, coef=None, intercept=None, model="linear_regression not fit.", variables={},
            r_squared=None
    ):
        """ Instantiates the linear regression object.
        ***** Note: Please don't use this for analysis. *****
        This object class was created to help solidify my understanding in creating the least squares
        linear regression model. There are better library packages out there that provide better
        analysis tools.
        """
        self.coef = coef
        self.intercept = intercept
        self.model = model
        self.variables = variables
        self.r_squared = r_squared


    @classmethod
    def fit(cls, x_var, y_var):
        """
        Fits least squares linear regression model using one feature.
        :param x_var: Explanatory Variable
        :param y_var: Response Variable
        :return: Fits linear_regression attributes to model.
        """
        # -- Calculate coefficient
        r_corr = stat_functions.correlation(x_var, y_var)
        cls.coef = float(r_corr * (np.std(y_var, ddof=1) / np.std(x_var, ddof=1)))

        # -- Calculate model's intercept
        cls.intercept = float(np.mean(y_var) - (cls.coef * np.mean(x_var)))

        # -- model equation
        cls.model = f"y_hat = {cls.intercept:.2f} + {cls.coef:.2f}x"
        y_pred = [cls.intercept + (cls.coef * x) for x in x_var]

        # -- Calculate r_squared value - Coeffecient of Determination
        values = np.column_stack((y_var, y_pred))
        y_mean = np.mean(values[0])
        sqr_error_ypred = np.sum(np.square([row[0] - row[1] for row in values]))
        sqr_error_ymean = np.sum(np.square([row[0] - y_mean for row in values]))
        r_sqr = 1 - (sqr_error_ypred / sqr_error_ymean)
        cls.r_squared = r_sqr

        cls.variables = {"explanatory":x_var, "response":y_var, "y_pred": y_pred}
        return cls


    @classmethod
    def prediction(cls, x_var):
        """
        calculates predictions using fitted model.
        :param x_var: Explanatory Variable, 1-D array or list
        :return: Numpy array of Prediction values
        """
        y_pred = np.array([cls.intercept + (cls.coef * x) for x in x_var])
        return y_pred

    @classmethod
    def visualize(cls, scale='auto'):
        """
        Generates a scatterplot with the linear regression line.
        """
        try:
            plt.scatter(cls.variables['explanatory'], cls.variables['response'], alpha=0.5)
            plt.axline((0, cls.intercept), slope=cls.coef, color='green', linestyle="--")
            plt.title(f"Linear Regression Model \n{cls.model}")
            plt.axis(scale)
            plt.grid()
            return plt.show()

        except AttributeError:
            print("***** Please fit linear_regression model, then Try again! *****")



if __name__ == '__main__':
    from sklearn.linear_model import LinearRegression

    x, y = np.random.default_rng().multivariate_normal(
        [10, 20],
        [[5.96202397, -2.85602287], [-2.85602287, 3.47613949]],
        500).T

    # -- Code to test if my linear regression algorithm is correct using SciKit-Learn's LinearRegression Object class.
    mylinreg = linear_regression().fit(x, y)
    x = np.reshape(x, (-1, 1))
    sklinreg = LinearRegression().fit(x, y)
    print(f"My regression model:            {mylinreg.model}")
    print(f"Sklearn's regression model:     y_hat = {sklinreg.intercept_:.2f} + {sklinreg.coef_[0]:.2f}x")

    # Test r_squared
    print(f"Coefficient of Determination: {mylinreg.r_squared:.3f} r^2")

    # Test `.viszualize()` method.
    mylinreg.visualize()
