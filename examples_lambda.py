"""
examples_lambda.py
Examples of using lambda
Created on Wed Dec 24 20:07:42 2014
"""


def square(num):
    ''' Specialized function called by the operate function.
        Signature: (float) -> float. '''
    return num ** 2


def cube(num):
    ''' Specialized function called by the operate function.
        Signature: (float) -> float. '''
    return num ** 3


def operate(func, num):
    '''Flexible function.
       Signature: (function, float) -> what the function returns. '''
    return func(num)


def main():
    """ Main code """
    # Super short version using lambda
    def square_plus_cube(x): return x ** 2 + x ** 3

    print("4**2=:", operate(square, 4))  # prints '16'
    print("4**3=:", operate(cube, 4))   # prints '64'

    print("4**2=:", operate(lambda x: x ** 2, 4))  # prints '16'
    print("4**3=:", operate(lambda x: x ** 3, 4))  # prints '64'

    print("4**2+4**3=:", operate(square_plus_cube, 4))  # prints '80'

    # Sorting examples
    id_dept_pairs = [(8283, 'Aero/Astro'),
                     (3456, 'CS'),
                     (7888, 'Math')]

    print("list of tuples:", id_dept_pairs)

    # Sort by id number which is the 1st element of tuple pair
    print("sorted by 1 elem:", sorted(id_dept_pairs, key=lambda pair: pair[0]))
    # [(3456, 'CS'), (7888, 'Math'), (8283, 'Aero/Astro')]

    # Sort by department alphabetically which is the 2nd element of tuple pair
    print("sorted by 2 elem:", sorted(id_dept_pairs, key=lambda pair: pair[1]))
    # [(8283, 'Aero/Astro'), (3456, 'CS'), (7888, 'Math')]


if __name__ == '__main__':
    main()
