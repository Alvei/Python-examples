""" contain_searches.py
    Two functions that searches for presence of an element in a list.
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
"""
#from __future__ import annotations
from typing import TypeVar
from typing import Iterable, Sequence, Any, Union
#from typing import Protocol   # Need to install this module

T = TypeVar('T')   # Create a generic type

def linear_contains(iterable: Iterable[T], key: T) -> bool:
    """ Generic Linear search. Order O(n). """

    # Makes sure not an empty . But iterable do not have len() function
    #if len(iterable) == 0:
        #return False

    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar("C", bound='Comparable')

#class Comparable():
class Comparable():
    """ Class that uses the Protocol type to define the comparison operators.
        A bit clunky and will likely not be necessary in the next version of Python.
        It assumes that all elements of list are the same. E.g., str < int does not work. """
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

def binary_contains(sequence: Sequence[C], key: C) -> Union[int, bool]:
    """ Generic binary search for sequences. Need a type with buit-in comparators.
        Therefore using class C. Assumes sorted list. O(nlog(n)).
        Returns -1 if sequence is not ordered. """

    if len(sequence) == 0:  # Makes sure not an empty sequence
        return False

    # Make sure the sequence is sorted
    if not sequence == sorted(sequence):
        #print(sequence, "=?", sorted(sequence))
        return -1

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
