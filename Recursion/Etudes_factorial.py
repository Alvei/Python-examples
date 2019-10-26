"""etudes_factorial.py
"""


def fact_i(num: int) -> int:
    """ Calculates the factorial with while loop. """
    assert num > 0 and isinstance(num, int)

    result = 1

    while num > 1:
        result = result * num
        num -= 1
    return result


def fact_r(num: int) -> int:
    """ Calculates the factorial using recursion. """
    assert num > 0 and isinstance(num, int)

    # base case
    if num == 1:
        return num
    return num * fact_r(num - 1)


def main():
    """ Main code """
    tests = [3, 4, 8]
    for test in tests:
        print(f"{test}! = {fact_i(test)}")


if __name__ == '__main__':
    main()
