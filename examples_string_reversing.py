"""
Simple functions to reverse a string.
"""

def reverse(string) -> str:
    """ Reversing the text using slicing. Most pythonic
        Signature: (str) -> str. """
    string = string[::-1]
    return string

def reverse_basic(text) -> str:
    """ Reverse by adding characters upfront to the string.
        Signature: (str) -> str. """
    new_text = ""
    for index in text:
        new_text = index + new_text
    return new_text


def reverse_counter(text) -> str:
    """ Reversing the text it receives using decremented counter.
        Signature: (str) -> str. """
    new_text = ''
    text = str(text)   # Convert the argument into a string if not already
    my_list = len(text) - 1

    for _ in text:
        new_text = new_text + text[my_list]
        my_list -= 1

    return new_text


def reverse_recursion(text) -> str:
    """ Function that is reversing the text it receives using recursion.
        Signature: (str) -> str. """
    if len(text) == 0:  # Base case
        return text
    else:
        return reverse_recursion(text[1:]) + text[0]


def main():
    """ Test harness """
    functions = [reverse, reverse_basic, reverse_counter, reverse_recursion]

    for func in functions:
        print(func("bonjour"))

if __name__ == "__main__":
    main()
