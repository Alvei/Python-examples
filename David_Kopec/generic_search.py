""" generic_search.py """
from __future__ import annotations
from typing import TypeVar, Iterable, Sequence, Any
from typing_extensions import Protocol   # Need to install this module
from typing import List, Callable, Set, Deque, Dict, Optional, Generic
from heapq import heappush, heappop

T = TypeVar('T')   # Create a generic type

class Stack(Generic[T]):
    """ Define a generic stack class. """

    def __init___(self) -> None:
        """ Initialize. """
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """ Not is true for empty container. """
        return not self._container

    def push(self, item: T) -> None:
        """ Add a Generic item to the stack. LIFO. """
        self._container.append(item)

    def pop(self) -> T:
        """Remove the last Generic item from the stack. LIFO. """
        return self._container.pop()

    def __repr__(self) -> str:
        """ Printing the stack. """
        return repr(self._container)

class Node(Generic[T]):
    """ Will keep track of how we got from one state to the other.
        Node is a wrapper around the state. """

    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0,
                 heuristic: float = 0.0) -> None:
        """ Initialize. """
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        """ Lower than comparator. """
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
