""" palindrome_recursion.py
"""
from typing import List, Any

def is_palindrome_list(my_list: List[Any]) -> bool:
    ''' Check if a list is a palindrome. '''

    assert isinstance(my_list, list)  # Check that name is a list

    temp = my_list[:]   # Make a copy of the list
    temp.reverse()

    if temp == my_list:
        return True
    return False

def to_chars(string: str) -> str:
    """ Converts all letters to lowercase & removes all non-letters. """
    string_lower = string.lower()
    letters = ''
    for char in string_lower:
        if char in 'abcdefghijklmnopqrstuvwxyz':
            letters = letters + char
    return letters

def is_palindrome(s: str) -> bool:
    """ Check if a word is a palindrome. Punctuations marks, blanks, and capitalization ignored."""
    assert isinstance(s, str)  # Check that name is a string

    def is_pal(txt: str) -> bool:
        """ Determine if a string is a Palindrome. """

        # print("   isPal called with", s)
        # Base case
        if len(txt) <= 1:
            # print("  About to return True from base case")
            return True

        """ answer is a bolean. Checking two conditions:
            1) ensure 1st and last letter are the same
            2) launch a recursive call with those two letters removed"""
        answer = txt[0] == txt[-1] and is_pal(txt[1:-1])
        # print("   About to return", answer, "for", s)
        return answer

    return is_pal(to_chars(s))


def main():
    """ Main code """

    print("dogGod is a palindrome?", is_palindrome("dogGod"))
    print("doGOOD is a palindrome?", is_palindrome("doGOOD"))
    print("[1, 2, 1] palindrome?", is_palindrome_list([1, 2, 1]))
    print("[1, 2, 2] palindrome?", is_palindrome_list([1, 2, 2]))


if __name__ == '__main__':
    main()
