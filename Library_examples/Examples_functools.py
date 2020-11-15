""" Examples_funtools.py
    Simple examples of using the functools libray.
    LRU -  Least Recently Used - the cach will keep the most recent input/result pairs by discarding the least recent/oldest entry.
    wraps - decorators
    https://medium.com/better-programming/every-python-programmer-should-know-lru-cache-from-the-standard-library-8e6c20c6bc49
    https://book.pythontips.com/en/latest/decorators.html
    """
import timeit, functools
from functools import lru_cache, wraps


def reverse_slice(text: str) -> str:
    """ Reversing the text using slicing. Most pythonic. """
    text = text[::-1]
    return text


@lru_cache(maxsize=1000)
def fast_fib2(num: int) -> int:
    """Implementation of recursive fib that does not calculate the same fib
    number. It uses functools to do memonization."""

    if not isinstance(num, int):
        raise TypeError("Expecting int but got", type(int))
    if num < 0:
        raise ValueError("num must be positive. It is", num)

    if num in (0, 1):
        return 1
    else:
        return fast_fib2(num - 1) + fast_fib2(num - 2)


def a_new_decorator(a_func):
    @wraps(a_func)
    def wrap_the_function():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrap_the_function


@a_new_decorator
def a_function_requiring_decoration() -> None:
    """Hey yo! Decorate me!"""
    print("\tI am the function which needs some decoration to " "remove my foul smell")


def main():
    """ Test harness """

    print(a_function_requiring_decoration.__name__)
    print(a_function_requiring_decoration)
    a_function_requiring_decoration()

    text = "bonjour"
    num = 54

    # Define a new  Timer object with a partial object as parameter
    # Important to have a function with no parameter for Timer. functools.partial does that.
    t = timeit.Timer(functools.partial(reverse_slice, text))
    print(text)
    this_time = t.timeit(150000)
    print("Time: {0:.3f}".format(this_time))

    print("fastFib2 of", num, "=", str(fast_fib2(num)))


if __name__ == "__main__":
    main()
