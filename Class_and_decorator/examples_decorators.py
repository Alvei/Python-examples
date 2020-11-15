""" Examples_decorators.py
Decorators are functions which modify the functionality of other functions.
They help to make our code shorter and more Pythonic.

The decorator function provides info on the funtion and returns either
the same result or the square of the result (in the second case).
Note that func and its parameters args,kwargs are available
to new_function inside the decorator.
References
https://book.pythontips.com/en/latest/decorators.html
https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""
from functools import wraps
from typing import Callable


def hi(name="Hugo"):
    """ Simple function with kwargs name assigned. It will always return hi Hugo """
    return "hi " + name


def hi2(name="Mili") -> None:
    """We can define functions in other functions.
    In other words: we can make nested functions."""

    print("now you are inside the hi2() function")

    def greet2():
        return "\tnow you are in the greet2() function"

    def welcome2():
        return "\tnow you are in the welcome2() function"

    print(greet2())
    print(welcome2())
    print("now you are back in the hi2() function")


def hi3(name="Anais and Zoe"):
    """It is not necessary to execute a function within
    another function, we can return it as an output as well."""

    def greet3():
        return "\tnow you are in the greet3() function"

    def welcome3():
        return "\tnow you are in the welcome3() function"

    # Not returning the function to avoid execution
    # Want to pass the variables
    if name == "Anais and Zoe":
        return greet3
    else:
        return welcome3


def hi4():
    return "\thi Georges!"


def document_it(func):
    """First decorator function that will give basic info on
    running a function.
    Signature: (function) -> what ever the function returns."""

    def new_function(*args, **kwargs):
        """Scope of new function is document_it. It will print some
        info and then return the operation of the passed function.
        Signature: (list, list) -> what ever the function returns"""

        # Run the passed function and save the result
        result = func(*args, **kwargs)
        print(
            f"Function: {func.__name__}, Positional arg: {args} Keywords arg: {kwargs} Result: {result}"
        )

        return result

    return new_function


def square_it(func):
    """Second decorator function. Does the same but square the output
    of the passed function."""

    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        ans = result * result
        print(f"Function: {func.__name__}: Result: {result} Squared: {ans}")

        return ans

    return new_function


def add_integers(a: int, b: int) -> int:
    """ Simple integer addition"""
    return a + b


@document_it
def substract_integers(a: int, b: int) -> int:
    """@document_it uses @ to make the implicit assignment. """
    return a - b


# @document_it
@square_it
def mult_integers(a: int, b: int) -> int:
    return a * b


def reviewing_functions():
    print(f"Calling hi(): {hi()}")  # hi Hugo
    # We can even assign a function to a variable. Nnot using parentheses b/c
    # not calling the function hi() instead putting it into the greet variable.
    greet = hi
    print(f"Calling greet(): {greet()}")  # hi Hugo
    hi2()  #  Calling hi2()
    # will finish with None since there is no return to hi2()
    print(f"Calling inside print: {hi2()}")
    # This shows that whenever you call hi(), greet() and welcome()
    # are also called. However the greet() and welcome() functions
    # are not available outside the hi() function e.g:

    # greet()
    # outputs: NameError: name 'greet' is not defined

    temp = hi3()
    print(temp)  # temp points to the function greet3() inside hi3()
    print(temp())  # Execute the function within hi3()
    print(hi3(name="bob"))  # points to the function welcome3()
    print(hi3(name="bob")())  # this executes where it points (ie welcome3()


def do_something_before_hi(func):
    """ Passing a function as an argument. """
    print("I am doing some boring work before executing hi4()")
    print(func())


def a_new_decorator(a_func):
    def wrap_the_function():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")

    return wrap_the_function


def reviewing_decorators():
    do_something_before_hi(hi4)  # Passing the function as an argument
    temp = a_new_decorator(hi4)  # temp points to the wrap_the_function
    print(f"\nPointing to: {temp}\n")
    print(f"Now executing temp: {temp()}")
    hi4 = a_new_decorator(hi4)
    hi4()


def outer_function(msg: str) -> Callable:
    def inner_function():
        print(msg)

    return inner_function  #  Does not execute the function but returns it


def decorator_function(original_function: Callable):
    """ Instead of receiving variable it receives a funciton as an argument. """

    def wrapper_function(*args, **kwargs):
        """ Inner function has access to outer function variables. """
        print(f"Wrapper executed before {original_function.__name__}")
        return original_function(*args, **kwargs)  # Execute the passed function

    return wrapper_function  # Does not execute the function but returns it


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call method. executed before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)  # Execute the passed function


def my_logger(orig_func):
    import logging

    logging.basicConfig(
        filename="{}.log".format(orig_func.__name__), level=logging.INFO
    )

    @wraps(orig_func)  # Needed to have the stack decorators
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args} and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper  # point to function not execute the function


def my_timer(orig_func: Callable):
    import time

    @wraps(orig_func)  # Needed to have stack decorators
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


def display():
    """ Function to be passed to the decorator. """
    print(f"Running {display.__name__}")


# @decorator_class  # Less common but equivalent
# @decorator_function # More common
@my_timer
@my_logger
def display2():
    """ Function to be passed to the decorator. """
    import time

    time.sleep(1)
    print(f"Running display2")


# @decorator_class  # Less common but equivalent
# @decorator_function # More common
@my_logger
def display_info(name: str, age: int):
    print(f"display_info {name} {age}")


def main():
    """ Test harness """
    # reviewing_functions()
    # reviewing_decorators()
    hi_func = outer_function("Hi")
    bye_func = outer_function("Bye")
    hi_func()
    bye_func()

    decorated_display = decorator_function(display)  # It points to a function
    decorated_display()

    display2()  # noticed that we do not need to do the 2 steps assigments

    display_info("Bob", 50)

    #############
    print(f"\nSimple addition: {add_integers(3, 5)}")

    # Manual decorator assignments
    cooler_add_ints = document_it(add_integers)
    cooler_add_ints(3, 5)
    substract_integers(5, 3)

    print(f"Multiplication with decorator Square_it: {mult_integers(5, 3)}")


if __name__ == "__main__":
    main()