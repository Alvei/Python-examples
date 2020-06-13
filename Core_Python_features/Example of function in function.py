"""
Define functions inside other functions. Explore different scope.
Created on Fri Jan 02 13:18:56 2015
"""


def greet1(name):
    """ Define a function inside another function. Scope of get_msg() limited to greet1()"""

    def get_msg():
        return "Hello "
    return get_msg() + name


def greet2(name):
    """ greet2 will be passed as an argument."""
    return "Hello " + name


def call_func(func):
    """ Passing a function called func as an argument."""
    other_name = "Bob"
    return func(other_name)  # It is returning the output of func()


def compose_greet_func():
    """Functions can return other functions."""
    def get_msg(name):
        return "Hello there!" + name
    return get_msg    # returning a function get_msg


# Assigning a function to greet. greet becomes a function that behaves like the get_msg function
greet = compose_greet_func()

print(greet("julie"))       # Print Hello there! julie


print(greet1("john"))       # Output : Hello John
print(call_func(greet2))    # Calling  function with greet2 as a functional arg. Output: Hello Bob
