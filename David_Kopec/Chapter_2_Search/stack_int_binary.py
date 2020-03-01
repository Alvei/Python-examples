""" stack_int_binary.py
    Convert an integer to binary using stack.
    Uses divide by two.
    example: 242
        242/2 = 121 => remainder 0  Bottom of stack
        121/2 = 60  => remainder 1
        60/2 = 30   => remainder 0
        30/2 = 15   => remainder 0
        15/2 = 7    => remainder 1
        7/2 = 3     => remainder 1
        3/2 = 1     => remainder 1  Top of stack
        can check int(1110010, 2) = 242"""
from data_classes import Stack

def stack_int_to_binary(dec_num)-> str:
    """ convert an integer to binary.
        dec_num needs to be greater than zero"""

    assert dec_num > 0, f"dec_num = {dec_num} needs to be greater than zero"
    binary_stack = Stack()

    while dec_num > 0:
        remainder = dec_num % 2
        binary_stack.push(remainder)
        dec_num = dec_num // 2      # // is a floor division

    bin_num = ""
    while not binary_stack.empty:
        bin_num += str(binary_stack.pop())

    return bin_num

if __name__ == "__main__":
    tests = [242, 8, 2, 0, -1]
    for test in tests:
        print(f"{test} is {stack_int_to_binary(test)}")


