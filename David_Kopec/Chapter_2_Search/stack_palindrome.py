""" stack_palindrome.py. """
from data_classes import Stack

def is_palindrome(word: str) -> bool:
    """ Check if a word is a palindome. Check for empty word. """
    assert len(word) != 0

    str_stack: Stack = Stack()

    # Push all the character onto the stack
    for char in word:
        str_stack.push(char)

    # Go through the characters and pop from the stack
    for char in word:
        if char == str_stack.pop():
            pass            # There is a match
        else:
            return False    # Stop as soon as one character is not a match

    return True  # Default is that it is a palindrome

if __name__ == "__main__":
    TESTS = ["madam", "laval", "marjo"]
    for test in TESTS:
        print(f"is {test} a palindrome? {is_palindrome(test)}")
