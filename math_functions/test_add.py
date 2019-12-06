import pytest
from add import add


def test_good_values():
    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    actual = add(matrix1, matrix2)
    expected = [[3, -3], [-3, 3]]
    message = (f"add() returned {actual} instead of {expected}")
    assert  actual == expected, message

    matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
    matrix2 = [[1, 1, 0],  [1, -2, 3],  [-2, 2, -2]]
    actual = add(matrix1, matrix2)
    expected = [[2, -1, 3], [-3, 3, -3], [5, -6, 7]]
    message = (f"add() returned {actual} instead of {expected}")
    assert  actual == expected, message

"""def test_matrix_type():
    with pytest.raises(AssertionError):
        assert add('a', [[1, 3], [1, 2]])
        assert add([1, 3], None)

def test_unitary_matrix():
    with pytest.raises(AssertionError):
        assert add([1], [[1, 3], [1, 2]])
        assert add([[1, 3], [1, 2]], [10])"""

def test_same_size():
    with pytest.raises(ValueError):
        assert add([[1, 2], [3, 4]], [[1, 3, 4], [1, 2, 3]])