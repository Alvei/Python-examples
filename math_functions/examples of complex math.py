"""
Created on Wed Dec 24 20:07:42 2014

Example of doing complex math
"""

import cmath  # complex math library


def dftk(x, k=0, all=False):
    ''' Function that applies k to all the elements of the list
        Signature: (list, int) -> float'''
    if all:
        return [dftk(x, k) for k in range(len(x))]
    c = -1j * 2 * cmath.pi * k / len(x)
    Xk = 0

    for n, xn in enumerate(x):
        Xk += xn * cmath.exp(c * n)
    return Xk


def square(x):
    ''' Specialized function called by the operate function.
        Signature: (float) -> float.'''
    return x ** 2


def cube(x):
    ''' Specialized function called by the operate function.
        Signature: (float) -> float.'''
    return x ** 3


def operate(f, y):
    '''Signature: (function, float/int) -> float.'''
    return f(y)


def square_plus_cube(x):
    return x ** 2 + x ** 3


X = [1, 2, 0.1, -1.1, 5]
X3 = dftk(X, 3, all=True)
print("X:\n", X)
print("X to the power of 3:\n", X3)

print(operate(square, 4))  # prints '16'
print(operate(cube, 4))  # prints '64'

# print(operate(lambda(x): x ** 2, 4))  # prints '16'
# print(operate(lambda(x): x ** 3, 4))  # prints '64'


print(operate(square_plus_cube, 4))  # prints '80'

id_dept_pairs = [(8283, 'Aero/Astro'),
                 (3456, 'CS'),
                 (7888, 'Math')]

# Sort by id number
print(sorted(id_dept_pairs, key=lambda pair: pair[0]))
# [(3456, 'CS'), (7888, 'Math'),
# (8283, 'Aero/Astro')]
# Sort by department alphabetically
print(sorted(id_dept_pairs, key=lambda pair: pair[1]))
# [(8283, 'Aero/Astro'), (3456, 'CS'),
# (7888, 'Math')]
