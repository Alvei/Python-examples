""" circuit_board_layout.py
    Grid which represent a circuit board.
    Variables are the NxM rectangles while the locations are the domains.
    Current problem does not include overlapping rectangles.
    From Classic Computer Science Problems in Python Chapter 3 by David Kopec. """

from typing import NamedTuple, List, Dict, Optional
from random import choice
from string import ascii_uppercase
from csp import CSP, Constraint

Grid = List[List[str]]  # Type alias for grids

class GridLocation(NamedTuple):
    """ Like our maze problem, NamedTupled takes advantage of row and column naming. """
    row: int
    column: int

def generate_grid(rows: int, columns: int) -> Grid:
    """ Initializes/fills the grid with x. """
    assert columns > 0
    assert rows > 0
    return [["x"
            for c in range(columns)]
            for r in range(rows)
           ]

def display_grid(grid: Grid) -> None:
    """ Displays the grid of letters. Grid is an alias of List[List[str]].
        Therefore .join(row) merges a list of characters. """
    for row in grid:
        print("".join(row))

def generate_domain(part: tuple, grid: Grid) -> List[List[GridLocation]]:
    """ Chips/rectangle must stay within a row, column or diagonal this is within
        the bound of the Grid.
        domain is List of List of all potential locations for a Chip. """

    domain: List[List[GridLocation]] = []
    grid_height: int = len(grid)
    grid_width: int = len(grid[0]) # Length of the 1st row assuming all row same
    part_height, part_width = part

    # Loop through all the rows and columns, to create all possible solutions
    # that can be included in the domain
    for row in range(grid_height):
        for col in range(grid_width):
            cols_left = range(col, col + part_width)
            rows_left = range(row, row + part_height)

            if col + part_width <= grid_width and row + part_height <= grid_height:
                domain.append([GridLocation(r, c) for c in cols_left for r in rows_left])
            if row + part_width <= grid_height and col + part_height <= grid_width:
                domain.append([GridLocation(r, c) for r in rows_left for c in cols_left ])

    return domain

class CircuitBoardConstraint(Constraint[str, List[GridLocation]]):
    """ Define the constraints by leveraging the abstract class Constraint. """

    def __init__(self, parts: List[tuple]) -> None:
        """ Initialize the constaints """
        super().__init__(parts)
        self.words: List[str] = parts   # Variables

    def satisfied(self, assignment: Dict[str, List[GridLocation]]) -> bool:
        """ Override the .satisfied() method from the abstract class
            If there are any duplicates grid locations then there is an overlap.
             """

        all_locations = [locs
                            for values in assignment.values()
                            for locs in values
                        ]

        # If the length of set() is different than original then overlap.
        return len(set(all_locations)) == len(all_locations)

if __name__ == "__main__":
    grid: Grid = generate_grid(9, 9)

    # Define variable(parts) and domains(locations).
    parts: List[tuple] = [(4, 5), (6, 3), (3, 2)]

    locations: Dict[str, List[List[GridLocation]]] = {}
    for part in parts:
        locations[part] = generate_domain(part, grid)

    csp: CSP[str, List[GridLocation]] = CSP(parts, locations)

    csp.add_constraint(CircuitBoardConstraint(parts))

    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        count = 0
        for grid_locations in solution.values():
            part_letter = "123456789"[count]
            count += 1
            for row, col in grid_locations:
                grid[row][col] = part_letter

        display_grid(grid)
