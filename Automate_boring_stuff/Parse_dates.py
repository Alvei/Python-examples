""" Parse_dates.py
    Check to see if string is a valid date. Return None is not,
    otherwise return a standard date format.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 166.
"""
from datetime import datetime
import re
from os.path import dirname, join
from typing import Union

def read_file(file_name: str, debug: bool = False) -> str:
    """ Read a file and return a long string while doing some basic error checking. """

    # Find the location of the current directory. Assumes the text file is in the same directory
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    with open(file_path, 'rt') as in_file:
        try:
            # Read the entire file into a string variable
            contents = in_file.read()
            if debug:
                print("Original file:\n", contents, '\n', sep="")
            return contents
        except IOError:
            print(f"Unable to load {file_path} Check that it exists.")
            return "IOError"


def try_parsing_date(text: str, debug: bool = False) -> Union[str, bool, datetime]:
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
