"""Etudes Fibonacci.py
   Compares the recursive implementation of Fib with the one using
   Hashing and dynamic programing
   Python 3.5"""
from functools import lru_cache


def fib_loop(num):
    """ Calculates the fibonacci number of num.
        Use loops and double assignments.
        Signature (int) -> int """
    assert num >= 0 and isinstance(num, int)

    old, new = 0, 1
    for _ in range(num):
        old, new = new, old + new
    return old


def fib(num):
    """Calculates the fibonacci number of num.
       Signature (int) -> int """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

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

@lru_cache(maxsize = 1000)
def fast_fib2(num):
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses functools to do memoization.
        Signature (int, dict) -> int """

    if not isinstance(num, int):
        raise TypeError("Expecting int but got", type(int))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    if num in (0,1):
        return 1
    else:
        return fast_fib2(num-1) + fast_fib2(num-2)


def fib_yield(num):
    """ Calculates the fibonacci number of num. Use generator.
        Signature (int) -> int """
    yield 0  # special case

    if num > 0:
        yield 1  # special case

    last, next = 0, 1  # initially set to fib(0) and fib(1)

    for _ in range(1, num):
        last, next = next, last + next
        yield next  # main generation step

def test_fib(num):
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """

    print("Traditional \t Memoization ")
    for i in range(num + 1):
        print(i, ':', str(fib(i)), "\t\t", str(fast_fib(i)))


def test_fib2(num):
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """
    print('fastFib of \t\t', num, ' = ', str(fast_fib(num)))   # Should be super fast
    print('fastFib2 of \t\t', num, ' = ', str(fast_fib2(num))) # Should be super fast
    print("This should take a while....")
    print('Traditional recursion Fib \t', num, ' = ', str(fib(num)))  # Should take some time
    print('Traditional loop Fib \t\t', num, ' = ', str(fib_loop(num)))  # Should take some time


def main():
    """ Test Harness """

    print('\n'); test_fib(4)
    print('\n'); test_fib2(35)

    # This is still buggy
    #for index in fib_yield(35):
    #    print(index)
    #print("Using Yield:", fib_yield(10))


if __name__ == '__main__':
    main()
