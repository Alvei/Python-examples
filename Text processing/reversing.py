""" reversing.py
    Different function that reverse a string.
"""

def reverse_slice(text: str) -> str:
    """ Reversing the text using slicing. Most pythonic. """
    text = text[::-1]
    return text

def reverse_iterator(text: str) -> str:
    """ Reversing text using the reversed() function. """
    reversed_iterator = reversed(text)
    reversed_text = "".join(reversed_iterator)
    return reversed_text

def reverse_method(text: str) -> str:
    """ Reversing text using the built-in reverse() method. This method cannot be used directly
        with the string data type. We must 1st convert to a list, then reverse the list and use join(). """
    temp_list = list(text)
    temp_list.reverse()
    reversed_text = "".join(temp_list)
    return reversed_text

def reverse_lateral(text: str) -> str:
    """ Traverse forward and add character upfront. """
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def reverse_counter(text: str) -> str:
    """ Reversing the text it receives using decremented counter. """
    reversed_text = ''
    my_list = len(text) - 1

    for _ in text:
        reversed_text = reversed_text + text[my_list]
        my_list -= 1
    return reversed_text

def reverse_recursion(text: str) -> str:
    """ Function that is reversing the text it receives using recursion. """
    if len(text) == 0:  # Base case
        return text
    else:
        return reverse_recursion(text[1:]) + text[0]

