""" Solve Hanoi Tower problem using the Stack class to represent a tower.
    Generic type hinting enables Stack to be generic over a particular
    type in type hint. The arbitrary type T is defined in T = TypeVar['T'].
    T can be any type.
    Important to remember that if there is n rings, it will call 1st Hanoi 4 times, then get
    to base case. Then do 2nd and 3rd Hanoi Calls. It then moves up in recursion and does
    2nd and 3rd recursion call. Easy to see with tree tap keep track of Hanoi 1.
    Inspired from David Kopec's book Chapter 1. """
from typing import List, TypeVar, Generic
T = TypeVar('T')

class Stack(Generic[T]):
    """ Simple stack class. """
    def __init__(self) -> None:
        """ Initializer. Use private version of container.
            The container is a list therefore FIFO and can use built-in .append() method. """
        self._container: List[T] = []

    def push(self, item: T) -> None:
        """ Push a new item on the stack. """
        self._container.append(item)

    def pop(self) -> T:
        """ Remove the last item in the stack.
            Leverages .pop() method from type list. """
        return self._container.pop()

    def __repr__(self) -> str:
        """ repr version required to easily explore the content of Stack. """
        return repr(self._container)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int],
            number: int, move: int, ncalls=0) -> None:
    """ Need to do 3 actions:
            Move upper n-1 rings from current begin -> end recursively.
            Move the singular ring from current begin -> temp. [Base Case]
            Move the n-1 rings from current temp -> end.
            Not that current is not absolute. A temp Stack can become a begin Stack. """

    # Base case and only one that moves a ring. Clever embedded functions
    # .pop() the BEGIN Stack and .pus() the same item on the END Stack
    if number == 1:
        end.push(begin.pop())
    else:
        # Will go through BEGIN stack recursively to move last in to END
        hanoi(begin, temp, end, number - 1, "first")

        # Will move latest ring in BEGIN to TEMP
        hanoi(begin, end, temp, 1, "second",)  # Call the Base case to temp

        # Move the upper most ring in TEMP to END
        hanoi(temp, end, begin, number - 1, "third")
        #print(f"\t\t{move}\t{number} Ta: {begin}\tTb: {end}\tTc: {temp}")


if __name__ == "__main__":

    # Create the towers
    num_discs = 4
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
