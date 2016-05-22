# -*- coding: utf-8 -*-
"""
Created on Sat Dec 20 14:43:09 2014

@author: Hugo Sarrazin
"""

import pylab

def printPolynomial(coef, Xrange, incr = 1):
    ''' Function to print a polynomical function
    
        coef is a list of all the coefficient of the polynomica
        with coef[2] being a, coef[1] being b and coef[0] being c
        
        Xrange is the ploting range
        
        incre is an option variable that defines the x- increments'''
        
    x = range(Xrange[0],Xrange[1], incr)
    y = []
    a, b, c = coef[2], coef[1], coef[0]
    
    for xi in x:
        y.append(a*xi**2 + b*xi + c)
    
    pylab.plot(x,y)

printPolynomial([2,3,10],[-100,100])


import numpy.polynomial.polynomial as poly
# the coefficient of polynomial go from lowest to higest
#print poly.polyroots([6,5,1]) 

import numpy as np
import matplotlib.pyplot as plt
import os

#creates a array in np 
my_array = np.array([0,1,2,3])
my_array.dtype

str_array = my_array.astype(str)  # converts to string

dim2_array = np.array([[0,1,2,3],[0,1,2,3], [0,1,2,4]]) # 2D array

dim2_array.ndim   # How many dimension - this is 2D
dim2_array.shape  # How many rows and columns
dim2_array.size   # How many elements

np.mean(dim2_array)  # Mean across all the elements
np.mean(dim2_array, axis = 0)  # Mean of all the columns
np.mean(dim2_array, axis = 1)  # Mean of all the rows

#Slicing
dim2_array[0]   # First row
dim2_array[:2]  # First 2 rows
dim2_array[:2, :2]  # First 2 rows and First 2 columns
dim2_array[0, ::-1]   # Reverses the first row

#Saving into excel by using comma delimited
np.savetxt('lookatarray.csv', dim2_array, delimiter = ',')

#Gets data that is delimited by commas
dim2_array2 = np.genfromtxt('lookatarray.csv', delimiter = ',')

#Current working directory
cwd = os.getcwd()