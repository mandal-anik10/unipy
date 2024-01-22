"""
Module for basic mathematical operations and physical quantities.

Mandal, Anik | 2023-10-03
"""


from numpy import *

# Mathematical Operations----------

# Summation:
def Sum(arr, step = 1):
    '''
    Returns sum of the elements in a input list

    -----Inputs----------
    arr : list : list of integers/float
    step : int : increment in the index value
    -----Output----------
    s : int/float : sum of the elements of list

    * Equivalant to numpy.sum()
    '''
    s = 0
    for i in range(0, len(arr), step):
        s = s + arr[i]
    return s


# Factorial:
def Fact(n, step=1):
    '''
    Returns factorial of a number 

    -----Inputs----------
    n : int : Input number
    step : int : difference between two successive numbers
    -----Output----------
    f : int : factorial of the number
    '''
    f = 1
    for i in range(1, n+1, step):
        f = f * i
    return f
    
# Integration:
def Integrate(y_data, x_data, spacing='linear'):
    '''
    Function for performing integration using trapizoidal method.

    -----Inputs----------
    y_data : list : a list of numbers defing the y values of the function
    x_data : list : a list of numbers defing the x values of the function
    spacing : string : specification of increment vector/scaler
        - default :'linear'
    -----Output----------
    s : float : value of the integration
    '''
    if len(y_data) != len(x_data) or len(x_data) <= 1 or len(y_data) <= 1:
        raise ValueError("x and y data are not consistant for trapizoidal integration")
    else:
        if spacing == 'linear':
            h = x_data[1] - x_data[0]
            s = Sum(y_data[1:len(x_data)-1])
            s = (y_data[0] + y_data[-1] + 2 * s) * h / 2
        else:
            s = 0
            for i in range(len(x_data)-1):
                h = x_data[i+1] - x_data[i]
                s = s + h * (y_data[i] + y_data[i+1]) / 2
    return s
    
def Integrate_simp(y_data, x_data, spacing='linear'):
    '''
    Function for performing integration using Simpson's 1/3 method.

    -----Inputs----------
    y_data : list : a list of numbers defing the y values of the function
    x_data : list : a list of numbers defing the x values of the function
    spacing : string : specification of increment vector/scaler
        - default :'linear'
    -----Output----------
    s : float : value of the integration
    '''
    if len(y_data) != len(y_data) or len(x_data) <= 2 or len(y_data) <= 2:
        raise ValueError("x and y data are not consistant for simpson integration")
    else:
        if spacing == 'linear':
            h = x_data[1] - x_data[0]
            s = 4 * Sum(y_data[1, len(x_data)-1], 2)
            s = s + 2 * Sum(y_data[2, len(x_data)-1], 2)
            s = (y_data[0] + s + y_data[-1]) * h / 3
        else: 
            raise NotImplementedError('Simpson\'s 1/3 integration is not implemented yet'+\
                                      'in nonlinear scale; use tapizoidal integration.')
    
# Fourier Series:
def FourierSeries(y_data, x_data, nc=10):
    '''
    Returns Fouries Series of a function

    -----Inputs----------
    y_data : list : a list of numbers defing the y values of the function
    x_data : list : a list of numbers defing the x values of the function
    nc : int : number of coefficents of sin and cos series
        - default :10
    -----Outputs----------
    cc : list : coeff. of cosine series
    cs : list : coeff. of sin series
    y_new : list : fourier function
    '''
    cc, cs, y_new = [], [], []
    
    l = x_data[-1]-x_data[1]

    for i in range(nc):
        yc = y_data * cos(2 * pi * i * x_data / l)
        ys = y_data * sin(2 * pi * i * x_data / l)

        sc = (2/l) * Integrate(yc, x_data)
        ss = (2/l) * Integrate(ys, x_data)

        cc.append(sc)
        cs.append(ss)

    cc[0] = cc[0]/2

    for i in range(len(x_data)):
        s = 0
        for j in range(nc):
            s = s + cc[j] * cos(2 * pi * j * x_data[i] / l) + cs[j] * sin(2 * pi * j * x_data[i] / l)

        y_new.append(s)
    return cc, cs, y_new     

                                
# Physical Quantities----------

# Inertia Tensor:
def Inertia_T(Mass_List, Pos_Tensor):
    '''
    Returns Inertia Tensor of discrete masses

    -----Inputs----------
    arr : list : list of integers/float
    -----Output----------
    s : int/float : sum of the elements of list
    '''
    I = np.zeros((3, 3))

    for m in range(3):
        for n in range(3):
            
            if m == n:
                for k in range(len(Mass_List)):
                    s = 0
                    for i in range(3):
                        if i != m:
                            s = s + Mass_List[k]*Pos_Tensor[k][i]**2
                            
                    I[m][n] = I[m][n] + s
                    
            else:
                for k in range(len(Mass_List)):
                    s = - Mass_List[k]*Pos_Tensor[k][m]*Pos_Tensor[k][n]
                        
                    I[m][n] = I[m][n] + s
    return I


