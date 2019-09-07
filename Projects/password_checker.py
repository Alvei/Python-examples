""" password_checker.py
Strong Password detection with Regexes.
Do not let the user specific a password that does not meet a set of conditions
First version is from article the second does an iteration on dictionary.
Inspired by
https://medium.com/analytics-vidhya/intro-to-regexes-strong-password-detection-in-python-2138fc3cf8bf
https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
"""
import re
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def password_strength():
    """ Signature: (None) -> str. """

    # Set the initial variable as False so that when it is true later (i.e. strong password entered), the program exits.
    pass_strong = False

    # Strength Checks
    char_regex = re.compile(r'(\w{8,})') # Check if password has at least 8 characters
    lower_regex = re.compile(r'[a-z]+')  # Check if at least one lowercase letter
    upper_regex = re.compile(r'[A-Z]+')  # Check if atleast one upper case letter
    digit_regex = re.compile(r'[0-9]+')  # Check if at least one digit.

    # Looping until pass_strong is set to True. Thereafter exit function.
    while not pass_strong:
        password_text = input('Enter Password (must be +8 charaters, contain uppercases, numbers): ')

        if char_regex.findall(password_text) == []:  # Checks if the password does not contain 8 characters and returns a message
            print('Password must contain at least 8 characters')
        elif lower_regex.findall(password_text)==[]: # Checks if the password does not contain a lowercase character and returns a message
            print('Password must contain at least one lowercase character')
        elif upper_regex.findall(password_text)==[]: # Checks if the password does not contain an uppercase character and returns a message
            print('Password must contain at least one uppercase character')
        elif digit_regex.findall(password_text)==[]: # Checks if the password does not contain a digit character and returns a message
            print('Password must contain at least one digit character')
        else:  # if the above 4 conditions are successfully passed, pringt out a message saying the password is strong.
            pass_strong = True

    print('Your password is strong. Good job!')
    return password_text # break out of function.


def password_strength2():
    """ Signature: (None) -> str. """

    # Set the initial variable as False so that when it is true later (i.e. strong password entered), the program exits.
    pass_strong = False

    # Strength Checks
    char_regex = re.compile(r'(\w{8,})') # Check if password has at least 8 characters
    lower_regex = re.compile(r'[a-z]+')  # Check if at least one lowercase letter
    upper_regex = re.compile(r'[A-Z]+')  # Check if atleast one upper case letter
    digit_regex = re.compile(r'[0-9]+')  # Check if at least one digit.

    checks = {  '8 characters': char_regex,
                'one lowercase letter': lower_regex,
                'one uppercase letter': upper_regex,
                'one digit': digit_regex}

    msg = 'Password must contain at least '

    # Looping until pass_strong is set to True. Thereafter exit function.
    while not pass_strong:
            password_text = input('Enter Password (must be +8 charaters, contain uppercases, numbers): ')

            for text, match in checks.items():
                logging.debug(text + " " + str(pass_strong))
                if match.findall(password_text) == []:  # Checks if the password does not contain match
                    print("\t" + msg + text)
                    pass_strong = False
                    break
                else:
                    logging.debug("changing flag")
                    pass_strong = True

    print('Your password is strong. Good job!')
    return password_text


def main():
    """ Test harness """
    print(password_strength2())

if __name__ == "__main__":
    main()
