"""
Module for curve fitting.

Mandal, Anik | 2023-10-03
"""

import numpy as np
from sklearn.linear_model import Lasso
from sklearn.preprocessing import PolynomialFeatures


# Linear Fit Module:
def LinearFit(x_data, y_Data):
    '''
    Returns slope and y-intersect of the best linear fit using least
    square fit

    -----Inputs----------
    x_data : list : x coordinate of the input values
    y_data : list : y coordinate of the input values
    -----Outputs----------
    m : float : slope of the best fit line
    c : float : y-intersect of the best fit line.
    '''
    (sx, sy, p1, p2) = (0, 0, 0, 0)
    for i in range(len(x_data)):
        sx = sx + x_data[i]
        sy = sy + y_Data[i]
    xb = sx/len(x_data)
    yb = sy/len(y_Data)
    for i in range(len(x_data)):
        p1 = p1 + (x_data[i]-xb)*(y_Data[i]-yb)
        p2 = p2 + (x_data[i]-xb)**2
    m = p1/p2
    c = yb - m*xb
    return m, c


# Nolinear Fit Module:
def LassoRegression(x_data, y_data, max_degrees=10, alpha_value=0.2, num_points=int(1e5)):
    '''
    Returns data set of best fit curve using sklearn Lasso Regression

    -----Inputs----------
    x_data : list : x coordinates of the input values
    y_data : list : y coordinates of the input values
    max_degree : int : maximum degree for interpolation
        - default : 10
    alpha_value : float : defines alpha parameter for Lasso regression
        - default : 0.2
    num_points : int : number of point for interpolation
        - default : 1e5 
    -----Outputs----------
    x_new : list : x coordinates of the fitted curve
    y_new : list : y coordinates of the fitted curve
    '''  
    d = max_degrees
    poly = PolynomialFeatures(degree=d, include_bias=False)
    x_new = poly.fit_transform(x_data)

    alp = alpha_value
    sl = Lasso(alpha=alp).fit(x_new, y_data)

    m = sl.coef_
    c = sl.intercept_
    s = sl.score(x_new, y_data)

    x_new = np.linspace(min(x_data), max(x_data), num_points)
    y_new = []
    for i in range(len(x_new)):
        a = 0
        for j in range(len(m)):
            a = a + m[j] * x_new[i] ** (j + 1)
        y_new.append(a + c[0])
    return x_new, y_new
