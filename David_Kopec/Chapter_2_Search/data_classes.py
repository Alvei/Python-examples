""" data_classes.py
    Defines the following generic classes: Stack, Queue, PriorityQueue
"""
#from __future__ import annotations
from typing import TypeVar, Generic
from typing import List, Deque
from heapq import  heappush, heappop
#from typing_extensions import Protocol   # Need to install this module

T = TypeVar('T')   # Create a generic type

class Stack(Generic[T]):
    """ Generic Stack Class implemented using Python’s built-in list type makes
        a decent stack data structure as it supports push and pop operations
        in amortized O(1) time. Python’s lists are implemented as dynamic arrays
        internally which means they occasional need to resize the storage space
        for elements stored in them when elements are added or removed. The list
        over-allocates its backing storage so that not every push or pop requires
        resizing and you get an amortized O(1) time complexity for these operations.

        The deque class implements a double-ended queue that supports adding and
        removing elements from either end in O(1) time (non-amortized).

        Because deques support adding and removing elements from either end equally
        well, they can serve both as queues and as stacks.
        https://dbader.org/blog/stacks-in-python. """
    def __init__(self) -> None:
        """ Initialize a List. """
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """ Returns True for empty container. """
        return not self._container

    def push(self, item: T) -> None:
        """ Add to the end of the stack item(s). """
        self._container.append(item)

    def pop(self) -> T:
        """ Remove the last item in the container. LIFO. """
        return self._container.pop()

    def __repr__(self) -> str:
        """ Use default repr(). """
        return repr(self._container)

    def size(self):
        """ Return the length of the container. """
        return len(self._container)

    def peek(self) -> T:
        """ View element at top of the stack. """
        if self.empty:
            raise Exception("Stack empty!")
        return self._container[-1]

    def show(self) -> List[T]:
        """ Displays the entire stack as a list. """
        return self._container

class Queue(Generic[T]):
    """ Generic Queue class. """
    def __init__(self) -> None:
        """ Initialize a List. """
        self._container: Deque[T] = Deque()

    @property
    def empty(self) -> bool:
        """ Returns True for empty container. """
        return not self._container

    def push(self, item: T) -> None:
        """ Add to the end of the queue item(s). """
        self._container.append(item)

    def pop(self) -> T:
        """ Remove the 1st item in the container. FIFO. """
        return self._container.popleft()

    def size(self):
        """ Return the length of the container. """
        return len(self._container)

    def peek(self) -> T:
        """ View element at top of the stack. """
        if self.empty:
            raise Exception("Queue empty!")
        return self._container[0]

    def show(self) -> Deque[T]:
        """ Displays the entire queue as a list. """
        return self._container

    def __repr__(self) -> str:
        """ Use default repr(). """
        return repr(self._container)

class PriorityQueue(Generic[T]):
    """ Generic Priority Queue class using heaps.
        Only works with uniform List.  ie. not [1, "two", 3]"""
    def __init__(self) -> None:
        """ Initialize a List. """
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """ Returns True for empty container. """
        return not self._container

    def push(self, item: T) -> None:
        """ Add but maintains the heap structure. """
        heappush(self._container, item)

    def pop(self) -> T:
        """ Remove and return the smallest element from heap.
            The order is adjusted, so as heap structure is maintained. """
        return heappop(self._container)

    def size(self):
        """ Return the length of the container. """
        return len(self._container)

    def __repr__(self) -> str:
        """ Use default repr(). """
        return repr(self._container)
