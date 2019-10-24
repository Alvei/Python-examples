""" Simple example of polymorphic function
    for Python 3.5."""


def read_val(val_type, request_msg, error_msg):
    """ Simple polymorphic function to read input
        and do some basic exception handling.
        Signature: (type, string, string)-> None."""
    while True:
        val = input(request_msg + ' ')

        # Check if the value type of val is consistent with type of val_type
        try:
            val = val_type(val)
            return val
        except ValueError:
            print(val, error_msg)

# Test


def main():
    """ main function """
    val = read_val(int, 'Enter an integer:', 'is not an integer')
    print(val)


main()
