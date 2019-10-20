""" Using recursion to do interger multiplications and power."""


def rec_power(m: int, n: int) -> int:
    """ Calculates the power n of a number m using recursion."""

    # Check that the input are ok
    assert isinstance(n, int) and isinstance(m, int)

    if n == 0:  # Base case
        return 1
    return m * rec_power(m, n - 1)


def rec_mult(m: int, n: int) -> int:
    ''' Calculates multiplication of m * n of a number m using recursion.'''

    assert type(n) == int and type(m) == int  # Check that the input are int
    assert n >= 0 and m >= 0    # Check that the input are positive

    if n == 0:  # Base case
        return 0
    return m + rec_mult(m, n - 1)


def main():
    """ Main code """

    print("3 * 4  = ", rec_mult(3, 4))
    print("2 ** 3 = ", rec_power(2, 3))


if __name__ == '__main__':
    main()
