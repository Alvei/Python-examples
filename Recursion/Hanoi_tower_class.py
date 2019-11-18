""" Solve Hanoi Tower using the stack class to represent a tower.
    Generic type hinting enables Stack to be generic over a particular
    type in type hint. The arbitrary type T is defined in T = TypeVar['T'].
    T can be any type.
    Inspired from David Kopec's book Chapter 1. """
from typing import List, TypeVar, Generic
T = TypeVar('T')

class Stack(Generic[T]):
    """ Simple stack class. """
    def __init__(self) -> None:
        """ Initializer. Use private version of container.
            The container is a list where FIFO is appended. """
        self._container: List[T] = []

    def push(self, item: T) -> None:
        """ Push a new item on the stack. """
        self._container.append(item)

    def pop(self) -> T:
        """ Remove the last item in the stack.
            Leverages .pop() method in list. """
        return self._container.pop()

    def __repr__(self) -> str:
        """ repr version required to easily explore the content of Stack. """
        return repr(self._container)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int],
            number: int, move: int) -> None:
    """ Need to do 3 actions:
            Move upper n-1 rings from begin -> temp recursively.
            Move the singular ring from begin -> end. [Base Case]
            Move the n-1 rings from temp -> end. """

    print(f"\t\t{move}\t{number} Begin: {begin}\ttemp: {temp}\tEnd: {end}")
    if number == 1: # Base case
        end.push(begin.pop())
        print(f"Base Case\t{move}\t{number} Begin: {begin}\ttemp: {temp}\tEnd: {end}")
    else:
        # Will go through Begin recursively and finish with a base case to end
        hanoi(begin, temp, end, number - 1, "first")
        hanoi(begin, end, temp, 1, "second")  # Call the Base case to temp
        hanoi(temp, end, begin, number - 1, "third")


if __name__ == "__main__":

    num_discs = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for index in range(1, num_discs + 1):
        tower_a.push(index)


    print("\nStarting position for Tower a", tower_a, "\nProcessing...")
    hanoi(tower_a, tower_c, tower_b, num_discs, "start")
    print("Tower a:", tower_a)
    print("Tower b:",tower_b)
    print("Tower c:",tower_c)
