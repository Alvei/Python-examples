"""
Check to see if a character is at beginning of string
and return 1 if true
Created on Wed Sep 19 21:18:07 2018

for Python 3.5"""


def char_at_beg(string, char):
    """ Signature: (str, str) -> boolean"""
    if string.lower().startswith(char):
        return 1
    return 0


print(char_at_beg("xoxo", 'x'))
