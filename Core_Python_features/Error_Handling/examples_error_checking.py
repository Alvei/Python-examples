"""
Created on Mon Dec 29 13:47:08 2014

Simple functions to read input with some error checking.
Note that checking for string does not work since it assume a
number is a string
python 3.x
"""


def yes_or_no(question: str) -> bool:
    """ Ask Y/N question with error checking."""
    while "the answer is invalid":
        reply = str(input(question + ' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def read_int():
    """ Function to ask for integer with basic error handling.
        Signature: (None) -> Int or error."""
    while True:
        val = input('Enter an integer: ')
        try:
            val = int(val)
            return val
        except ValueError:
            print(val, 'is not an integer')


def read_val(val_type, request_msg: str, error_msg: str, max_tries=4):
    """ Function to test the input with error handling
    Input:
        valtype: is the type of value expected (eg., int)
        requestMsg: str defining the input question
        errorMsg: str to be displayed to user when error happens
    """

    num_tries = 0
    while num_tries < max_tries:
        val = input(request_msg)
        try:
            val = val_type(val)
            return val
        except ValueError:  # Handler for the exception
            print(error_msg)
            num_tries += 1

    raise TypeError('Number of tries exceeded')


def temp_convert(var):
    """ Convert to integer. """
    try:
        return int(var)
    except ValueError:
        print("The argument does not contain integers\n")


def main():
    """ Main code - test harness. """
    # read_int()
    print(read_val(int, "Enter int: ", "Not an int."))
    print(read_val(str, "Enter string: ", "Not an string."))

    # temp_convert("xyz");


if __name__ == '__main__':
    main()
