"""
Example of doing complex math. """

import cmath  # complex math library
from typing import Callable, List, Union


def dftk(x: List[float], k: int = 0, all = False) -> Union[float, List[float]]:
    ''' Function that applies k to all the elements of the list. '''
    if all:
        return [dftk(x, k) for k in range(len(x))]
    num_c = -1j * 2 * cmath.pi * k / len(x)

    Xk = 0
    for index, xn in enumerate(x):
        Xk += xn * cmath.exp(num_c * index)
    return Xk


def square(x: float) -> float:
    ''' Specialized function called by the operate function. '''
    return x ** 2


def cube(x: float) -> float:
    ''' Specialized function called by the operate function. '''
    return x ** 3


def operate(f: Callable, y: float) -> float:
    '''Apply a function on a single variable (not list). '''
    return f(y)


def square_plus_cube(x: float) -> float:
    return x ** 2 + x ** 3


def main():
    X = [1, 2, 0.1, -1.1, 5]
    X3 = dftk(X, 3, all=True)
    print("X:{X}\n")
    print("X to the power of 3:{X3}\n")

    num = 4
    print(f"Square => {num}^2: {operate(square, num)}")     # prints '16'
    print(f"Cube => {num}^3: {operate(cube, num)}")         # prints '64'

    # print(operate(lambda(x): x ** 2, 4))  # prints '16'
    # print(operate(lambda(x): x ** 3, 4))  # prints '64'

    print(f"Square + Cube => {num}^2 + {num}^3: {operate(square_plus_cube, num)}")  # prints '80'

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

if __name__ == "__main__":
    main()
