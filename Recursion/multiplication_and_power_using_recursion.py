# Power of n using recursion
############################################


def rec_power(m, n):
    """ Calculates the power n of a number m using recursion
        Signature: (int, int) -> int"""

    # Check that the input are ok
    assert isinstance(n, int) and isinstance(m, int)

    if n == 0:  # Base case
        return 1
    return m * rec_power(m, n - 1)


def rec_mult(m, n):
    ''' Calculates multiplication of m * n of a number m using recursion
        Signature: (int, int) -> int'''

    assert type(n) == int and type(m) == int  # Check that the input are int
    assert n >= 0 and m >= 0    # Check that the input are positive

    if n == 0:  # Base case
        return 0
    return m + rec_mult(m, n - 1)
