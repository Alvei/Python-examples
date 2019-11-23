"""
Etudes_comprehension.py
Different examples of using comprehensions.
Created on Thu Apr 19 19:28:53 2018
For Python 3.5
"""
import math


def list_comprehension():
    """ Examples of list comprehensions. """
    # List comprehensions form new lists by manipulating old ones
    vals = [1, 2, 3, 5, 7, 9, 10]
    double_vals = [2 * v for v in vals]
    print("Vectors\nV1:\t\t", vals)
    print("V2=2*V1:", double_vals)

    # Only include doubles for values dibisible by 5
    double_vals5 = [2 * v for v in vals if v % 5 == 0]
    print("V3=V2%5:", double_vals5)

    x_pts = [-1, 0, 2]
    y_pts = [2, 4]
    xy_pts = [[x, y] for x in x_pts for y in y_pts]
    # [[-1, 2], [-1, 4], [0, 2], [0, 4], [2, 2], [2, 4]]
    print("\nVectors:\nX:", x_pts, "Y:", y_pts)
    print("X.Y:", xy_pts)


def parsing_vector(vec):
    """ Parsing a vector
        Signature (str) -> list of floats"""

    # Strip away the brackets
    vec = vec.lstrip('[')
    vec = vec.rstrip(']')

    # Form a list by splitting on comma
    nums = vec.split(',')

    # Go from string to floating point
    nums = [float(n) for n in nums]
    return nums


def main():
    """ Main code """

     # Build a list using range() and list to expand the iterator or using list comprehension
    number_list = list(range(1, 6))
    number_list2 = [number for number in range(1, 6)]
    print(number_list)
    print(number_list2, "\n")

    # Now the power of list comprehension shines. Apply an IF condition
    even_list = [number for number in range(1, 6) if number % 2 == 0]
    print("Only even numbers:", even_list)

    # Tuple comprehension
    cell = [(row, col) for row in range(1, 3) for col in range(5, 8)]
    print("tuple:", cell)

    # Use tuple unpacking. This prints a tuple per line
    for row, col in cell:
        print(row, col)

    # Dictionnary comprehension
    word = 'letters'
    letter_counts = {letter: word.count(letter) for letter in word}
    print("Dictionary:", letter_counts)

    list_comprehension()

    print("\nParsed vector string:", parsing_vector('[12.4, 3, 4, 7.22]'))

    # Parsing a vector using comprehension instead of a function using
    vec = '[12.4, 3, 4, 7.22]'
    nums = [float(n) for n in vec.strip('[]').split(',')]
    print("\nParsed vector string:", nums)


if __name__ == '__main__':
    main()
