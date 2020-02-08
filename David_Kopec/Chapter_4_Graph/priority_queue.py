""" priority_queue.py
    Inspired From Classic Computer Science Problems in Python Chapter 4 by David Kopec. """
from typing import TypeVar, Generic, List
from heapq import heappush, heappop

T = TypeVar('T')

class PriorityQueue(Generic[T]):
    " Priority Queue implementation. "
    def __init__(self) -> None:
        """ Initialize the container as a List. """
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """ Check if the queue is empty. """
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        """ Enter an new item by priority. """
        heappush(self._container, item)

    def pop(self) -> T:
        """ Out by priority. """
        return heappop(self._container)

    def __repr__(self) -> str:
        """ Print the queue. """
        return repr(self._container)