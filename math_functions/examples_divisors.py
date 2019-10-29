"""
examples_divisors.py
Find all the common divisors between two integers. """
from typing import Tuple

def find_divisors(number1: int, number2: int) -> Tuple[int, int]:
    """ Find the common divisors of number1 and number2
        Assumes that number1 and number2 are positive ints
        Returns a tuple containing all common divisors. """
    assert number1 >= 1 and number2 >= 1

    divisors = ()   # Initialize the empty tuple

    for num in range(1, min(number1, number2) + 1):
        # print("num = ", num)
        if number1 % num == 0 and number2 % num == 0:
            # print("found divisor = ", num)
            divisors = divisors + (num,)
    return divisors


def test_divisors():
    """ Test harness for divisor"""
    divisors = find_divisors(20, 100)
    print("Answer is:\t\t", divisors)
    print("Answer should be:\t (1, 2, 4, 5, 10, 20)")

    total = 0
    for digit in divisors:
        total += digit
    print("Sum of divisors:", total, "\t=> Answer = 42")


def find_extreme_divisors(number1: int, number2: int) -> tuple():
    """ Find the smallest and largest common divisors of number1 and number2.
        Assumes that number1 and number2 are positive ints. """
    assert number1 >= 1 and number2 >= 1

    min_val, max_val = None, None

    for index in range(2, min(number1, number2) + 1):
        # print("index =", index)
        if number1 % index == 0 and number2 % index == 0:
            if min_val is None or index < min_val:
                min_val = index
            if max_val is None or index > max_val:
                max_val = index

    return (min_val, max_val)


def main():
    """ Main code """
    test_divisors()
    min_div, max_div = find_extreme_divisors(100, 200)
    print(f"Min Divisor = {min_div}\t\t=> Answer = 2")
    print(f"Max Divisor = {max_div}\t=> Answer = 100")

if __name__ == '__main__':
    main()
