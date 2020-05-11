""" Parse_dates.py
    Check to see if string is a valid date. Return None is not,
    otherwise return a standard date format.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 166.
"""
from datetime import datetime
from typing import Union

def try_parsing_date(text: str, debug: bool = False) -> Union[bool, datetime]:
    """ Find a date in a string. If not possible return False. """

    # Loop through the 3 different ways of representing a date
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass

    # Keepe raise if you want it to fail
    if debug:
        raise ValueError('No valid date format found')
    return False


def main():
    """ Test harness """

    texts = ['2014-05-18', '18.5.2014', '18/05/2019', 'xxx']

    for text in texts:
        print("Date:", try_parsing_date(text, False), sep='')

if __name__ == "__main__":
    main()
