# Viết function thực hiện Mean Difference of nth Root Error

import numpy as np


def mean_difference_nth_root_error(y_true, y_pred, n, p):

    root_y = np.power(y_true, 1 / n)
    root_y_hat = np.power(y_pred, 1 / n)
    difference = (root_y - root_y_hat) ** p

    return difference


if __name__ == "__main__":

    y_true = 50
    y_pred = 49.5
    n = 2
    p = 1

    res = mean_difference_nth_root_error(y_true, y_pred, n, p)
    print(f"Mean difference nth roor error is: {res}")
