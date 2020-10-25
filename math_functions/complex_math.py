"""
Example of doing complex math using cmath library.
"""

import cmath
from typing import Callable, List, Union


def dftk(
    my_list: List[float], num: int = 0, all_elem=False
) -> Union[float, List[float]]:
    """ Function that applies k to all the elements of the list. """
    if all_elem:
        # return [dftk(my_list, num) for k in range(len(my_list))]
        return [dftk(my_list, num) for k in range(len(my_list))]

    num_c = -1j * 2 * cmath.pi * num / len(my_list)

    Xk = 0
    for index, xn in enumerate(my_list):
        Xk += xn * cmath.exp(num_c * index)
    return Xk


def square(num: float) -> float:
    """ Specialized function called by the operate function. """
    return num ** 2


def cube(num: float) -> float:
    """ Specialized function called by the operate function. """
    return num ** 3


def operate(func: Callable, num: float) -> float:
    """Apply a function on a single variable (not list). """
    return func(num)


def square_plus_cube(num: float) -> float:
    """ Specialized function called by the operate function. """
    return num ** 2 + num ** 3


def main():
    """ Test. Harness"""
    my_list = [1, 2, 0.1, -1.1, 5]
    my_list3 = dftk(my_list, 3, all_elem=True)
    print(f"X:{my_list}\n")
    print(f"X to the power of 3:\n{my_list3}\n")

    num = 4
    print(f"Square => {num}^2: {operate(square, num)}")  # prints '16'
    print(f"Cube   => {num}^3: {operate(cube, num)}")  # prints '64'

    # print(operate(lambda(x): x ** 2, 4))  # prints '16'
    # print(operate(lambda(x): x ** 3, 4))  # prints '64'

    print(
        f"Square + Cube => {num}^2 + {num}^3: {operate(square_plus_cube, num)}"
    )  # prints '80'

    id_dept_pairs = [(8283, "Aero/Astro"), (3456, "CS"), (7888, "Math")]

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
