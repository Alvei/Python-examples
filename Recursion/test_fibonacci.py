from Fibonacci import fib1, fib2, fib3, fib4, fib5, fib6, fib7, fib8, matmult, matrix_power
import pytest

def test_fib1():
    """ Basic Fib recursion """
    assert fib1(0) == 0
    assert fib1(1) == 1
    assert fib1(2) == 1
    assert fib1(3) == 2
    assert fib1(6) == 8
    assert fib1(10) == 55

    with pytest.raises(TypeError):
        assert fib1('a')
    with pytest.raises(ValueError):
        assert fib1(-1)

def test_fib2():
    """ Basic Fib with loop """
    assert fib2(0) == 0
    assert fib2(1) == 1
    assert fib2(2) == 1
    assert fib2(3) == 2
    assert fib2(6) == 8
    assert fib2(10) == 55

    with pytest.raises(TypeError):
        assert fib2('a')
    with pytest.raises(ValueError):
        assert fib2(-1)

""" NOT SURE HOW TO TEST A FUNCTION THAT RETURNS A GENERATOR
def test_fib3():
    assert fib3(0) == 0
    assert fib3(1) == 1
    assert fib3(2) == 1
    assert fib3(3) == 2
    assert fib3(6) == 8
    assert fib3(10) == 55

    with pytest.raises(TypeError):
        assert fib2('a')
    with pytest.raises(ValueError):
        assert fib2(-1) """

def test_fib4():
    """ Uses dict to create memoization """
    assert fib4(0) == 0
    assert fib4(1) == 1
    assert fib4(2) == 1
    assert fib4(3) == 2
    assert fib4(6) == 8
    assert fib4(10) == 55

    with pytest.raises(TypeError):
        assert fib4('a')
    with pytest.raises(ValueError):
        assert fib4(-1)

def test_fib5():
    """ LRU Cache implementation of memoization. """
    assert fib5(0) == 0
    assert fib5(1) == 1
    assert fib5(2) == 1
    assert fib5(3) == 2
    assert fib5(6) == 8
    assert fib5(10) == 55

    with pytest.raises(TypeError):
        assert fib5('a')
    with pytest.raises(ValueError):
        assert fib5(-1)

def test_fib6():
    """ LRU Cache implementation with tuple. """
    actual = fib6(0)
    assert actual[0] == 0, f"Expected: 0, Actual: {actual[0]}"
    actual = fib6(1)
    assert actual[0] == 1, f"Expected: 1, Actual: {actual[0]}"
    actual = fib6(2)
    assert actual[0] == 1, f"Expected: 1, Actual: {actual[0]}"
    actual = fib6(3)
    assert actual[0] == 2, f"Expected: 2, Actual: {actual[0]}"
    actual = fib6(6)
    assert actual[0] == 8, f"Expected: 8, Actual: {actual[0]}"
    actual = fib6(10)
    assert actual[0] == 55, f"Expected: 55, Actual: {actual[0]}"

    with pytest.raises(TypeError):
        assert fib6('a')
    with pytest.raises(ValueError):
        assert fib6(-1)


def test_fib7():
    """ Manual implementation of memoization. """
    assert fib7(0) == 0
    assert fib7(1) == 1
    assert fib7(2) == 1
    assert fib7(3) == 2
    assert fib7(6) == 8
    assert fib7(10) == 55

    with pytest.raises(TypeError):
        assert fib7('a')
    with pytest.raises(ValueError):
        assert fib7(-1)

def test_fib8():
    """ Fib closed formed using linear algebra. """
    assert fib8(0) == 0
    assert fib8(1) == 1
    assert fib8(2) == 1
    assert fib8(3) == 2
    assert fib8(6) == 8
    assert fib8(10) == 55

    with pytest.raises(TypeError):
        assert fib8('a')
    with pytest.raises(ValueError):
        assert fib8(-1)

def test_matmult():
    """ 2X2 matrix multiplications using tuples.
        Did not test valid types. """
    A = ((1, 2), (2, 1))
    B = ((1, 1), (2, 1))
    assert matmult(A, B) == ((5, 3), (4, 3))
    A = ((1, 2), (2, 1))
    B = ((1, 0), (0, 1))
    assert matmult(A, B) == ((1, 2), (2, 1))
    A = ((1, 2), (2, 1))
    B = ((0, 0), (0, 0))
    assert matmult(A, B) == ((0, 0), (0, 0))
    A = ((1, 2), (2, 1))
    B = ((1, 1), (1, 1))
    assert matmult(A, B) == ((3, 3), (3, 3))

#def test_matrix_power():
    """ Apply power num to 2X2 matrix.
        Did not test valid types. """
    """A = ((1, 2), (3, 1))
    num = 0
    assert matrix_power(A, num) == ((1, 0), (0, 1))
    num = 1
    assert matrix_power(A, num) == ((1, 2), (3, 1))
    num = 2
    assert matrix_power(A, num) == ((1, 4), (9, 1))
    num = 3
    assert matrix_power(A, num) == ((1, 8), (27, 1))
    num = 7
    assert matrix_power(A, num) == ((1, 128), (2187, 1))
    num = 8
    assert matrix_power(A, num) == ((1, 256), (6561, 1))"""
