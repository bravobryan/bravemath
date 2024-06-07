import numpy as np


# #### Base Functions #####
# #-- z-score --##
def z_score(array, sample=True):
    """ Returns z-score values into a Numpy Array """
    mean = np.mean(array)
    if sample:
        n = 1
    else:
        n = 0
    std = np.std(array, ddof=n)
    return np.array([(val - mean) / std  for val in array])


# #-- correlation coefficient --##
def correlation(x_val, y_val, kind="sample"):
    """ Returns the Sample Correlation Coefficient """
    # Sample Correlation Coefficient
    if kind == "sample":
        zscore_mult = z_score(x_val) * z_score(y_val)
        numerator = np.sum(zscore_mult)
        denominator = len(zscore_mult) - 1
        return numerator/denominator


if __name__ == '__main__':
    x = [1, 2, 2, 3]
    y = [1, 2, 3, 6]
    print(f"The correlation coefficient is: {correlation(x, y):.3f}")

