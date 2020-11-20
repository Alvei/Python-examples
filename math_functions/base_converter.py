""" base_converter.py
    Flexible implementation that leverages Stack() object."""


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        """ O(1). """
        self.items.append(item)

    def pop(self):
        """ O(1). """
        return self.items.pop()

    def peek(self):
        """ O(1). """
        return self.items[len(self.items) - 1]

    def size(self):
        """ O(1). """
        return len(self.items)

    def __str__(self):
        """ Need to convert the list of integer to string. """
        ans = ""
        for char in self.items:
            ans += str(char)
        return ans


def base_converter(dec_number: int, base: int) -> str:
    """ Converter a number into any base. """
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base
    # print(rem_stack)

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


def main():
    """ Test Harness. """
    test_cases = [
        (10, 2, "1010"),
        (80, 2, "1010000"),
        (25, 2, "11001"),
        (25, 16, "19"),
        (250, 16, "FA"),
        (1968, 16, "7B0"),
    ]

    for number, base, expected in test_cases:
        print(
            f" Number: {number}, base: {base} = {base_converter(number, base)} ? {expected}"
        )


if __name__ == "__main__":
    main()
