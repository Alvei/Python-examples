""" Inspired by David Kopec. """
from enum import Enum
import random
from math import sqrt
from typing import List, NamedTuple, Callable, Optional
from generic_search import dfs, bfs, node_to_path, Node

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

    def goal_test(self, ml: MazeLocation) -> bool:
        """ Checks whether the goal was reached during the search. """
        return ml == self.goal

    def successor(self, ml: MazeLocation) -> List[MazeLocation]:
        """ Find all the possible next locations for a given MazeLocation.
            First check within the maze then check that it is not blocked. """
        locations: List[MazeLocation] = []

        if ml.row + 1 < self._rows and self._grid[ml.row + 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row + 1, ml.column))
        if ml.row - 1 >= 0 and self._grid[ml.row - 1][ml.column] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row - 1, ml.column))

        if ml.column + 1 < self._columns and self._grid[ml.row][ml.column + 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column + 1))
        if ml.column - 1 >= 0 and self._grid[ml.row][ml.column - 1] != Cell.BLOCKED:
            locations.append(MazeLocation(ml.row, ml.column - 1))
        #print(f"=> {locations}")
        return locations

    def mark(self, path: List[MazeLocation]):
        """ Mark the maze with the successful path. """
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

    def clear(self, path: List[MazeLocation]):
        """ Remove a path on a maze. """
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY

        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

if __name__ == "__main__":

    # Test DFS
    m: Maze = Maze()            # Use defaults
    print("\n=> New Maze\n")
    print(m)

    solution1: Optional[Node[MazeLocation]] = dfs(m.start, m.goal_test, m.successor)
    if solution1 is None:
        print("\n => No solution found using DFS.")
    else:
        path1: List[MazeLocation] = node_to_path(solution1)
        m.mark(path1)
        print(m)
        m.clear(path1)

    # BFS
    solution2: Optional[Node[MazeLocation]] = bfs(m.start, m.goal_test, m.successor)

    if solution2 is None:
        print("\n => No solution found in BFS!")
    else:
        path2: List[MazeLocation] = node_to_path(solution2)
        m.mark(path2)
        print(m)
        m.clear(path2)