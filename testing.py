import numpy as np
import matplotlib.pyplot as plt

# takes input data x and y and estimates coefficents of linear regression line
# take in data of x and y and estimates slope and y-intercept
def estimate_coef(x,y):
    # number of points
    n = np.size(x)
    
    # avgs of x and y values
    m_x = np.mean(x)
    m_y = np.mean(y)
    
    # calculating cross deviation and deciation about x
    # how x and y change together
    SS_xy = np.sum(y*x) - n*m_y*m_x
    # how x values spread out from avg
    SS_xx = np.sum(x*x) - n*m_x*m_x
    
    # calculating regression coefficients
    # calc slope
    b_1 = SS_xy /SS_xx
    # calc y-intercept
    b_0 = m_y - b_1*m_x
    
    return (b_0, b_1)