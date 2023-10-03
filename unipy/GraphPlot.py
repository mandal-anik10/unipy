"""
Module for graph plotting.

Mandal, Anik | 2023-10-03
"""

def ExpData2GraphData(x_data, y_data, small_x, small_y):
    '''
    Returns sum of the elements in a input list

    -----Inputs----------
    arr : list : list of integers/float
    step : int : increment in the index value
    -----Output----------
    s : int/float : sum of the elements of list
    '''
    x_new = []
    y_new = []
    for i in range(len(x_data)):
        x_new.append(x_data[i]/small_x)
        y_new.append(y_data[i]/small_y)
    return x_new, y_new
