
#from ProfilerTools import Timer
from functools import lru_cache
from math import log2, ceil
#from generic_search import Stack

"""@Timer(message='Better_Fib', unit='us')
def call_better_fib(index):
    return better_fib(index)

@Timer(message='Normal Fib', unit='us')
def call_normal_fib(index):
    return fib_5(index)"""


"""
Ex. 2
Int Wrapper for compression
"""

class BitStringCompression:

    def __init__(self, string):
        self.data = string

    def __str__(self):
        return self.data

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        # for i in range(0, self._data.bit_length() - 1, self._shift):  # -1 to exclude sentinal Val
        print(f" Next {self.i}")
        bits = self._data >> self.i & (pow(2, self._shift) - 1)  # gets 2 bits at a time
        g = self._unique_parts[bits]
        self.i += self._shift
        if self.i >= self._data.bit_length():
            raise StopIteration
        return g

    @property
    def data(self):
        g = ''
        print("Shift", self._shift)
        for i in range(0, self._data.bit_length() - 1, self._shift):  # -1 to exclude sentinal Val
            bits = self._data >> i & (pow(2, self._shift) - 1)  # gets 2 bits at a time
            print(bits, end= " ")
            g += self._unique_parts[bits]
        print("done\n")
        return g[::-1]  # [::-1] reverses the string by slicing backwards

    @data.setter
    def data(self, val):
        self._unique_parts = list({x for x in val})

        self._shift = ceil(log2(len(self._unique_parts)))
        bit_string = 1  # start with a sentinel
        for part in val:
            bit_string <<= self._shift
            bit_string |= self._unique_parts.index(part)
        self._data = bit_string


def exercise_2():
    from sys import getsizeof
    original = 'ABCDEFGH' * 1
    print(f'Original is {getsizeof(original)} Bytes')
    compressed = BitStringCompression(original)
    print(f'Compressed is {getsizeof(compressed._data)} Bytes')
    print(f'Original and Compressed are the same: {original == compressed.data}')
    print('Iteration:')
    #for i, letter in enumerate(compressed):
    #    print(letter, end="")


"""
Exercise 3
Powers of Hanoi with N-towers \

def hanoi(begin, end, temp, n):
    if n == 1:
        end.push(begin.pop())
    else:
        hanoi(begin, temp, end, n - 1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n - 1)


def exercise_3():
    num_disks = 10
    tower_a = Stack()
    tower_b = Stack()
    tower_c = Stack()
    for i in range(1, num_disks + 1):
        tower_a.push(i)

    print(f'Tower A: {tower_a}')
    print(f'Tower B: {tower_b}')
    print(f'Tower C: {tower_c}')
    print(f'Switch Towers')
    hanoi(tower_a, tower_c, tower_b, num_disks)
    print(f'Tower A: {tower_a}')
    print(f'Tower B: {tower_b}')
    print(f'Tower C: {tower_c}')

"""
if __name__ == '__main__':

    exercise_2()
    #exercise_3()
