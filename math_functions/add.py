""" add.py
    Function that accepts two list of lists of numbers
    and returns one list of list with each of the corresponding
    numbers in the the two given lists of list added together.
    Inspired by Python Morsels. """

# from typing import List


def add(*matrices: list):
    """ nXn matrix additions using lists. """

    # Test to make sure that all matrix have the same dimensions.
    # Loop over the matrices with set comprehension to keep only different shapes in a tuple.
    # The tuple function converts the size of each row which would have been a list into a tuple.
    # The inner list comprehension loops over the row of the given matrix and calculates its length.
    no_matrix_shapes = {tuple(len(row) for row in matrix) for matrix in matrices}
    # matrix_shape is a set, if we have more than 1, all matrices are not of the same size.
    if len(no_matrix_shapes) > 1:
        raise ValueError("Matrices are not of the same shape.")

    # zip iterates over 2 lists and returns a tuple with the corresponding elements
    # Takes the same rows of each matrices ancd create a list of lists.
    # E.g., [row1_A, row1_B, row1_C] then [row2_A, row2_B, row2_C]
    # Then take the same element of each sub-list and sums them.
    return [[sum(values) for values in zip(*rows)] for rows in zip(*matrices)]


def add_m_matrices_1_comprehension(*matrices: list):
    """ nXn m matrices additions using lists. """

    # zip iterates over two lists and returns a tuple with the corresponding elements
    new_matrix: list = []
    # Takes the same rows of each matrices ancd create a list of lists.
    # E.g., [row1_A, row1_B, row1_C] then [row2_A, row2_B, row2_C]
    for rows in zip(*matrices):
        row: list = []
        # Take the same element of each sub-list
        # now that we have the same elment from each matrix in a list, sum them
        row = [sum(values) for values in zip(*rows)]
        new_matrix.append(row)
    return new_matrix


def add_m_matrices(*matrices: list):
    """ nXn matrix additions using lists. """

    new_matrix: list = []
    # zip iterates over two lists and returns a tuple with the corresponding elements
    # Takes the same rows of each matrices ancd create a list of lists.
    # E.g., [row1_A, row1_B, row1_C] then [row2_A, row2_B, row2_C]
    for rows in zip(*matrices):
        row: list = []
        # Take the same element of each sub-list
        for values in zip(*rows):
            # now that we have the same elment from each matrix in a list, sum them
            row.append(sum(values))
        new_matrix.append(row)
    return new_matrix


def add_2_matrices(matrix1: list, matrix2: list):
    """ nXn matrix additions using lists. Using for loop and 2 list comprehension"""
    assert isinstance(matrix1, list)
    assert isinstance(matrix2, list)

    assert len(matrix1) > 1
    assert len(matrix2) > 1

    # Create two list comprehensions and compare them
    if [len(row) for row in matrix1] != [len(row) for row in matrix2]:
        raise ValueError("Given matrices are not of the same size")

    # zip iterates over two lists and returns a tuple with the corresponding elements
    # Create two list comprehension.
    return [
        [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]


def add_list_comprehension(matrix1: list, matrix2: list):
    """ nXn matrix additions using lists. Using for loop and 1 list comprehension"""

    new_matrix: list = []
    # zip iterates over two lists and returns a tuple with the corresponding elements
    for row1, row2 in zip(matrix1, matrix2):
        new_matrix.append([elem1 + elem2 for elem1, elem2 in zip(row1, row2)])
    return new_matrix


def add_zip(matrix1: list, matrix2: list):
    """ nXn matrix additions using lists. Using for loop and zip. """

    new_matrix: list = []
    # zip iterates over two lists and returns a tuple with the corresponding elements
    for row1, row2 in zip(matrix1, matrix2):
        row: list = []
        for elem1, elem2 in zip(row1, row2):
            row.append(elem1 + elem2)
        new_matrix.append(row)
    return new_matrix


def add_loop(matrix1: list, matrix2: list):
    """ nXn matrix additions using lists. Using for loop and very clumsy """

    new_matrix: list = []
    for row, value_row in enumerate(matrix1):
        temp_list: list = []
        for col, _ in enumerate(value_row):
            temp_list.append(matrix1[row][col] + matrix2[row][col])
        new_matrix.append(temp_list)
    return new_matrix


if __name__ == "__main__":
    mat1 = [[1, -2], [-3, 4]]
    mat2 = [[2, -1], [0, -1]]
    mat3 = [[3, 0], [1, -2]]
    print(add(mat1, mat2, mat3))
    # print(add([[1, 2], [3, 4]], [[1, 3, 4], [1, 2, 3]]))
