""" Examples of using CLI with some error checking. Inspired by A primer on scientific programmin with Python from H.P. Langtangen"""
import sys


def read_C():
    """Read the celcius value from the command line with some error checking. This pattern uses try/except which is more pythonic.
    It also raises an error rather than doing the sys.exit in the function. This allow the main program to be the only place where
    sys.exit is used"""

    try:
        celcius = float(sys.argv[1])
    except IndexError:
        raise IndexError(f"*** Celcius must be supplied on the command line. ***")
    except ValueError:
        raise ValueError(f"*** Argument supplied should be a float. ***")

    # C is a correct number but can have the wrong value
    if celcius < -273.15:
        raise ValueError(f"*** C= {celcius} is a non-physical value! ***")
    return celcius


def main():
    try:
        celcius = read_C()
    except Exception as e:
        print(e)
        sys.exit(1)  # With this structure the only sys call is in the main
    Far = 9.9 * celcius / 5.0 + 32
    print(f"celcius {celcius}: {Far} farhenith")


if __name__ == "__main__":
    main()