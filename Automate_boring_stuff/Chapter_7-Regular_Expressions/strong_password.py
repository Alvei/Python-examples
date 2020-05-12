""" strong_password.py
    Use Regex to extract all the NA phone numbers and emails from a file.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 177.
"""
import re

def chk_pwd(text: str) -> bool:
    """ Check if a password is strong? To be strong you need to be at least 8 character, to have
        at least one upper case, one lower case and one digit, must have at least one of [._%+-].
        Note I was not able to get the weird test to work with !."""

    length_regex = re.compile(r'.{8,}')
    upper_regex = re.compile(r'[A-Z]')
    lower_regex = re.compile(r'[a-z]')
    digit_regex = re.compile(r'[0-9]')
    weird_regex = re.compile(r'[._%+-]')
    regex_list = [length_regex, upper_regex, lower_regex, digit_regex, weird_regex]
    #regex_list = [upper_regex, lower_regex, digit_regex]

    for check in regex_list:
        if re.search(check, text):  # If there is a match, the if statement is True.
            pass
        else:
            return False

    # Default case
    return True


def main():
    """ Test harness """
    test_password = ['aaaa', 'Ab9ab9+2', 'Ab9ab9!2', 'ab9ab9+2']
    for text in test_password:
        print(f"{text} ? {chk_pwd(text)}")

if __name__ == "__main__":
    main()
