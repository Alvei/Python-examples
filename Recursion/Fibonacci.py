""" Fibonacci.py
    Compares the recursive implementation of Fib
    fib1() is basic recursion.
    fib2() is using a while loop.
    fib3() is using yield.
    fib4() is  using dict to create memoization.
    fib5() is using lru_cache from functools to do memoization.
    fib6() is using lru_cache from functools to do memoization. Using tuples.
    fibt7() is a manual memoization.
    fib6 > fib2 > fib5 > fib7 > fib1
    The tuple memoization is best. Recursion is worst.
    Looping (fib2) is suprisingly fast. LRU_cach or dict implementation is similar
    My implementation of LRU_cache with decorator is pretty bad. Probably the sorting and conversion to tuple.
    Good article at https://fulmicoton.com/posts/fibonacci/  """
from functools import lru_cache
import time
from typing import Generator, Dict, Tuple

def fib1(num: int) -> int:
    """Calculates the fibonacci number of num. """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    # Base case
    if num < 2:
        return num
    return fib1(num - 1) + fib1(num - 2)

def fib2(num: int) -> int:
    """ Calculates the fibonacci number of num.
        Use loops and double assignments.
        Has linear computational time and constant memory. """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    old, new = 0, 1
    for _ in range(num):
        old, new = new, old + new
    return old

def fib3(num: int) -> Generator:
    """ Calculates the fibonacci number of num. Use generator. """
    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    yield 0  # special case

    if num > 0:
        yield 1  # special case

    last, next_up = 0, 1  # initially set to fib(0) and fib(1)

    for _ in range(1, num):
        last, next_up = next_up, last + next_up
        yield next_up  # main generation step

def fib4(num: int, memo: Dict[int, int] = {}) -> int:
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses a dictionary of previously computed Fib numbers.
        dictionary entry in memo => (key = num, value = fib(num))
        Initialize memo if empty. """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    # Base case
    if num < 2:
        return num
    try:  # Check to see if already computed and in dictionary
        return memo[num]
    except KeyError:  # Otherwise calculate the new {key, value} pair
        result = fib4(num - 1, memo) + fib4(num - 2, memo)
        memo[num] = result
        return result

@lru_cache(maxsize=1000)
def fib5(num: int) -> int:
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses functools to do memoization. """

    if not isinstance(num, int):
        raise TypeError("Expecting int but got", type(int))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    if num < 2:
        return num

    return fib5(num-1) + fib5(num-2)

@lru_cache(maxsize=None)
def fib6(num: int) -> Tuple[int, int]:
    """ Implementation of recursive fib that does not calculate the same fib
        number. It uses functools to do memoization. By using tuples and doing 2 calculations
        in every recursion and takes better advantage of memoization.
        The first element [0] of tuple is the current answer. The second is F[n+1].
        This implementation is very interesting. No reference for the algo. """

    if not isinstance(num, int):
        raise TypeError("Expecting int but got", type(int))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    # Base case
    if num == 0:
        return 0, 1

    else:
        num_a, num_b = fib6(num // 2)
        num_c = num_a * (num_b * 2 - num_a)
        num_d = num_a * num_a + num_b * num_b

        if num % 2 == 0:
            return num_c, num_d
        else:
            return num_d, num_c + num_d

def memoize(f):
    """ Decorator for memoization function. """
    cache = {}
    def aux(*args, **kargs):
        """ Dummy function. Dict are not hashable, transform kargs in a tuple of (key, value). """
        key = (args, tuple(sorted(kargs.items())))

        if key not in cache:
            cache[key] = f(*args, **kargs)
        return cache[key]
    return aux

@memoize
def fib7(num: int) -> int:
    """ Calculate Fib number. """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    if num == 0:
        return 0
    if num == 1:
        return 1
    return fib7(num-1) + fib7(num-2)

def test_fib(num: int) -> None:
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """

    print("Traditional \t Memoization ")
    for i in range(num + 1):
        print(i, ':', str(fib1(i)), "\t\t", str(fib3(i)))


def test_fib2(num: int) -> None:
    """ Test harness. The last call with n = 35 is instanteneous
        for fastFib but takes long for fib """
    print(f"fastFib of {num} =\t\t{str(fib3(num))}")   # Should be super fast
    print(f"fastFib2 of {num} =\t{str(fib4(num))}") # Should be super fast
    print("This should take a while....")
    print(f"Traditional recursion Fib {num} =\t {str(fib1(num))}")  # Should take some time
    print(f"Traditional loop Fib {num} =\t {str(fib2(num))}")  # Should take some time

def time_fib(func, num: int) -> int:
    """ Simple function to calculate execution time. """
    start = time.time()
    answer = func(num)
    end = time.time()
    print(f"{func.__name__} took {(end-start)*1000:.2f} miliseconds")
    return answer

def main():
    """ Test Harness """
    #test_fib(4)
    #test_fib2(35)
    #test_fib(10)
    # This is still buggy
    #for index in fib_yield(35):
    #    print(index)
    #print("Using Yield:", fib_yield(10))
    num = 399
    test_func = [fib7, fib5, fib4, fib2]  # Cannot time the yield and the tuple memoization
    for func in test_func:
        time_fib(func, num)

    # Have to do manually since it has a tuple return value
    start = time.time()
    answer = fib6(num)
    end = time.time()
    print(f"{fib6.__name__} took {(end-start)*1000:.2f} miliseconds")


if __name__ == '__main__':
    main()
