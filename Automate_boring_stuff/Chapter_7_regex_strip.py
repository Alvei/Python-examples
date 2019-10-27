""" Chapter_7_phone_and_email.py
    Use Regex to emulate the string.strip() method.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 177.
"""
import re
import logging
DEBUG = False

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)

def my_strip(text: str, remove: str = '') -> str:
    """ Remove a character from a string. """

    # Start with default. Removes whitespace from either end of the string.
    if remove == '':
        logging.debug("*** %s ***", text)

        # Remove the front spaces, use ^ to insist on starting at beginning
        front_regex = re.compile(r'^\s+')
        front = front_regex.sub("", text)
        logging.debug("*** %s ***", front)

        # Remove the back spaces. \Z means from the end of the string
        back_regex = re.compile(r'\s+\Z')
        ans = back_regex.sub("", front)

        logging.debug("*** %s ***", ans)
        return ans

    # Uses ^ for the beginning and & for the end.
    # The % inside the paranthesis gets replaced with remove
    remove_start = re.compile(r'^([%s]+)' % remove)
    remove_end = re.compile(r'([%s]+)$' % remove)
    start = remove_start.search(text)
    end = remove_end.search(text)

    # Calculate the length of the matched
    start_len = len(start.group())
    end_len = len(end.group())

    logging.debug("Start:" + start.group() + "End:" + end.group())

    # Allows function to strip even if only one side has remove characters
    try:
        return text[start_len:len(text) - end_len]
    except AttributeError:
        # Simply bad the beginning and end with the character to be remove and run again
        error_avoid = remove + text + remove
        return my_strip(error_avoid, remove)


def main():
    """ Test Harness"""

    tests = {"": "   allo c'est moi        ", "#": "####Non c'est toi###"}

    for key, text in tests.items():
        print(f"\nKey:\' {key}\' \tValue:\'{text}\'.")
        orig_len = len(text)
        ans = my_strip(text, key)
        print(f"Length: Original= {orig_len} -> Final= {len(ans)} :{ans}.")


if __name__ == "__main__":
    main()
