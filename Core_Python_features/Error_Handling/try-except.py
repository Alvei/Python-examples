""" Example of two functions to add dictionary. If the key does not exist, the function returns None.
"""


def add(values: dict) -> dict:
    """Look Before You Leap (LBYL) is not idiomatic.
    The code asks every time, although not having the keys is the exception, not the rule!"""
    if "X" in values and "Y" in values:
        x = values["X"]
        y = values["Y"]
        return x + y
    return None


def add2(values: dict) -> dict:
    """We recognize that X and Y should always be present in dictionary and not finding is exception.
    Easier to Ask for Forgiveness than Permission (EAFP). In Python, exceptions are cheap."""
    try:
        x = values["X"]
        y = values["Y"]
    except KeyError:
        return None
    else:
        return x + y


def read_file():
    try:
        file = open("test.txt", "rb")
    except (IOError, EOFError) as e:
        print("An error occurred. {}".format(e.args[-1]))


def read_file2():
    try:
        file = open("test.txt", "rb")
    except EOFError as e:
        print("An EOF error occurred.")
        raise e
    except IOError as e:
        print("An error occurred.")
        raise e


if __name__ == "__main__":
    my_dict = {"X": 5, "Y": 2}

    print(add(my_dict))
    read_file()  # This is cleaner erro message than read_file2()
    # read_file2()
