import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bravemath import stat_functions


class linear_regression:
    def __init__(
            self, coef=None, intercept=None, model="linear_regression not fit.", variables={}
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
            (cls.intercept + cls.coef * exp) for exp in x_var
        ]

        cls.variables = {"explanatory":x_var, "response":y_var, "predict": predict}
        return cls


    @classmethod
    def visualize(cls):
        """
        Generates a scatterplot with the linear regression line.
        """
        try:
            plt.scatter(cls.variables['explanatory'], cls.variables['response'], alpha=0.5)
            plt.axline((0, cls.intercept), slope=cls.coef, color='green', linestyle="--")
            plt.title(f"Linear Regression Model \n{cls.model}")
            plt.axis("equal")
            plt.grid()
            return plt.show()

        except AttributeError:
            print("*****Please fit linear_regression model, then Try again!*****")

    @classmethod
    def resid(cls, dataframe=False, squared=False):
        """
        Generates a residual plot of the fitted model
        :param dataframe: Bool
            If `True` then the method returns a DataFrame with the explanatory variables (actuals),
                predictions (using the actuals) and the residuals of the variables.
        :param squared: Bool
            If `True` the method will return a Residual Squared Plot.
        :return:
        """
        try:
            if squared:
                df = pd.DataFrame({
                    "explanatory": cls.variables['explanatory'],
                    "predict": cls.variables['predict']
                })
                df['resid'] = df['explanatory'] - df['predict']
                df['resid_squared'] = np.square(df['resid'])
                sns.residplot(data=df, x='predict', y='resid_squared',
                              lowess=True, line_kws=dict(color='red'))
                plt.xlabel('Fitted Values')
                plt.title(f"Residuals Squared versus Fitted \nResiduals Sum of Squares (RSS): {np.sum(df['resid_squared']):.3f}")
                plt.show()
                if dataframe:
                    return df
                else:
                    pass

            else:
                df = pd.DataFrame({
                    "explanatory":cls.variables['explanatory'],
                    "predict":cls.variables['predict']
                })
                df['resid'] = df['explanatory'] - df['predict']
                sns.residplot(data=df, x='predict', y='resid',
                              lowess=True, line_kws=dict(color='red'))
                plt.xlabel('Fitted Values')
                plt.title(f"Residuals versus Fitted \nResiduals Sum: {np.sum(df['resid']):.3f}")
                plt.show()
                if dataframe:
                    return df
                else:
                    pass

        except AttributeError:
            print("*****Please fit linear_regression model, then Try again!*****")


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

    # Test `.viszualize()` method.
    mylinreg.visualize()
