""" add.py
    Function that accepts two list of lists of numbers
    and returns one list of list with each of the corresponding
    numbers in the the two given lists of list added together.
    Inspired by Python Morsels. """

from typing import List
def add(matrix1: list, matrix2: list):
    """ nXn matrix additions using lists. """
    assert isinstance(matrix1, list)
    assert isinstance(matrix2, list)

    # Both lists needs to be of the same size
    error_msg = "The two matrices are not of the same size"
    try:
        len(matrix1) == len(matrix2) # Number of rows
        try:
            len(matrix1[0]) == len(matrix2[0])  # Number of columns
        except (ValueError):
            print(error_msg)
    except (ValueError):
        print(error_msg)

    new_matrix = []
    for row, value_row in enumerate(matrix1):
        temp_list = []
        for col, _ in enumerate(value_row):
            temp_list.append(matrix1[row] [col] + matrix2[row] [col])
        new_matrix.append(temp_list)
    return new_matrix

if __name__ == "__main__":
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print( add(matrix1, matrix2) )
