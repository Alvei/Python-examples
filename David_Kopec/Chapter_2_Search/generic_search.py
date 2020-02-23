""" generic_search.py """
from __future__ import annotations
from typing import TypeVar, Generic
from typing import List, Callable, Set, Optional
from typing import Iterable, Sequence, Any, Union
from typing import Deque, Dict
from heapq import heappush, heappop
from typing_extensions import Protocol   # Need to install this module

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

def binary_contains(sequence: Sequence[C], key: C) -> Union[int, bool]:
    """ Generic binary search for sequences. Need a type with buit-in comparators.
        Therefore using class C. Assumes sorted list. O(nlog(n)).
        Returns -1 if sequence is not ordered"""

    if len(sequence) == 0:  # Makes sure not an empty sequence
        return False

    # Make sure the sequence is sorted

    if not (sequence == sorted(sequence)):
        print(sequence, "=?", sorted(sequence))
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

    def show(self) -> List[T]:
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

class Node(Generic[T]):
    """ Will keep track of how we got from one state to the other (or one place to another).
        Node is a wrapper around the state. """

    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0,
                 heuristic: float = 0.0) -> None:
        """ Initializes Node().
            state: Current state or current place.
            parent: The previous Node or None.
            cost: Used in the comparison operator used in *A search - priority queue
            heuristic: Used in the comparison operator used in *A search. """
        self.state: T = state
        self.parent: Optional[Node] = parent
        self.cost: float = cost
        self.heuristic: float = heuristic

    def __lt__(self, other: Node) -> bool:
        """ Lower than comparator that is needed for priority queue
            and heappop() and heappush() in particular. """
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __repr__(self) -> str:
        """ printing. """
        #return (f"state: {self.state} parent: {self.parent}")
        return f"s: {self.state} p: {self.parent}"

def node_to_path(node: Node[T]) -> List[T]:
    """ Helps keep track of the path pursued. """
    path: List[T] = [node.state]

    # Work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path

def dfs(initial: T, goal_test: Callable[[T], bool],
        successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    """ Depth-First-Search algorithm. Uses Stack Data element.
        initial: starting point for search.
        goal_test: simple comparison fonction with input type T that returns a bool.
        successors: function that returns a List[T] of all potential next steps or returns None. """

    frontier: Stack[Node[T]] = Stack()      # Were we have yet to go of type Node[T]
    frontier.push(Node(initial, None))      # Load-up the frontier with starting Node
    explored: Set[T] = {initial}            # Where we have been. Use set to avoid duplication

    # Keep going while there is more to explore, counter will keep track of all attempts
    counter = 0

    # Use the empty method to check if stack is empty
    while not frontier.empty:

        # Assign the latest frontier node to current_node. That Node is a linked list
        # Current node will eventually become the final path.
        # The first time, it is equal to the initial. It is possible that there is no
        # successors for that Node, it will then simply .pop() another one  from the stack
        current_node: Node[T] = frontier.pop()

        # Assign current_node to the current_state
        current_state: T = current_node.state

        # print(f"count {counter}: {current_node}")

        # We are done? by checking the goal_test() function
        if goal_test(current_state):
            # current_node is the linked-list of all Nodes that created the path
            return current_node

        # Check where we can go next and have not explored. e.g. successors return up to 4 in Maze
        for child in successors(current_state):
            if child in explored: # Skip the children we already explored
                continue

            # Use the set.add() method to add the current child to the list of visited Nodes
            explored.add(child)

            # Add to the frontier with the current (child, parent)
            # Parent is also a Node with (state, parent) -> linked-list
            frontier.push(Node(child, current_node))
        counter += 1
    return None     # Went through everything and never found goal

def bfs(initial: T, goal_test: Callable[[T], bool],
        successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    """ Breadth-First-Search algorithm. Uses Queue Data element.
        initial: starting point for search.
        goal_test: simple comparison fonction with input type T that returns a bool.
        successors: function that returns a List[T] of all potential next steps or returns None.
        https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
        There’s a great news about BFS: it’s complete. That’s because this algorithm is always able to find
        a solution to a problem, if there is one. Completeness is a nice-to-have feature for an algorithm,
        but in case of BFS it comes to a high cost. The time complexity of the algorithm is exponential.
        Lesson learned: You should use BFS only for relatively small problems. """

    # Missing a check that initial is in the solution set of successor

    frontier: Queue[Node[T]] = Queue()      # Were we have yet to go of type Node[T]
    frontier.push(Node(initial, None))      # Load-up the frontier with starting Node
    explored: Set[T] = {initial}            # Where we have been. Use set to avoid duplication

    # Keep going while there is more to explore
    while not frontier.empty:

        # Assign the latest frontier node to current_node. That Node is a linked list
        # Current node will eventually become the final path.
        # The first time, it is equal to initial. It is possible that there is no
        # successors for that Node, it will then simply .pop() another one  from the queue
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # If we found the goal, we are done!
        if goal_test(current_state):
            return current_node

        # Check where we can go next and have not explored
        for child in successors(current_state):
            if child in explored: # Skip the children we already explored
                continue

            # Use the .add() method from set to the current child to the list of visited Nodes
            explored.add(child)

            # Load the queue with the current options -> child
            # and keep track of parent -> current_node
            frontier.push(Node(child, current_node))

    return None     # Went through everything and never found goal

def astar(initial: T, goal_test: Callable[[T], bool],
          successors: Callable[[T], List[T]],
          heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    """ A*star algorithm. Uses PriorityQueue Data element.
        initial: starting point for search.
        goal_test: simple comparison fonction with input type T that returns a bool.
        successors: function that returns a List[T] of all potential next steps or returns None.
        explored: not a Set[] but a Dict[] to keep track of cost function also. """

    frontier: PriorityQueue[Node[T]] = PriorityQueue()  # Were we have yet to go of type Node[T]
    frontier.push(Node(initial, None))                  # Load-up the frontier with starting Node
    explored: Dict[T, float] = {initial: 0.0}           # Use Dict to keep track of cost function

    # Keep going while there is more to explore
    while not frontier.empty:

        # Assign the latest frontier node to current_node. That Node is a linked list
        # Current node will eventually become the final path.
        # The first time, it is equal to the initial. It is possible that there is no
        # successors for that Node, it will then simply .pop() another one  from the queue
        # Main difference is .pop() is implemented to look at the cost function
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # If we found the goal, we are done!
        if goal_test(current_state):
            return current_node

        # Check where we can go next and have not explored
        for child in successors(current_state):

            new_cost: float = current_node.cost + 1 # Assumes a grid for this cost function
            if child in explored: # Skip the children we already explored
                continue

            # Keep cost of current child to the list of visited Nodes
            explored[child] = new_cost

            # Load the PriorityQueue with the current (child, parent, cost, heuristic)
            frontier.push(Node(child, current_node, new_cost, heuristic(child)))

    return None     # Went through everything and never found goal
