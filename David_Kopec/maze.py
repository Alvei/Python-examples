""" Inspired by David Kopec. KGB33 """
from enum import Enum
import random
from math import sqrt
from typing import List, NamedTuple, Callable, Optional
from generic_search import dfs, bfs, node_to_path, astar, Node

class Cell(str, Enum):
    """ Defined the different states each cell can have. """
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    """ Refer to individual location in the maze.
        By using NamedTuple vs. Tuple we can access by.attribute vs. index.
        start.row rather than start[0]. """
    row: int
    column: int

   # def __str__(self) -> str:
   #     return f"{self.row}, {self.column}"

class Maze:
    """ Defines a Maze. Note all variables are private except start. """
    def __init__(self, rows: int = 10, columns: int = 10, sparseness: float = 0.2,
                 start: MazeLocation = MazeLocation(0, 0),
                 goal: MazeLocation = MazeLocation(9, 9)) -> None:

        # Initialize basic instance variables
        self._rows: int = rows
        self._columns: int = columns
        self.start: MazeLocation = start
        self.goal: MazeLocation = goal

        # Fill the grid with empty cells. 1st list are rows
        self._grid: List[List[Cell]] = [
            [Cell.EMPTY for c in range(columns)]
            for r in range(rows)
        ]

        # Populate the grid with blocked cells
        self._randomly_fill(rows, columns, sparseness)

        # Fill the start and goal locations
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL

    def _randomly_fill(self, rows: int, columns: int, sparseness: float):
        """ Populate the grid with blocked cells. """
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0, 1.0) < sparseness:
                    self._grid[row][column] = Cell.BLOCKED

    def __str__(self) -> str:
        """ Return a nicely formatted version of the maze for printing. """
        output: str = ""
        # First list are for rows
        for row in self._grid:
            # List comprehension across the columns. attribue value is for NamedTuple
            output += "".join([c.value for c in row]) + "\n"
        return output

    def goal_test(self, mloc: MazeLocation) -> bool:
        """ Checks whether the goal was reached during the search. """
        return mloc == self.goal

    def successor(self, mloc: MazeLocation) -> List[MazeLocation]:
        """ Find all the possible next locations for a given MazeLocation.
            First check within the maze then check that it is not blocked. """
        locations: List[MazeLocation] = []

        if mloc.row + 1 < self._rows and self._grid[mloc.row + 1][mloc.column] != Cell.BLOCKED:
            locations.append(MazeLocation(mloc.row + 1, mloc.column))
        if mloc.row - 1 >= 0 and self._grid[mloc.row - 1][mloc.column] != Cell.BLOCKED:
            locations.append(MazeLocation(mloc.row - 1, mloc.column))

        if mloc.column + 1 < self._columns and self._grid[mloc.row][mloc.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(mloc.row, mloc.column + 1))
        if mloc.column - 1 >= 0 and self._grid[mloc.row][mloc.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(mloc.row, mloc.column - 1))
        #print(f"=> {locations}")
        return locations

    def mark(self, path: List[MazeLocation], clear=False):
        """ Mark the maze with the successful path.
            If clear is True, remove the path on the maze. """
        fill = Cell.PATH    # Default is to fill a path
        if clear:           # Overwrite if we need to clear
            fill = Cell.EMPTY

        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = fill

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

def euclidean_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    """ Wrapper function that passes the goal that is a permanent MazeLocation. """
    def distance(mloc: MazeLocation) -> float:
        """ Function that does all the work and permanently knows the goal.
            Uses Pythagorean theorem. """
        xdist: int = mloc.column - goal.column
        ydist: int = mloc.row - goal.row
        return sqrt((xdist * xdist) + (ydist * ydist))
    return distance

def manhattan_distance(goal: MazeLocation) -> Callable[[MazeLocation], float]:
    """ Wrapper function that passes the goal that is a permanent MazeLocation. """
    def distance(mloc: MazeLocation) -> float:
        """ Function that does all the work and permanently knows the goal.
            Uses a simplifying assumption that we have square grid. """
        xdist: int = mloc.column - goal.column
        ydist: int = mloc.row - goal.row
        return xdist + ydist
    return distance

if __name__ == "__main__":
    m: Maze = Maze()            # Use defaults
    print(m)

    # Test DFS
    solution1: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successor)
    if solution1 is None:
        print("\n => No solution found using DFS.")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        print(f"DFS Path Length: {len(path1)}")
        m.mark(path1, clear=True)

    # BFS
    solution2: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successor)

    if solution2 is None:
        print("\n => No solution found in BFS!")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        m.mark(path2)
        print(m)
        print(f"BFS Path Length: {len(path2)}")
        m.mark(path2, clear=True)

    # A*
    dist: Callable[[MazeLocation], float] = manhattan_distance(m.goal)
    solution3: Optional[Node[MazeLocation]] = astar(m.start, m.goal_test,
                                                    m.successor, dist)

    if solution3 is None:
        print("\n => No solution found in A*!")
    else:
        path3: List[MazeLocation] = node_to_path(solution3)
        m.mark(path3)
        print(m)
        print(f"A* Path Length: {len(path3)}")
        m.mark(path3, clear=True)
