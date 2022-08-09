# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:24:37 2022

@author: Juanvi
"""

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the functions; for getting the slope and the y-intercept, and for plotting the graph
def getting_coefficients(X,Y):
    
    # Slope and Y-Intercept
    mean_x, mean_y = np.mean(X), np.mean(Y)
    
    n = len(X)
    
    num, denom = 0, 0
    for i in range (n):
        num += (X[i] - mean_x) * (Y[i]-mean_y)
        denom += (X[i] - mean_x)**2
    
    slope = num/denom
    y_intercept = mean_y - (slope * mean_x)
    
    max_x = np.max(X)
    min_x = np.min(X)
    
    x = np.linspace(min_x, max_x, 1000)
    y = y_intercept + slope*x
    
    print('The Slope is: ', round(slope,4), "\nThe Y-Intercept is",round(y_intercept,4))
    return x, y

def plotting (x, y):
    plt.xlabel('Grades in first period')
    plt.ylabel('Final grades')
    plt.plot(x, y, color='red', label= 'Regression Line')
    plt.scatter(X, Y, color='green', label= 'Scatter Plot')
    plt.legend()
    plt.show()


# We run the program
if __name__ == '__main__':
    
    # Get data
    matrix = pd.read_csv ("student-mat.csv", sep=";")
    
    # Least squares from grades of students first period and final grades
    values = matrix [['G1','G3']]
    
    X = values['G1']
    Y = values['G3']
    x, y = getting_coefficients(X, Y)
    plotting(x,y)



