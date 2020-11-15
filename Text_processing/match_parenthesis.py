""" check for matching strings
"""
import sys
from typing import TypeVar, Generic, List

T = TypeVar("T")  # Create a generic type


class Stack(Generic[T]):
    """Generic Stack Class implemented using Python’s built-in list type makes
    a decent stack data structure as it supports push and pop operations
    in amortized O(1) time. Python’s lists are implemented as dynamic arrays
    internally which means they occasional need to resize the storage space
    for elements stored in them when elements are added or removed. The list
    over-allocates its backing storage so that not every push or pop requires
    resizing and you get O(1) time complexity for these operations.

    The deque class implements a double-ended queue that supports adding and
    removing elements from either end in O(1) time (non-amortized).

    Because deques support adding and removing elements from either end equally
    well, they can serve both as queues and as stacks.
    https://dbader.org/blog/stacks-in-python."""

    def __init__(self) -> None:
        """ Initialize a List. """
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """Returns True for empty container.
        Chose to implement as property vs. function. O(1)."""
        return not self._container

    def push(self, item: T) -> None:
        """ Add to the end of the stack item(s). O(1). """
        self._container.append(item)

    def pop(self) -> T:
        """ Remove the last item in the container. LIFO. O(1). """
        if self.empty:
            raise Exception("Stack empty! Cannot use .pop()")
        return self._container.pop()

    def __repr__(self) -> str:
        """ Use default repr(). """
        return repr(self._container)

    def size(self):
        """ Return the length of the container. O(1). Const time. """
        return len(self._container)

    def peek(self) -> T:
        """ View element at top of the stack. O(1). """
        if self.empty:
            raise Exception("Stack empty! Cannot use .peek()")
        return self._container[-1]

    def show(self) -> List[T]:
        """ Displays the entire stack as a list. """
        return self._container


def match_symbols(msg: str) -> bool:
    """ Works for known opening/closing pair. """
    symbol_pairs = {"(": ")", "[": "]", "{": "}"}

    openers = symbol_pairs.keys()
    closers = symbol_pairs.values()
    my_stack = Stack()

    for char in msg:
        if char in openers:  # Opening char added to stack
            my_stack.push(char)
        elif char in closers:
            if my_stack.empty:  # If nothing to close then mismatch
                return False
            top = my_stack.pop()
            if char != symbol_pairs[top]:  # Do opening and closing char match
                return False
        else:
            pass

    if my_stack.empty:  # when loop is done then we have match all parenthesis
        return True

    return False  # Default behavior


def main(msg):
    """ Test Harness. """

    print(match_symbols(msg))


if __name__ == "__main__":
    main(sys.argv[1])
