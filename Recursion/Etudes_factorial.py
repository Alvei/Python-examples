"""
etudes_factorial.py
"""


def fact_i(num):
    """ Calculates the factorial with while loop.
        Signature (int) -> int

        for Python 3.5 """

    assert num > 0 and isinstance(num, int)

    result = 1

    while num > 1:
        result = result * num
        num -= 1
    return result


def fact_r(num):
    """ Calculates the factorial using recursion.
    Signature (int) -> int"""

    assert num > 0 and isinstance(num, int)

    # base case
    if num == 1:
        return num
    return num * fact_r(num - 1)


def main():
    """ Main code """
    print("3! = ", fact_i(3))
    print("4! = ", fact_r(4))


if __name__ == '__main__':
    main()
