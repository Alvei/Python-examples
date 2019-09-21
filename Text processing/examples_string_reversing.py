"""
Simple functions to reverse a string.
"""
import timeit

def reverse(text: str) -> str:
    """ Reversing the text using slicing. Most pythonic. """
    text = text[::-1]
    return text

def reverse_basic(text: str) -> str:
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


def my_function():
    y = 3.1415
    for _ in range(100):
        y = y ** 0.7
    return y



def main():
    """ Test harness """
    functions = [reverse, reverse_basic, reverse_counter, reverse_recursion]
    dict_functions = {"slicing": reverse, "lateral": reverse_basic, reverse_counter, reverse_recursion}
    text = 'bonjour'

    # print(timeit.timeit(reverse(text), number=1000))
    print(timeit.timeit(my_function, number=100000))

    for func in functions:
        print(func(text))
        #print(timeit.timeit(func(text), number=1000))

if __name__ == "__main__":
    main()
