"""
Module for vector operations.

Mandal, Anik | 2023-10-03
"""

import numpy as np
from unipy.MatOp import *


# Vector Dimension:
def V_Dim(v1):
    '''
    Returns the dimension of the vector

    -----Inputs----------
    v1 : array-like : input vector
    -----Output----------
    D : int : dimension of the input vector
    '''
    D = M_Order(v1)[0]
    return D

# Vector Sum:
def V_Sum(v1, v2):
    '''
    Returns sum of two vectors

    -----Inputs----------
    v1 : array-like : first vector
    v2 : array-like : second vector
    -----Output----------
    vs : array-like : sum of the two vectors
    '''
    if V_Dim(v1) == V_Dim(v2):
        vs = M_Sum(v1, v2)
        return vs
    else:
        raise ValueError('Dimension of the vectors doesn\'t match')


# Vector Negative:
def V_Neg(v1):
    '''
    Returns neg vector of a vector

    -----Inputs----------
    v1 : array-like : input vector
    -----Output----------
    vn : array-like : neg vector of the input vector
    '''

    vn = np.zeros((V_Dim(v1), 1))
    for i in range(V_Dim(v1)):
        vn[i][0] = -v1[i][0]
    return vn


# Vector Substraction:
def V_Subtract(v1, v2):
    '''
    Returns subtraction of two vectors

    -----Inputs----------
    v1 : array-like : first vector
    v2 : array-like : second vector
    -----Output----------
    vs : array-like : subtraction of the two vectors
    '''
    vn = V_Sum(v1, V_Neg(v2))
    return vn


# Vector Dot Product:
def V_Dot(v1, v2):
    '''
    Returns scaler product of two vectors

    -----Inputs----------
    v1 : array-like : first vector
    v2 : array-like : second vector
    -----Output----------
    vs : array-like : scaler product of the two vectors
    '''
    if V_Dim(v1) == V_Dim(v2):
        vs = 0
        for i in range(V_Dim(v1)):
            vs = vs + v1[i][0] * v2[i][0]
        return vs
    else:
        raise ValueError('Dimension of the vectors doesn\'t match')


# Vector Scaler Product:
def V_Scale(v1, f):
    '''
    Returns scaled vector of a vector

    -----Inputs----------
    v1 : array-like : input vector
    f: floar : scaling factor
    -----Output----------
    vs : array-like : scaled vector of the input vector
    '''
    vs = np.zeros((V_Dim(v1), 1))
    for i in range(V_Dim(v1)):
        vs[i][0] = vs[i][0] + f * v1[i][0]
    return vs


# Vector Mod:
def V_Mod(v1):
    '''
    Returns length/modulus of a vector

    -----Inputs----------
    v1 : array-like : input vector
    -----Output----------
    vm : float : length of the vector
    '''
    vm = (V_Dot(v1, v1))**0.5
    return vm


# Unit Vector:
def V_Unit(v1):
    '''
    Returns unit vector of a vector

    -----Inputs----------
    v1 : array-like : input vector
    -----Output----------
    vu : array-like : unit vector of the input vector
    '''
    vm = V_Mod(v1)
    if vm > 0:
        vu = np.zeros((V_Dim(v1), 1))
        for i in range(v1):
            vu[i][0] = v1[i][0] / vm
        return vu
    else:
        raise ZeroDivisionError('Length of the vector found to be zero!')


# Vector Cross Product:
def V_Cross(v1, v2):
    '''
    Returns cross product  of two vectors

    -----Inputs----------
    v1 : array-like : first input vector
    v2 : array-like : second input vector
    -----Output----------
    vc : array-like : cross product of the input vectors
    '''
    if V_Dim(v1) == V_Dim(v2) == 3:
        vcx = v1[1][0] * v2[2][0] - v1[2][0] * v2[1][0]
        vcy = v1[2][0] * v2[0][0] - v1[0][0] * v2[2][0]
        vcz = v1[0][0] * v2[1][0] - v1[1][0] * v2[0][0]
        vc = [vcx, vcy, vcz]

        return vc
    else:
        raise ValueError('Dimension of the vectors are not compatible for cross product')




# Gram-Schimdt Orthogonalization:
def GSOrtho(list_v):
    '''
    Returns vectors which are normal with each other using
    Gram-Schimdt orthogonalization method

    -----Inputs----------
    list_v : list : list of vectors
    -----Output----------
    list_n : list : mutually normal vectors
    '''
    dim_vs = [V_Dim(v) for v in list_v]
    if len(set(dim_vs)) == 1 and len(list_v) == dim_vs[0]:

        list_n = np.zeros((len(list_v)))
        list_n[0] = list_v[0]

        for i in range(1, len(list_n)):
            s = list_v[i]
            for j in range(0, i):
                s = s - (V_Dot(list_n[j], list_v[i]) / V_Mod(list_v[i])) * V_Unit(list_n[j])
        
            list_n[i] = s

        return list_n
    else:
        raise ValueError('Set of given vector are not compatible for Gram-Schimdt orthogonalization')


