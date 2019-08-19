"""
Created on Fri Jan 02 09:10:38 2015

Examples of decorators around simple math operations.
The decorator function provides info on the funtion and returns either
the same result or the square of the result (in the second case).
Note that func and its parameters args,kwargs are available
to new_function inside the decorator.

"""


def document_it(func):
    """ First decorator function that will give basic info on
        running a function.
        Signature: (function) -> what ever the function returns."""
    def new_function(*args, **kwargs):
        """ Scope of new function is document_it. It will print some
            info and then return the operation of the passed function.
            Signature: (list, list) -> what ever the function returns"""

        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keywords arguments:", kwargs)

        # Run the passed function and save the result
        result = func(*args, **kwargs)
        print("Result:", result)

        return result
    return new_function


def square_it(func):
    """ Second decorator function. Does the same but square the output
        of the passed function."""
    def new_function(*args, **kwargs):
        print("Running function:", func.__name__)
        print("Positional arguments:", args)
        print("Keywords arguments:", kwargs)

        result = func(*args, **kwargs)
        print("Result of function:", result)

        return result * result
    return new_function


def add_integers(a, b):
    return a + b


@document_it
def substract_integers(a, b):
    """@document_it uses @ to make the implicit assignment"""
    return a - b


# @document_it
@square_it
def mult_integers(a, b):
    return a * b


# Test harness
# #############
print("Simple addition:", add_integers(3, 5), "\n")

# Manual decorator assignments
cooler_add_ints = document_it(add_integers)
cooler_add_ints(3, 5)
print("\n")

substract_integers(5, 3)
print("\n")

print("Multiplication with decorator Square_it:", mult_integers(5, 3))
