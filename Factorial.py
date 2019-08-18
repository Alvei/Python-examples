def fact_i(num):
    """ Calculates the factorial.
    Signature (int) -> int
    Assumes that num is an int > 0
    for Python 3.5 """

    result = 1

    while num > 1:
        result = result * num
        num -= 1
    return result


def fact_r(num):
    """ Calculates the factorial using recursion.
    Signature (int) -> int
    Assumes that num is an int > 0"""

    # base case
    if num == 1:
        return num
    return num * fact_r(num - 1)
