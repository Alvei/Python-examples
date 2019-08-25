""" Chapter_7_phone_and_email.py
    Use Regex to extract all the NA phone numbers and emails from a file.
    https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch04s02.html
    also Inspired from Automate the Boring Stuff with Python - Al Sweigart. Chapter 6. Page 166.
"""
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

def get_all_phone_no(text, debug=False):
    """ Apply phone_no regex to find all the phone numbers in a string.
        Signature: (str) -> list(str). """
    # By putting the parenthesis in front of each element we get access to each
    phone_regex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?       # Area code
        (\s|-|\.)?               # Separator
        (\d{3})                  # First 3 digits
        (\s|-|\.) ?              # Separator
        (\d{4})                  # Last 4 digits
        )''', re.VERBOSE)
    ans = phone_regex.findall(text)
    if debug == True:
        print("Phone found:", ans)

    # Extra step to extract the 1st item of list which contains the whole phone no. Could also remove parenthesis
    phone_no = []
    for item in ans:
        phone_no.append(item[0])
    # Convert the list of strings to a singular string with each answer separated by an EOL
    return '\n'.join(phone_no)


def get_all_emails(text):
    """ Apply email regex to find all the emails in a string.
        Signature: (str) -> str. """
    # By putting the parenthesis in front of each element we get access to each
    email_regex = re.compile(r'''(
        ([a-zA-Z0-9._%+-]+)     # username
        @                       # @ symbol
        [a-zA-Z0-9.-]+          # domain name
        (\.[a-zA-Z]{2,4})       # dot-something
        )''', re.VERBOSE)
    ans = email_regex.findall(text)

    # Extra step to extract the 1st item of list which contains the whole email. Could also remove parenthesis.
    emails = []
    for item in ans:
        emails.append(item[0])

    # Convert the list of strings to a singular string with each answer separated by an EOL
    return '\n'.join(emails)


def main():
    """ Test harness """
    text = read_file('Chapter_7_input_file.txt', debug=True)
    print("Phone no:\n", get_all_phone_no(text), sep='')
    print("\nEmails:\n", get_all_emails(text), sep='')


if __name__ == "__main__":
    main()
