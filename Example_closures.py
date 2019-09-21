"""
    examples_closures.py
    Closures can avoid the use of global values and provides some form of data hiding.
    They are used extensively by decorators.

    The value in the enclosing scope is remembered even when the variable goes out of scope
    or the function itself is removed from the current namespace.
    The criteria that must be met to create closure in Python are:
        - Must have a nested function.
        - Nested function must refer to a value defined in the enclosing function.
        - Enclosing function must return the nested function. """


def print_msg(msg):
    """ This is the outer enclosing function. The nested function printer() is able
        to access the non-local variable msg of the enclosing function.
        This is not closure since it does not return the nested function."""
    def printer():
        """ This is the nested function. """
        print(msg)
    printer()

def print_msg2(msg):
    """ This is the outer enclosing function. What would happen if the last line
        of the function print_msg() returned the printer() function instead of calling it?
        This is a closure"""
    def printer():
        """ This is the nested function. """
        print(msg)
    return printer  # This got changed. Returning the nexted function

def make_multiplier_of(n):
    def multiplier(x):
        """ This is the nested function. It accesses n"""
        return x * n
    return multiplier # Returning the nested function

def main():

    print_msg("Hello")              # Call the nested function to print hello
    another = print_msg2("Hello2")  # Bind the function (and parameter) to a variable
    another()                       # Call the closure function

    # Assign the functions and define n
    times3 = make_multiplier_of(3)
    times5 = make_multiplier_of(5)

    print("3*9 =", times3(9))               # Output: 27
    print("5*3 =", times5(3))               # Output: 15
    print("5*3*2 = ", times5(times3(2)))    # Output: 30

    """ All function objects have a __closure__ attribute that returns a
        tuple of cell objects if it is a closure function.
        We know times3 and times5 are closure functions. """
    print("closure attribute", times3.__closure__[0].cell_contents)
    print("closure attribute", times5.__closure__[0].cell_contents)

if __name__ == "__main__":
    main()
