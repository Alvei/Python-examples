# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 20:07:42 2014

Examples of using lambda

@author: Hugo Sarrazin
"""

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
# Super short version using lambda
square_plus_cube = lambda(x): x ** 2 + x ** 3

print operate(square, 4) # prints '16'
print operate(cube, 4) # prints '64'

print operate(lambda(x): x ** 2, 4) # prints '16'
print operate(lambda(x): x ** 3, 4) # prints '64'

print operate(square_plus_cube, 4) # prints '80'


# Sorting examples
id_dept_pairs = [(8283, 'Aero/Astro'),
                 (3456, 'CS'),
                (7888, 'Math')]

# Sort by id number which is the 1st element of tuple pair
print sorted(id_dept_pairs, key=lambda pair: pair[0])
# [(3456, 'CS'), (7888, 'Math'),
# (8283, 'Aero/Astro')]
# Sort by department alphabetically which is the 2nd element of tuple pair
print sorted(id_dept_pairs, key=lambda pair: pair[1])
# [(8283, 'Aero/Astro'), (3456, 'CS'),
# (7888, 'Math')]
