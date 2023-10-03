"""
Module for matrix operations.

Mandal, Anik | 2023-10-03
"""

import numpy as np

# Matrix Order:
def M_Order(arr_x):
    '''
    Returns order of the input matrix

    -----Inputs----------
    arr_x : array-like : input array
    -----Output----------
    o : list : order of the matrix
    '''       
    r = len(arr_x)
    c = len(arr_x[0])
    o = [r, c]
    return o


# Matrix Sum:
def M_Sum(arr_x, arr_y):
    '''
    Returns sum of two matrices

    -----Inputs----------
    arr_x : array-like : first input matrix
    arr_y : array-like : second input matrix
    -----Output----------
    arr_z : array-like : output matrix as the sum of input matrices
    '''  
    if M_Order(arr_x) == M_Order(arr_y):
        Order = M_Order(arr_x)
        arr_z = np.zeros(Order)
        for i in range(Order[0]):
            for j in range(Order[1]):
                arr_z[i][j] = arr_x[i][j] + arr_y[i][j]
        return arr_z
    else:
        raise ValueError('Order of the matrices doesn\'t match')


# Matrix Multiplication:
def M_Multiplication(arr_x, arr_y):
    '''
    Returns multiplication of two matrices

    -----Inputs----------
    arr_x : array-like : first input matrix
    arr_y : array-like : second input matrix
    -----Output----------
    arr_z : array-like : output matrix as the multiplication of input matrices
    '''  
    Ox = M_Order(arr_x)
    Oy = M_Order(arr_y)
    arr_z = np.zeros((Ox[0],Oy[1]))
    if Ox[1] == Oy[0]:
        for i in range(0,Ox[0]):
            for j in range(0,Oy[1]):
                for k in range(0,Ox[1]):
                    arr_z[i][j] = arr_z[i][j] + arr_x[i][k] * arr_y[k][j]
        return arr_z
    else:
        raise ValueError('order of the matrices are incompatable for matrix multiplication'+\
                         'number of column of the fist matrix must be equal to the number of row of second matrix')
    


