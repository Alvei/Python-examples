""" test_reversing.py
    Different function that reverse a string.
    The partial() is used for partial function application which “freezes”
    some portion of a function’s arguments and/or keywords resulting in a
    new object with a simplified signature.
    https://docs.python.org/3/library/functools.html
"""
import unittest
from reversing import reverse_slice, reverse_iterator, reverse_method, reverse_lateral, reverse_counter, reverse_recursion
import timeit, functools

def main():
    """ Test harness """
    dict_functions = {"slicing": reverse_slice, "iterator": reverse_iterator, "list method": reverse_method,
                    "lateral": reverse_lateral, "counter": reverse_counter, "recursion": reverse_recursion}
    text = 'bonjour'
    a = 1
    time = []
    print("Approach\tAnswer\t\tTime")
    for name, func in dict_functions.items():
        # Define a new  Timer object with a partial object as parameter
        # Important to have a function with no parameter for Timer.
        t = timeit.Timer(functools.partial(func, text))
        this_time = t.timeit(150000)
        time.append(this_time)
        print("{0:}:\t{1:}\t\t{2:.3f}".format(name, func(text), this_time))

    hi = max(time)
    lo = min(time)
    print("\nmin:{0:.3f} max:{1:.3f} ratio: {2:.0f}X".format(lo, hi, hi/lo))

if __name__ == "__main__":
    main()
