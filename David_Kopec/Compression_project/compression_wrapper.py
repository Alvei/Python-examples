
""" Inspired by
    https://github.com/KGB33/ClassicComputerScienceProblems/blob/master/1_SmallProblems/Exercises.py
"""
from math import log2, ceil
from sys import getsizeof
from typing import List

class BitStringCompression:
    """ Wrapper class. """
    def __init__(self, string: str) -> None:
        """ Initialize. """
        self.data = string
        self.incr = 0

    def __str__(self) -> str:
        """ Printing class. """
        return self.data

    def __iter__(self):
        """ Iterator. """
        self.incr = 0
        return self

    def __next__(self):
        """ Increment by one. """
        # for i in range(0, self._data.bit_length() - 1, self._shift):  # -1 to exclude sentinal Val
        bits = self._data >> self.incr & (pow(2, self._shift) - 1)  # gets 2 bits at a time

        # Get the character for the specific bit
        gene = self._unique_parts[bits]
        self.incr += self._shift
        if self.incr >= self._data.bit_length():
            raise StopIteration
        return gene

    @property
    def data(self) -> str:
        """ Define the getter method. """
        gene = ''
        for index in range(0, self._data.bit_length() - 1, self._shift):  # -1 to exclude sentinel
            bits = self._data >> index & (pow(2, self._shift) - 1)  # gets 2 bits at a time
            gene += self._unique_parts[bits]

        return gene[::-1]                    # [::-1] reverses the string by slicing backwards

    @data.setter
    def data(self, val: str) -> None:
        """ Define the setter method. """

        # Unpact the string and create a list of unique characters, the use of {} creates set
        self._unique_parts: List[str] = list({x for x in val})

        # Calculate the number of bits to store the unique characters
        # with 8 characters, log2(2^3) = 3. That becomes the number of shifts
        self._shift: int = ceil(log2(len(self._unique_parts)))

        bit_string: int = 1  # start with a sentinel

        # Iterate through all the characters
        for part in val:
            bit_string <<= self._shift
            # Very clever pattern.
            # Uses the index of the character in ._unique_parts which is a class variable
            bit_string |= self._unique_parts.index(part)

        # Save in the class as a compressed string
        self._data = bit_string

def exercise_2():
    """ Generic example of compressing class from string to bits.
    Using nucleotides example which takes two bites because 4 letters can be represented with that.
    Should adjust based on the number of letters we need to map.
    Inspired by David Kopec's book.  """

    original = 'ABCDEFGH' * 1
    print(f'Original is {getsizeof(original)} Bytes')
    compressed = BitStringCompression(original)
    print(f'Compressed is {getsizeof(compressed._data)} Bytes')
    print(f'Original and Compressed are the same: {original == compressed.data}')
    print('Iteration:')
    for _, letter in enumerate(compressed):
        print(letter, end="")

if __name__ == "__main__":
    exercise_2()
