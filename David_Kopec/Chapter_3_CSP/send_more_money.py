""" send_more_money.py
    Cryptoarithmic puzzle where you find digits to replace letters to make a mathematical statement True.
    Each letter represents one digt (0-9). No two letters can represents the same digit.
    Statement: SEND + MORE = MONEY. Number of letters cannot exceet 10!
    Inpsired Classic Computer Science Problems in Python Chapter 3 by Copyright 2018 David Kopec. """

from typing import Dict, List, Optional
from csp import Constraint, CSP

class SendMoreMoneyConstraint(Constraint[str, int]):
    """ Inherits properties from abstract class Constraint. """

    def __init__(self, letters: List[str]) -> None:
        """ Initialize instance. """
        assert len(letter) <= 10
        super().__init__(letters)
        self.letters: List[str] = letters

    def satisfied(self, assignment: Dict[str, int]) -> bool:
        """ Overrid the .satisfied() method.
            SEND + MORE = MONEY.
            Not generic and alot of hard coding. """

        # If there are duplicate values then it's not a solution. Use set() trick again.
        if len(set(assignment.values())) < len(assignment):
            return False

        # If all variables have been assigned, check if it adds correctly
        if len(assignment) == len(self.letters):
            s: int = assignment["S"]
            e: int = assignment["E"]
            n: int = assignment["N"]
            d: int = assignment["D"]
            m: int = assignment["M"]
            o: int = assignment["O"]
            r: int = assignment["R"]
            y: int = assignment["Y"]
            send: int = s * 1000 + e * 100 + n * 10 + d
            more: int = m * 1000 + o * 100 + r * 10 + e
            money: int = m * 10000 + o * 1000 + n * 100 + e * 10 + y
            return send + more == money
        return True # no conflict


if __name__ == "__main__":

    # Define variables
    math_expr: str = "SEND+MORE=MONEY"   # Original mathematical expression as a string
    strip_expr: str = ''.join( c for c in math_expr if  c not in '+-*/= ' )
    letters: List[str] = list(set(list(strip_expr))) # Convert into list, use set() to dedup

    # Define domains which is all the digits for each variable
    possible_digits: Dict[str, List[int]] = {}
    for letter in letters:
        possible_digits[letter] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    possible_digits["M"] = [1]  # so we don't get answers starting with a 0

    csp: CSP[str, int] = CSP(letters, possible_digits)

    csp.add_constraint(SendMoreMoneyConstraint(letters))
    solution: Optional[Dict[str, int]] = csp.backtracking_search()
    if solution is None:
        print("No solution found!")
    else:
        print(solution)