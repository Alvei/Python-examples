
"""
examples_recursions_functions.py
Examples of recursions:
factorial()
Palindrome with list

Created on Fri Dec 26 10:50:21 2014
for Python 3.5
"""


def is_palindrome_list(name):
    ''' Check if a word is a palindrome
        Signature: (list) -> boolean.'''

    assert isinstance(name, list)  # Check that name is a list

    temp = name[:]   # Make a copy of the list
    temp.reverse()

    if temp == name:
        return True

    return False


def is_palindrome(s):
    """ Check if a word is a palindrome.
        Punctuations marks, blanks, and capitalization ignored.
        Signature: (list) -> boolean."""

    assert isinstance(s, str)  # Check that name is a string

    def to_chars(string):
        """ Converts all letters to lowercase & removes all non-letters
            Signature: (str) -> str."""
        string = string.lower()
        letters = ''
        for char in string:
            if char in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + char
        return letters

    def is_pal(s):
        """ Determine if a string is a Palindrome.
            Signature: (string) -> boolean"""

        # print("   isPal called with", s)
        # Base case
        if len(s) <= 1:
            # print("  About to return True from base case")
            return True

        """ answer is a bolean. Checking two conditions:
            1) ensure 1st and last letter are the same
            2) launch a recursive call with those two letters removed"""
        answer = s[0] == s[-1] and is_pal(s[1:-1])
        # print("   About to return", answer, "for", s)
        return answer

    return is_pal(to_chars(s))


def test_is_palindrome():
    print("Try dogGod")
    print(is_palindrome("dogGod"))
    print("Try doGOOD")
    print(is_palindrome("doGOOD"))


test_is_palindrome()
print(is_palindrome_list([1, 2, 1]), "should be True")
print(is_palindrome_list([1, 2, 2]), "should be False")
