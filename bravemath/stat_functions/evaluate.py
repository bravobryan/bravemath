import numpy as np

def rmse(y_actual, y_pred, mse=False):
    """
    Returns Mean Squared Error on input data for testing regression models.
    :param y_actual: Array or list of actual response variables.
    :param y_pred: Array or list of predicted response variables.
    :return: MSE score value. If `squared = True` then RMSE is returned.
    """
    se = np.square(np.array(y_actual, np.float32) - np.array(y_pred, np.float32))
    mse = (np.sum(se) / (len(se) - 2))
    if mse:
        score = mse
    else:
        score = np.sqrt(mse)
    return score


if __name__ == '__main__':
    x = [1, 2, 2, 3]
    y = [1, 2, 3, 6]
    y_pred = [0.5, 3, 3, 5.5]

    print(rmse(y, y_pred))