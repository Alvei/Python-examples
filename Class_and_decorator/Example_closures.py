"""
    examples_closures.py
    Closures can avoid the use of global values and provides some form of data hiding.
    They are used extensively by decorators.

    The value in the enclosing scope is remembered even when the variable goes out of scope
    or the function itself is removed from the current namespace.
    The criteria that must be met to create closure in Python are:
        - Must have a nested function.
        - Nested function must refer to a value defined in the enclosing function.
        - Enclosing function must return the nested function.

        Wikipedia: A closure is a record storing a function together with an environment
        : a mapping associating each free variables of the function with the value or
        storage location to which the name was bound when the closure was created.
        A closure, unlike a plain function, allows the function to access those captured
        variables through the closure's reference to them. even when the function is
        invoke outside their scope."""
import logging
from typing import Callable

logging.basicConfig(filename="example.log", level=logging.INFO)


def print_msg(msg: str) -> None:
    """This is the outer enclosing function. The nested function printer() is able
    to access the non-local variable msg of the enclosing function.
    This is not closure since it does not return the nested function."""

    def printer() -> None:
        """ This is the nested function. """
        print(msg)

    printer()


def print_msg2(msg: str) -> Callable:
    """This is the outer enclosing function. What would happen if the last line
    of the function print_msg() returned the printer() function instead of calling it?
    This is a closure."""

    def printer() -> None:
        """ This is the nested function. """
        print(msg)

    return printer  # This got changed. Returning the nested function


def make_multiplier_of(n: int) -> Callable:
    def multiplier(x: int) -> int:
        """ This is the nested function. It accesses n."""
        return x * n

    return multiplier  # Returning the nested function


def logger(func: Callable) -> Callable:
    """ Outer function. """

    def log_func(*args) -> None:
        """ Inner function. """
        logging.info(f"Running {func.__name__} with arg: {args}")
        print(func(*args))

    return log_func


def add(x: int, y: int) -> int:
    return x + y


def main():

    print_msg("Hello")  # Call the nested function to print hello
    another = print_msg2("Hello2")  # Bind the function (and parameter) to a variable
    another()  # Call the closure function

    # Assign the functions and define n
    times3 = make_multiplier_of(3)
    times5 = make_multiplier_of(5)

    print(f"3*9 = {times3(9)} \t?= 27")
    print(f"5*3 = {times5(3)} \t?= 15")
    print(f"5*3*2 = {times5(times3(2))} \t?= 30")

    """ All function objects have a __closure__ attribute that returns a
        tuple of cell objects if it is a closure function.
        We know times3 and times5 are closure functions. """
    print("closure attribute", times3.__closure__[0].cell_contents)
    print("closure attribute", times5.__closure__[0].cell_contents)

    add_logger = logger(add)
    add_logger(10, 5)


if __name__ == "__main__":
    main()
