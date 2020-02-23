""" Chap2_generic_search.py
    Different ways of searching. Using generic types not only list
    Linear search with O(n) and binary search with O(nLog(n).
    Binary search requires the list to be ordered.
    The examples are done on Genes. Genes of made of Codons. Codons are 3 Nucleotides.
    Inspired by David Kopec.
    Key dependencies
    __future__ import feature to backport features from other
               higher Python versions to the current interpreter.
    Sequence: Iterable that can be address with indexes/slice: lists, tuples, sets
    TypeVar:  Works with generic to define the type hint.
    Generic
    Deque
    heapq
    Protocol
    """
from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Any, Union
from typing_extensions import Protocol   # Need to install this module
#from typing import List, Callable, Set, Deque, Dict, Optional, Generic
#from heapq import heappush, heappop

T = TypeVar('T')   # Create a generic type

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    """ Generic Linear search. Order O(n). """
    if len(iterable) == 0:  # Makes sure not an empty list
        return False

    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound='Comparable')

class Comparable(Protocol):
    """ Class that uses the Protocol type to define the comparison operators.
        A bit clunky and will likely not be necessary in the next version of Python. """
    def __eq__(self, other: Any) -> bool:
        """ Equal comparator. Uses default. """
        ...
    def __lt__(self: C, other: C) -> bool:
        """ Lower than comparator. Uses default. """
        ...
    def __gt__(self: C, other: C) -> bool:
        """ Greater than comparator. """
        return (not self < other) and self != other
    def __le__(self: C, other: C) -> bool:
        """ Lower or equal than comparator. """
        return self < other or self == other
    def __ge__(self: C, other: C) -> bool:
        """ Greater or equal than comparator. """
        return self < other

def binary_contains(sequence: Sequence[C], key: C) -> Union[bool, int]:
    """ Generic binary search for sequences. Need a type with buit-in comparators.
        Therefore using class C. Assumes sorted list. O(nlog(n)).
        Return -1 if list is not sorted"""

    if len(sequence) == 0:  # Makes sure not an empty sequence
        return  False

    #print("=>", sorted(sequence))
    # Make sure the sequence is sorted
    if not (sequence == sorted(sequence)):
        print(sequence, "=?", sorted(sequence), " => the list is not ordered")
        return -1

    # Pythonic way to check for numbers but does not work for strings
    #all(sequence[i] <= sequence[i+1] for i in range(len(sequence)-1)) )

    low: int = 0
    high: int = len(sequence) - 1
    while low <= high:              # While there is still search space
        mid: int = (low + high) // 2
        if sequence[mid] < key:     # If key is to the right of mid, replace low
            low = mid + 1
        elif sequence[mid] > key:   # If key is to the right of mid, replace high
            high = mid - 1
        else:
            return True             # Found the match
    return False


if __name__ == "__main__":
    my_list = [1, 5, 15, 15, 15, 20]  # must be sorted list
    key = 5
    print(f"\nkey: {key} is in list: {my_list}? {linear_contains(my_list, key)}")
    print(f"key: {key} is in list {my_list}? {binary_contains(my_list, key)}")

    my_list2 = ["M", "a", "b", "e", "z"] # Uppercase come first
    key2 = "M"
    print(f"\nkey: {key2} is in list: {my_list2}? {linear_contains(my_list2, key2)}")
    print(f"key: {key2} is in list {my_list2}? {binary_contains(my_list2, key2)}")

    my_list3 = ["john", "mark", "ronald", "julie", "sarah"]
    key3 = "sheila"
    print(f"\nkey: {key3} is in list: {my_list3}? {linear_contains(my_list3, key3)}")
    print(f"key: {key3} is in list {my_list3}? {binary_contains(my_list3, key3)}")

    my_list4 = [1, 25, 15, 35, 45, 20]
    key4 = 15
    print(f"\nkey: {key} is in list: {my_list4}? {linear_contains(my_list4, key4)}")
    print(f"key: {key} is in list {my_list4}? {binary_contains(my_list4, key4)}")
