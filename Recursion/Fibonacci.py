"""Fibonacci.py
   Compares the recursive implementation of Fib with the one using
   Hashing and dynamic programing. """
from functools import lru_cache
from typing import Generator, Dict


def fib_loop(num: int) -> int:
    """ Calculates the fibonacci number of num.
        Use loops and double assignments. """

    assert isinstance(num, int)
    assert num >= 0

    old, new = 0, 1
    for _ in range(num):
        old, new = new, old + new
    return old


def fib(num: int) -> int:
    """Calculates the fibonacci number of num. """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    # Base case
    if num < 2:
        return num
    return fib(num - 1) + fib(num - 2)


def fast_fib(num: int, memo: Dict[int, int] = {}) -> int:
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses a dictionary of previously computed Fib numbers.
        dictionary entry in memo => (key = num, value = fib(num))
        Initialize memo if empty. """

    assert num >= 0 and isinstance(num, int)

    # Base case
    if num < 2:
        return num
    try:  # Check to see if already computed and in dictionary
        return memo[num]
    except KeyError:  # Otherwise calculate the new {key, value} pair
        result = fast_fib(num - 1, memo) + fast_fib(num - 2, memo)
        memo[num] = result
        return result

@lru_cache(maxsize=1000)
def fast_fib2(num: int) -> int:
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses functools to do memoization. """

    if not isinstance(num, int):
        raise TypeError("Expecting int but got", type(int))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    if num < 2:
        return num
    return fast_fib2(num-1) + fast_fib2(num-2)


def fib_yield(num: int) -> Generator:
    """ Calculates the fibonacci number of num. Use generator. """
    yield 0  # special case

    if num > 0:
        yield 1  # special case

    last, next_up = 0, 1  # initially set to fib(0) and fib(1)

    for _ in range(1, num):
        last, next_up = next_up, last + next_up
        yield next_up  # main generation step

def test_fib(num: int) -> None:
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """

    print("Traditional \t Memoization ")
    for i in range(num + 1):
        print(i, ':', str(fib(i)), "\t\t", str(fast_fib(i)))


def test_fib2(num: int) -> None:
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """
    print(f"fastFib of {num} =\t\t{str(fast_fib(num))}")   # Should be super fast
    print(f"fastFib2 of {num} =\t{str(fast_fib2(num))}") # Should be super fast
    print("This should take a while....")
    print(f"Traditional recursion Fib {num} =\t {str(fib(num))}")  # Should take some time
    print(f"Traditional loop Fib {num} =\t {str(fib_loop(num))}")  # Should take some time


def main():
    """ Test Harness """

    print('\n')
    #test_fib(4)
    print('\n')
    #test_fib2(35)
    test_fib(10)
    # This is still buggy
    #for index in fib_yield(35):
    #    print(index)
    #print("Using Yield:", fib_yield(10))


if __name__ == '__main__':
    main()