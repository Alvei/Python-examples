"""
examples_closures.py
Closures can avoid the use of global values and provides some form of data hiding. They are used extensively by decorators.

The value in the enclosing scope is remembered even when the variable
goes out of scope or the function itself is removed from the current
namespace. The criteria that must be met to create closure in Python are summarized in the following points.

- We must have a nested function (function inside a function).
- The nested function must refer to a value defined in the enclosing
  function.
- The enclosing function must return the nested function.
"""


def print_msg(msg):
    """ This is the outer enclosing function.
        the nested function printer() is able to access the
        non-local variable msg of the enclosing function."""

    def printer():
        """ This is the nested function"""
        print(msg)

    printer()


# We execute the function Output: Hello
print_msg("Hello")


def print_msg2(msg):
    """ This is the outer enclosing function.
        what would happen if the last line of the function print_msg()
        returned the printer() function instead of calling it?"""

    def printer():
        """ This is the nested function."""
        print(msg)

    return printer  # This got changed. Returning the function


# Now let's try calling this function. Output: Hello
# The returned function is bound to the name another
# This technique by which some data (Hello) gets attached to
# the code is called closure in Python.
another = print_msg2("Hello2")
another()


def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier


# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print("3*9 =", times3(9))

# Output: 15
print("5*3 =", times5(3))

# Output: 30
print("5*3*2 = ", times5(times3(2)))


""" All function objects have a __closure__ attribute that returns a
    tuple of cell objects if it is a closure function. Referring to
    the example above, we know times3 and times5 are closure functions."""
print(times3.__closure__[0].cell_contents)
print(times5.__closure__[0].cell_contents)
