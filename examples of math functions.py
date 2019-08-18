"""
Find all the common divisors between two integers.

Created on Sat Jan 10 16:53:39 2015

Python 3.X
"""


def findDivisors(number1, number2):
    """ Find the common divisors of number1 and number2
        Assumes that number1 and number2 are positive ints
        Returns a tuple containing all common divisors
        Signature: (int, int) -> tuple."""

    assert number1 >= 1 and number2 >= 1

    divisors = ()   # Initialize the empty tuple

    for num in range(1, min(number1, number2) + 1):
        # print("num = ", num)
        if number1 % num == 0 and number2 % num == 0:
            # print("found divisor = ", num)
            divisors = divisors + (num,)
    return divisors


# Test harness for divisor
def testDivisors():
    divisors = findDivisors(20, 100)
    print("Answer is:\t\t\t", divisors)
    print("Answer should be:\t (1, 2, 4, 5, 10, 20)")

    total = 0
    for digit in divisors:
        total += digit
    print("Sum of divisors:\t", total)
    print("Answer should be:\t 42")


def findExtremeDivisors(number1, number2):
    """ Find the smallest and largest common divisors of number1 and number2.
        Assumes that number1 and number2 are positive ints.
        Signature (int, int) => (tuple)."""

    assert number1 >= 1 and number2 >= 1

    minVal, maxVal = None, None

    for i in range(2, min(number1, number2) + 1):
        # print("i =", i)
        if number1 % i == 0 and number2 % i == 0:
            if minVal == None or i < minVal:
                minVal = i
            if maxVal == None or i > maxVal:
                maxVal = i

    return (minVal, maxVal)


# Test harness
testDivisors()
minDiv, maxDiv = findExtremeDivisors(100, 200)
print("Min Divisor =", minDiv, "\t=> Answer = 2")
print("Max Divisor =", maxDiv, "\t=> Answer = 100")
