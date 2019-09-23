import timeit, functools
from functools import lru_cache

def reverse_slice(text: str) -> str:
    """ Reversing the text using slicing. Most pythonic. """
    text = text[::-1]
    return text


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



def main():
    """ Test harness """

    text = 'bonjour'
    num = 54

    # Define a new  Timer object with a partial object as parameter
    # Important to have a function with no parameter for Timer.
    t = timeit.Timer(functools.partial(reverse_slice, text))
    print(text)
    this_time = t.timeit(150000)
    print("Time: {0:.3f}".format(this_time))

    print('fastFib2 of \t\t', num, ' = ', str(fast_fib2(num))) # Should be super fast

if __name__ == "__main__":
    main()
