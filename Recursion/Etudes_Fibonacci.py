"""Etudes Fibonacci.py
   Compares the recursive implementation of Fib with the one using
   Hashing and dynamic programing
   Python 3.5"""


def fib_loop(num):
    """ Calculates the fibonacci number of num.
        Use loops and double assignments.
        Signature (int) -> int """
    assert num >= 0 and isinstance(num, int)

    old, new = 0, 1
    for index in range(num):
        old, new = new, old + new
    return old


def fib(num):
    """Calculates the fibonacci number of num.
       Signature (int) -> int """
    assert num >= 0 and isinstance(num, int)

    # Base case
    if num in (0, 1):
        return 1
    return fib(num - 1) + fib(num - 2)


def fast_fib(num, memo={}):
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses a dictionary of previously computed Fib numbers.
        dictionary entry in memo => (key = num, value = fib(num))
        Initialize memo if empty.
        Signature (int, dict) -> int """

    assert num >= 0 and isinstance(num, int)

    # Base case
    if num in (0, 1):
        return 1
    try:  # Check to see if already computed and in dictionary
        return memo[num]
    except KeyError:  # Otherwise calculate the new {key, value} pair
        result = fast_fib(num - 1, memo) + fast_fib(num - 2, memo)
        memo[num] = result
        return result


def test_fib(num):
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """

    for i in range(num + 1):
        print('fib of ', i, ' = ', str(fib(i)))

    for j in range(num + 1):
        print('fast_fib of ', j, ' = ', str(fast_fib(j)))


def test_fib2(num):
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """
    print('fastFib of \t', num, ' = ', str(fast_fib(num)))   # Should be super fast
    print('fib of \t\t', num, ' = ', str(fib(num)))            # Should take some time


print(fib_loop(45))

test_fib(12)
print('\n\n')
test_fib2(35)
