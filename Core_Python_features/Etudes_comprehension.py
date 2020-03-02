"""
Etudes_comprehension.py
Different examples of using comprehensions.
For Python 3.5
"""
from typing import List

def list_comprehension():
    """ Examples of list comprehensions. """
    # List comprehensions form new lists by manipulating old ones
    vals: list = [1, 2, 3, 5, 7, 9, 10]
    double_vals: list = [2 * v
                        for v in vals]
    print("Vectors\nV1:\t\t", vals)
    print("V2= 2*V1:", double_vals)

    # Only include doubles for values dibisible by 5
    double_vals5: list = [2 * v
                          for v in vals
                              if v % 5 == 0]
    print("V3= V2%5:", double_vals5)

    x_pts: list = [-1, 0, 2]
    y_pts: list = [2, 4]
    xy_pts: list = [[x, y]
                    for x in x_pts
                        for y in y_pts]
    # [[-1, 2], [-1, 4], [0, 2], [0, 4], [2, 2], [2, 4]]
    print("\nVectors:\nX:", x_pts, "Y:", y_pts)
    print("X.Y:", xy_pts)

def parsing_vector(vec: str) -> List[float]:
    """ Parsing a vector. No error checking"""
    assert vec[0] == '['

    # Strip away the brackets
    vec = vec.lstrip('[]')
    vec = vec.rstrip(']')

    # Form a list by splitting on comma
    vec = vec.split(',')

    # Go from string to floating point
    nums: List[float] = [float(n)
                         for n in vec]
    return nums


def main():
    """ Main code """

    # Now the power of list comprehension shines. Apply an IF condition
    even_list: list = [number
                      for number in range(1, 6)
                        if number % 2 == 0]
    print("Only even numbers:", even_list)

    # Tuple comprehension
    cell = [(row, col)
            for row in range(1, 3)
                for col in range(5, 8)]
    print("tuple:", cell)

    # Use tuple unpacking. This prints a tuple per line
    #for row, col in cell:
    #    print(row, col)

    # Dictionnary comprehension
    word: str = 'letters'
    letter_counts: dict = {letter: word.count(letter)
                            for letter in word}
    print("Dictionary:", letter_counts)

    #list_comprehension()

    # Parsing a vector using comprehension instead of a function using
    vec: str = '[12.4, 3, 4, 7.22]'
    nums = [float(n)
            for n in vec.strip('[]').split(',')]
    print(f"\nParsed vector string: {nums}")
    print("Parsed vector string:", parsing_vector('[12.4, 3, 4, 7.22]'))


if __name__ == '__main__':
    main()
