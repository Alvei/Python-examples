""" Chapter_7_isphone_no.py
    Check if number is a telephone number. Various implementation.
    Some with checks various scenarios and others use regex
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 143.
"""
import re

def isphone_no(text: str) -> bool:
    """ Very clumsy implementation. Also only works for xxx-xxx-xxxx. """
    if len(text) != 12:
        return False
    for num in range(0-3):
        if not text[num].isdecimal():
            return False
    if text[3] != '-':
        return False
    if text[7] != '-':
        return False
    for num in range(8, 12):
        if not text[num].isdecimal():
            return False
    return True


def isphone_no2(text: str) -> bool:
    """ Use Regex. """
    # Basic regex
    # phone_no_regex = r'\d{3}-\d{3}-\d{4}'

    # The most robust with the anchor assertion to define beginning and end of line
    phone_no_regex = r'^\(?\d{3}\)?[-.●]\d{3}[-.●]\d{4}$'

    # This search returns a match_object or None. Therefore the if statement is True is not None!
    # print(re.search(phone_no_regex, text))
    if re.search(phone_no_regex, text):
        return True
    return False

def look_phone_no(msg: str) -> list:
    """ Process a line to see if there are phone numbers.
        Clumsy implementation.
        Assumes a phone no is xxx-xxx-xxxx of length 12. """
    length = 12
    phone_no = []

    # Go through the line by moving a chunk of length characters
    for index in range(len(msg)):
        chunk = msg[index:index + length]
        if isphone_no(chunk):
            phone_no.append(chunk)
    return phone_no


def look_phone_no2(text: str) -> list:
    """ Process a line to see if there are phone numbers.
        Assumes a phone no is xxx-xxx-xxxx of length 12. """

    # Basic checks for xxx-xxx-xxxx
    # phone_no_regex = re.compile(r'\d{3}-\d{3}-\d{4}')

    # More advance includes optional (xxx)-xxx-xxxx by putting \(? and \)?
    # phone_no_regex = re.compile(r'\(?\d{3}\)?-\d{3}-\d{4}')

    # Even more advance that accepts (xxx).xxx-xxxx also
    phone_no_regex = re.compile(r'\(?\d{3}\)?[-.●]\d{3}[-.●]\d{4}')

    return phone_no_regex.findall(text)


def main():
    """ Test Harness """

    print(f"1st test of presence: {isphone_no('415-124-5678')}")
    print(f"2nd test of presence: {isphone_no2('415-124-5678')}")

    msg = "Call me at 415-555-1234 tomorrow. 415-555-9999 is my office"
    msg2 = "Call me at 415.555.1234 tomorrow. 415-555-9999 is my office"
    msg3 = "Call me at 415-555-1234 tomorrow. (415)-555-9999 is my office"

    print(f"Message: {msg}")
    print(f"All the phone number(s) found: {look_phone_no(msg)}")
    print(f"All the phone number(s) found: {look_phone_no2(msg)}")

    print(f"\nMessage 2: {msg2}")
    print(f"All the phone number(s) found: {look_phone_no(msg2)}")
    print(f"All the phone number(s) found: {look_phone_no2(msg2)}")

    print(f"\nMessage 3: {msg3}")
    print(f"All the phone number(s) found: {look_phone_no(msg3)}")
    print(f"All the phone number(s) found: {look_phone_no2(msg3)}")

if __name__ == "__main__":
    main()
