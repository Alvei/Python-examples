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
    My implementation of LRU_cache with decorator is bad. Probably sorting & conversion to tuple.
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

    num_a, num_b = fib6(num // 2)
    num_c = num_a * (num_b * 2 - num_a)
    num_d = num_a * num_a + num_b * num_b

    if num % 2 == 0:
        return num_c, num_d

    return num_d, num_c + num_d

def memoize(func):
    """ Decorator for memoization function. """
    cache = {}
    def aux(*args, **kargs):
        """ Dummy function. Dict are not hashable, transform kargs in a tuple of (key, value). """
        key = (args, tuple(sorted(kargs.items())))

        if key not in cache:
            cache[key] = func(*args, **kargs)
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

def matmult(matrix_a: Tuple[Tuple[int, int], Tuple[int, int]],
            matrix_b: Tuple[Tuple[int, int], Tuple[int, int]]) \
                -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """ 2X2 matrix multiplications using tuples. """
    def val(row: int, col: int) -> int:
        """ Element multiplications. """
        return matrix_a[row][0] * matrix_b[0][col] + matrix_a[row][1] * matrix_b[1][col]
    # Do the multiplication for each i,j pair or row, col pair
    return (
        (val(0, 0), val(0, 1)),
        (val(1, 0), val(1, 1))
    )

def matrix_power(matrix_a: Tuple[Tuple[int, int], Tuple[int, int]], num: int) \
    -> Tuple[Tuple[int, int], Tuple[int, int]]:
    """ Apply the power of num to a 2x2 matrix. """

    # Base case
    if num == 0:
        return ((1, 0), (0, 1))

    if num % 2 == 1:
        return matmult(matrix_a, matrix_power(matrix_a, num-1))

    root = matrix_power(matrix_a, num//2)
    return matmult(root, root)

def fib8(num: int) -> int:
    """ Calculate Fib number. Using matrix algebra and a closed form.
        See Structure and interpretation of Computer Programs. """

    # Check that the input is a positive integer
    if not isinstance(num, int):
        raise TypeError("num must be an int. It is", type(num))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    # Matrix that allows to move one step ahead
    matrix_m: Tuple[Tuple[int, int], Tuple[int, int]] = ((0, 1), (1, 1))

    # Apply the matrix power function num time to find FIB(num). Keep 1st element
    return matrix_power(matrix_m, num)[0][1]


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
    print(f"{func.__name__} took {(end-start)*1000:.2f} miliseconds. answer: {answer}")
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
    num = 20
    test_func = [fib7, fib5, fib4, fib2]  # Cannot time the yield and the tuple memoization
    for func in test_func:
        time_fib(func, num)

    # Have to do manually since it has a tuple return value
    start = time.time()
    answer = fib6(num)
    end = time.time()
    print(f"{fib6.__name__} took {(end-start)*1000:.2f} miliseconds. answer: {answer[0]}")

    print(f"\nDoing it with large number very fast!!!!\n{fib8(2000)}")
    A = ((1, 2), (3, 1))
    for num in range(10):
        print(f"{num} -> {matrix_power(A,num)}")


if __name__ == '__main__':
    main()
