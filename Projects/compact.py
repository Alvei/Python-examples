""" compaq.py
    Accepts a sequence (e.g., lists, strings, tuples) and returns a new iterable
    anything you can loop over) with adjacent duplicate values removed.
    A sequence is a subset of iterables that can be access with indexing.

    For the first bonus, make sure you accept any iterable as an argument,
    not just a sequence (which means you can't use index look-ups in your answer).

    As a second bonus, make sure you return an iterator from your compact function instead of a list.
    This should allow your compact function to accept infinitely long iterables (or other lazy iterables).
    Inspired by python morsels. """

# Make an iterator that returns consecutive keys and groups from the iterable.
from itertools import groupby
from typing import Iterable, Iterator, Sequence, Any

def compact(seq: Sequence[Any]) -> Iterable[Any]:
    """ Removes duplicate of a sequence. """
    # Make sure it is a sequence. Find out what type of sequence
    assert isiterable(seq)
    return iter([k for k,_ in groupby(seq)])

def compact_index(seq: Sequence[Any]) -> Iterable[Any]:
    """ Removes duplicate of a sequence. """
    # Make sure it is a sequence. Find out what type of sequence
    assert isiterable(seq)
    seq_type = type(seq)
    new_seq = list(seq)
    prev = None
    #new_iter = [] # Use item initially but convert later to the right iterable
    list_to_remove = []
    for index, item in enumerate(new_seq):
        if item == prev:
            list_to_remove.append(index)
        else:
            prev = item

    # Reverse the list to start from the end
    list_to_remove = list_to_remove[::-1]
    for item in list_to_remove:
        del new_seq[item]
    return new_seq

def isiterable(obj) -> bool:
    """ Checks if object is iterable or not. """
    try:            # Tries to create an iterator using obj. Only works if iterable
        iter(obj)
        return True
    except TypeError:
        return False

if __name__ == "__main__":
    initial = [1, 1, 2, 3, 3, 3, 4]
    print(f"{initial} ? {list(compact(initial))}")
    initial = "Sasskatoon"
    print(f"{initial} ? {list(compact(initial))}")
    initial = (1, 2, 3, 3, 3, 3, 3, 8)
    print(f"{initial} ? {list(compact(initial))}")
    initial = [n**2 for n in [1, 2, 2]]
    print(f"{initial} ? {list(compact(initial))}")
    initial = (n**2 for n in [1, 2, 3])
    print(f"{[1, 4, 9]} ? {list(compact(initial))}")
