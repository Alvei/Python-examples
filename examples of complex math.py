# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 20:07:42 2014

@author: Hugo Sarrazin
"""

import cmath # complex math library
def dftk(x, k=0, all=False):
    '''Function that ...
    Input: x is a list and k is an int 
    Output: float Xk'''
    if all:
        return [dftk(x, k) for k in range(len(x))]
    c = -1j * 2 * cmath.pi * k / len(x)
    Xk = 0
    
    for n, xn in enumerate(x):
        Xk += xn * cmath.exp(c * n)
    return Xk
X3 = dftk([1, 2, 0.1, -1.1, 5], 3, all=True)

def square(x):
    ''' Specialized function called by the operate function.
    Input: float
    '''
    return x ** 2
def cube(x):
    ''' Specialized function called by the operate function.
    Input: float
    '''
    return x ** 3

def operate(f, y):
    '''Input: f is a function and y is a float/int
    '''
    return f(y)
print operate(square, 4) # prints '16'
print operate(cube, 4) # prints '64'

print operate(lambda(x): x ** 2, 4) # prints '16'
print operate(lambda(x): x ** 3, 4) # prints '64'
square_plus_cube = lambda(x): x ** 2 + x ** 3
print operate(square_plus_cube, 4) # prints '80'

id_dept_pairs = [(8283, 'Aero/Astro'),
                 (3456, 'CS'),
                (7888, 'Math')]

# Sort by id number
print sorted(id_dept_pairs, key=lambda pair: pair[0])
# [(3456, 'CS'), (7888, 'Math'),
# (8283, 'Aero/Astro')]
# Sort by department alphabetically
print sorted(id_dept_pairs, key=lambda pair: pair[1])
# [(8283, 'Aero/Astro'), (3456, 'CS'),
# (7888, 'Math')]
