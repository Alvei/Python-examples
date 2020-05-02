""" Simple example of polymorphic function for Python 3.5."""
from typing import Any


def read_val(val_type, request_msg: str, error_msg: str):
    """ Simple polymorphic function to read input with basic exception handling. """

    while True:
        val = input(request_msg)
        # Check if the value type of val is consistent with type of val_type
        try:
            val = val_type(val)
            return val
        except ValueError:
            print(val, error_msg)


def main():
    """ main function """
    val = read_val(int, 'Enter an integer:', 'is not an integer')
    
    print(val)

if __name__ == "__main__":
    main()
