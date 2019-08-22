""" A Collatz Sequence Program.
    If even number it should print it.
    If odd number if should print it and return 3*number+1
    It should stop if number is one.
    Inspired from Automate the Boring Stuff with Python - Al Sweigart. Page 77.
"""


def collatz(number):
    """ Collatzs the input number recursively until it reaches 1.
        Signature: (int) -> None"""
    if number == 1:
        print('Collatz Complete because found 1!')
    elif number % 2 == 0:
        print(int(number / 2))
        collatz(number / 2)
    else:
        print(int(number * 3 + 1))
        collatz(number * 3 + 1)


def collatz2(number):
    """Collatz the number and print each step and tracks the number of them.
       Signature: (int) -> int."""
    if number > 1:
        steps = 0
        while number != 1:
            if number % 2 == 0:
                print(int(number / 2))
                number = number / 2
                steps += 1
            else:
                print(int(number * 3 + 1))
                number = number * 3 + 1
                steps += 1
        print('Collatz sequence finished in ' + str(steps) + ' steps')
    else:
        print("You entered 1. Should be greater than one. Start again.")


def yes_or_no(question):
    """ Ask Y/N question with error checking.
        Signature: (str) -> boolean."""
    while "the answer is invalid":
        reply = str(input(question+' (y/n): ')).lower().strip()
        if reply[:1] == 'y':
            return True
        if reply[:1] == 'n':
            return False


def main():
    """"Main program"""
    
    print(" Collatz Sequence Program\n", "#"*25)
    if yes_or_no("Choose to count steps"):
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