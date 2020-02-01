""" queens.py
    How can eight queens be placed on an 8x8 board without any queen attacking another queen?
    It requires a queen on each column. Requires two classes defined elsewhere that do all the work.
    Setup the CSP problem with columns (variables) and rows (domains or possible solution).    Inspired From Classic Computer Science Problems in Python Chapter by David Kopec. """

from typing import Dict, List, Optional
from pprint import pprint
from csp import Constraint, CSP

class QueensConstraint(Constraint[int, int]):
    """ Inherits the attributes of Constraint class including a satisfied method that needs
        to be updated. Use [int, int] rather than [str, int] to iterate easily across columns. """

    def __init__(self, columns: List[int]) -> None:
        """ Initialize the game. """
        super().__init__(columns)
        self.columns: List[int] = columns

    def satisfied(self, assignment: Dict[int, int]) -> bool:
        """ 2 conditions that must be satisfied: 2 queens are on the same row or same diagonal.
            To check diagonal, the difference between rows is equal to difference betweel cols.
            Not checking for columns since the problem requires 8 queens, we fixed 1 per column.
            arg: assignement defines the "decided variables matched" up to this point. """

        # q1c = queen 1 column, q1r = queen 1 row
        # assigment.items() will return tuples of all the decided locations, one at a time.
        for q1c, q1r in assignment.items():
            # q2c = queen 2 column
            for q2c in range(q1c + 1, len(self.columns) + 1):
                if q2c in assignment:
                    q2r: int = assignment[q2c] # q2r = queen 2 row
                    if q1r == q2r: # same row?
                        return False
                    if abs(q1r - q2r) == abs(q1c - q2c): # same diagonal?
                        return False
        return True # no conflict


if __name__ == "__main__":

    cols: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]  # Define the variables

    # Define the domains which is the range of values for a variable
    rows: Dict[int, List[int]] = {}
    for column in cols:
        rows[column] = [1, 2, 3, 4, 5, 6, 7, 8]

    # Create instance of the CSP framework with variables and domains
    csp: CSP[int, int] = CSP(cols, rows)

    # .add_constraint() expects an object of type Constraint.
    # the __init__ requires a list of int cols
    csp.add_constraint(QueensConstraint(cols))

    solution: Optional[Dict[int, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        # Convert the answer so that the column is displayed in letters
        LETTER_COLS: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        final_sol: Optional[Dict[str, int]] = dict(zip(LETTER_COLS, list(solution.values())))
        pprint(final_sol)
