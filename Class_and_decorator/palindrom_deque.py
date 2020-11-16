""" palindrom_deque.py
    https://docs.python.org/2/library/collections.html#collections.deque """
from collections import deque


def ispalindrom(msg: str) -> bool:
    """ Check if the msg is a palindrom. """
    msg = msg.lower()
    # by using iterable in initialization avoid the loop to load it with append
    container = deque(msg)

    # for char in msg:
    #    container.append(char)

    index = len(msg)
    while index > 2:
        lhs = container.popleft()
        rhs = container.pop()

        if lhs != rhs:  # Exit as soon as a mismatch is found
            return False
        index -= 2
    return True  # Default


def main():
    """ Test Harness """
    print(ispalindrom("Laval"))
    print(ispalindrom("Kayak"))
    print(ispalindrom("nothing"))


if __name__ == "__main__":
    main()
