""" Series of small text processing functions."""
from functools import wraps

def mapper(func):
    """ Decorator function that allows the use of a list rather than strings in camelcase
    Signature: (function) -> list."""

    @wraps(func)        # Preserve the docstring of the original function
    def inner(list_of_values):
        return [func(value) for value in list_of_values]
    return inner


@mapper
def camelcase(my_string):
    """ Takes string like this how_are_you and returns string like HowAreYou.
    Signature: (str) -> str."""
    return "".join([word.capitalize() for word in my_string.split('_')])

#print("Simple case using a string as an input:", camelcase("how_are_you"))

my_list = ['bonjour_comment', "how_are_you", "This_is_it"]
print(camelcase(my_list))
print(camelcase.__doc__)