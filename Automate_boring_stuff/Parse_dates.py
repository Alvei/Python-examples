""" Parse_dates.py
    Check to see if string is a valid date. Return None is not, otherwise return a standard date format.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 166.
"""
from datetime import datetime
import re
from os.path import dirname, join


def read_file(file_name, debug=False):
    """ Read a file and return a long string while doing some basic error checking
        Signature: (str, str) -> str."""

    # Find the location of the current directory. Assumes the text file is in the same directory
    current_dir = dirname(__file__)
    file_path = join(current_dir, "./", file_name)

    with open (file_path, 'rt') as in_file:
        try:
            # Read the entire file into a string variable
            contents = in_file.read()
            if debug == True:
                print("Original file:\n", contents, '\n', sep="")
            return contents
        except IOError:
            print('Unable to load "%s".  Check that it exists.' % file_path)
            return


def try_parsing_date(text, debug=False):
    """ Signature: (str) -> str. """
    for fmt in ('%Y-%m-%d', '%d.%m.%Y', '%d/%m/%Y'):
        try:
            return datetime.strptime(text, fmt)
        except ValueError:
            pass

    # Keepe raise if you want it to fail
    if debug == True:
        raise ValueError('no valid date format found')
    return None


def main():
    """ Test harness """

    texts = ['2014-05-18', '18.5.2014', '18/05/2019', 'xxx']

    for text in texts:
        print("Date:", try_parsing_date(text, False), sep='')

if __name__ == "__main__":
    main()
