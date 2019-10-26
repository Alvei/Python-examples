""" Using recursion to do interger multiplications and power."""


def rec_power(num: int, exp: int) -> int:
    """ Calculates the power exp of a number num using recursion."""
    assert isinstance(exp, int) and isinstance(num, int)

    if exp == 0:  # Base case
        return 1
    return num * rec_power(num, exp - 1)


def rec_mult(num: int, num2: int) -> int:
    ''' Calculates multiplication of m * n of a number m using recursion.'''
    assert isinstance(num2, int) and isinstance(num, int)  # Check that the input are int
    assert num2 >= 0 and num >= 0    # Check that the input are positive

    if num2 == 0:  # Base case
        return 0
    return num + rec_mult(num, num2 - 1)


def main():
    """ Main code """
    print("3 * 4  = ", rec_mult(3, 4))
    print("2 ** 3 = ", rec_power(2, 3))


if __name__ == '__main__':
    main()
