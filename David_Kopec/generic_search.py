""" generic_search.py """
from __future__ import annotations
from typing import TypeVar, Generic
from typing import List, Callable, Set, Optional
#from typing import Iterable, Sequence, Any
from typing import Deque, Dict
from heapq import heappush, heappop
from typing_extensions import Protocol   # Need to install this module

T = TypeVar('T')   # Create a generic type

class Stack(Generic[T]):
    """ Generic Stack class implemented using a list. """
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

    def __repr__(self) -> str:
        """ Use default repr(). """
        return repr(self._container)

class PriorityQueue(Generic[T]):
    """ Generic Priority Queue class. """
    def __init__(self) -> None:
        """ Initialize a List. """
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        """ Returns True for empty container. """
        return not self._container

    def push(self, item: T) -> None:
        """ Add to the end of the priority queue item(s). """
        heappush(self._container, item)

    def pop(self) -> T:
        """ Remove the 1st item in the container. FIFO. """
        return heappop(self._container)

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

    def __str__(self) -> str:
        """ printing. """
        return (f"state: {self.state} parent: {self.parent}")

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

    print(frontier)
    # Keep going while there is more to explore
    while not frontier.empty:

        # The 1st time, .pop() the starting Node, the other time, list
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

            # Load the stack with the current options -> child
            # and keep track of parent -> current_node
            frontier.push(Node(child, current_node))

    return None     # Went through everything and never found goal

def bfs(initial: T, goal_test: Callable[[T], bool],
        successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    """ Breadth-First-Search algorithm. Uses Queue Data element.
        initial: starting point for search.
        goal_test: simple comparison fonction with input type T that returns a bool.
        successors: function that returns a List[T] of all potential next steps or returns None. """

    frontier: Queue[Node[T]] = Queue()      # Were we have yet to go of type Node[T]
    frontier.push(Node(initial, None))      # Load-up the frontier with starting Node
    explored: Set[T] = {initial}            # Where we have been. Use set to avoid duplication

    print(f"Starting: {frontier}")
    # Keep going while there is more to explore
    while not frontier.empty:

        # The 1st time, .pop() the starting Node, the other time, list
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

            # Load the stack with the current options -> child
            # and keep track of parent -> current_node
            frontier.push(Node(child, current_node))

    return None     # Went through everything and never found goal

def astar(initial: T, goal_test: Callable[[T], bool],
          successors: Callable[[T], List[T]],
          heuristic: Callable[[T], float]) -> Optional[Node[T]]:
    """ A*star algorithm. Uses Queue Data element.
        initial: starting point for search.
        goal_test: simple comparison fonction with input type T that returns a bool.
        successors: function that returns a List[T] of all potential next steps or returns None. """

    frontier: PriorityQueue[Node[T]] = PriorityQueue()  # Were we have yet to go of type Node[T]
    frontier.push(Node(initial, None))                  # Load-up the frontier with starting Node
    explored: Dict[T, float] = {initial: 0.0}           # Use Dict to keep track of cost function

    print(f"Starting: {frontier}")
    # Keep going while there is more to explore
    while not frontier.empty:

        # The 1st time, .pop() the starting Node, the other time, list
        current_node: Node[T] = frontier.pop()
        current_state: T = current_node.state

        # If we found the goal, we are done!
        if goal_test(current_state):
            return current_node

        # Check where we can go next and have not explored
        for child in successors(current_state):
            new_cost: float = current_node.cost + 1 # Assumes a grid. Could make more complicated
            if child in explored: # Skip the children we already explored
                continue

            # Keep cost of current child to the list of visited Nodes
            explored[child] = new_cost

            # Load the stack with the current options -> child
            # and keep track of parent -> current_node
            frontier.push(Node(child, current_node, new_cost, heuristic(child)))

    return None     # Went through everything and never found goal
