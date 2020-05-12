""" A Collatz Sequence Program.
    If even number it should print it.
    If odd number if should print it and return 3*number+1
    It should stop if number is one.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Page 77.
"""


def collatz(number: int) -> None:
    """ Collatzs the input number recursively until it reaches 1. """
    if number == 1:
        print('Collatz Complete because found 1!')
    elif number % 2 == 0:
        print(number // 2)
        collatz(number // 2)
    else:
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)


def collatz2(number: int) -> None:
    """Collatz the number and print each step and tracks the number of them. """
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print(number // 2)
                number = number // 2
                steps += 1
            else:
                print(int(number * 3 + 1))
                number = number * 3 + 1
                steps += 1
        print('Collatz sequence finished in ' + str(steps) + ' steps')

    print("Should be greater than one. Start again.")


def yes_or_no(question: str) -> bool:
    """ Ask Y/N question with error checking."""
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False

    return False # This will never be reached but required for pylint, mypy


def main():
    """"Main program"""

    print(" Collatz Sequence Program\n", "#"*25)
    if yes_or_no("Choose to count steps?"):
        try:
            collatz2(int(input('Choose any integer greater than 1: ')))
        except ValueError:
            print('Non-Integer entered, program will exit')
    else:
        try:
            collatz(int(input('Choose any integer greater than 1: ')))
        except ValueError:
            print('Non-Integer entered, program will exit')


if __name__ == '__main__':
    main()
