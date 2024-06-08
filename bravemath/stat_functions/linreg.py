import numpy as np
from bravemath import stat_functions


class linear_regression:
    def __init__(
            self, coef=None, intercept=None, model="linear_regression not fit.", variables={}
    ):
        """ Instantiates the linear regression object.
        ***** Note: Please don't use this for analysis. *****
        This object class was created to help solidify my understanding in creating a least squares
        linear regression model. There are better library packages out there that provide better
        analysis tools.
        """
        self.coef = coef
        self.intercept = intercept
        self.model = model
        self.variables = variables
    @classmethod
    def fit(cls, x_var, y_var):
        """
        Fits least squares linear regression model using one feature.
        :param x_var: Explanatory Variable
        :param y_var: Response Variable
        :return: Fits linear_regression attributes to model
        """
        r_corr = stat_functions.correlation(x_var, y_var)
        cls.coef = float(r_corr * (np.std(y_var, ddof=1) / np.std(x_var, ddof=1)))
        cls.intercept = float(np.mean(y_var) - (cls.coef * np.mean(x_var)))
        cls.model = f"y_hat = {cls.intercept:.2f} + {cls.coef:.2f}x"
        predict = [
            cls.intercept + cls.coef*exp for exp in x_var
        ]
        resid = [act - pred for act in y_var for pred in predict]

        cls.variables = {"explanatory":x_var, "response":y_var, "resid": resid}
        return cls

    @classmethod
    def visualize(cls):
        """Generates a scatterplot with the linear regression line."""
        if cls.coef == None:
            "Please fit linear_regression model, then try again."
        else:
            import matplotlib.pyplot as plt

            plt.scatter(cls.variables['explanatory'], cls.variables['response'], alpha=0.5)
            plt.axline((0, cls.intercept), slope=cls.coef, color='green', linestyle="--")
            plt.title(f"Linear Regression Model \n{cls.model}")
            plt.axis("equal")
            plt.grid()
            plt.show()


if __name__ == '__main__':
    from sklearn.linear_model import LinearRegression

    x, y = np.random.default_rng().multivariate_normal(
        [10, 20],
        [[5.96202397, -2.85602287], [-2.85602287, 3.47613949]],
        500).T

    # -- Code to test if my linear regression algorithm is correct using SciKit Learn's LinearRegression Object class.
    mylinreg = linear_regression().fit(x, y)

    x = np.reshape(x, (-1, 1))
    sklinreg = LinearRegression().fit(x, y)
    print(f"My regression model:            {mylinreg.model}")
    print(f"Sklearn's regression model:     y_hat = {sklinreg.intercept_:.2f} + {sklinreg.coef_[0]:.2f}x")
    mylinreg.visualize()
