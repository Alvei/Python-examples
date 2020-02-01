""" word_search.py
    Grid of letters with hidden letters placed along rows, columns, diagonals.
    Variables are the words while the locations are the domains.
    Current problem does not include overlapping words.
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
    """ Initializes/fills the grid with random letters. """
    assert columns > 0
    assert rows > 0
    return [[choice(ascii_uppercase)
            for c in range(columns)]
            for r in range(rows)
           ]

def display_grid(grid: Grid) -> None:
    """ Displays the grid of letters. Grid is an alias of List[List[str]].
        Therefore .join(row) merges a list of characters. """
    for row in grid:
        print("".join(row))

def generate_domain(word: str, grid: Grid) -> List[List[GridLocation]]:
    """ Words must stay within a row, column or diagonal this is within
        the bound of the Grid.
        domain is List of List of all potential locations for a word. """

    domain: List[List[GridLocation]] = []
    height: int = len(grid)
    width: int = len(grid[0]) # Length of the 1st row assuming all row same
    length: int = len(word)

    # Loop through all the rows and columns, to create all possible solutions
    # that can be included in the domain
    for row in range(height):
        for col in range(width):

            columns: range = range(col, col + length + 1)
            rows: range = range(row, row + length + 1)

            # Does not exceed grid to the right of current loc
            if col + length <= width:
                # left to right
                domain.append([GridLocation(row, c) for c in columns])
                # diagonal towards bottom right
                if row + length <= height:
                    domain.append([GridLocation(r, col + (r - row)) for r in rows])

            # Does not exceed grid to the bottom of current loc
            if row + length <= height:
                # top to bottom
                domain.append([GridLocation(r, col) for r in rows])
                # diagonal towards bottom left
                if col - length >= 0:
                    domain.append([GridLocation(r, col - (r - row)) for r in rows])
    return domain

class WordSearchConstraint(Constraint[str, List[GridLocation]]):
    """ Define the constraints by leveraging the abstract class Constraint. """

    def __init__(self, words: List[str]) -> None:
        """ Initialize the constaints """
        super().__init__(words)
        self.words: List[str] = words   # Variables

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

    # Define variables(words) and domains(locations)
    words: List[str] = ["MATTHEW", "JOE", "MARY", "SARAH", "SALLY"]
    locations: Dict[str, List[List[GridLocation]]] = {}
    for word in words:
        locations[word] = generate_domain(word, grid)

    csp: CSP[str, List[GridLocation]] = CSP(words, locations)

    csp.add_constraint(WordSearchConstraint(words))

    solution: Optional[Dict[str, List[GridLocation]]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        for word, grid_locations in solution.items():
            # random reverse half the time
            if choice([True, False]):
                grid_locations.reverse()
            for index, letter in enumerate(word):
                (row, col) = (grid_locations[index].row, grid_locations[index].column)
                grid[row][col] = letter
        display_grid(grid)
