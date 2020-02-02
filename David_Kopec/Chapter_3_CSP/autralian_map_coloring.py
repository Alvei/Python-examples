""" Map Colloring constraint problem.
    The constraints are that no two adjacent regions can be colored
    with the same color. So the condition depends on who borders who.
    It is therefore a binary contraints (between two variables).
    Every 2 regions that share a border will have a binary constraints meaning
    they cannot have the same color.
    Inspired From Classic Computer Science Problems in Python Chapter by David Kopec.  """

from typing import Dict, List, Optional
from csp import Constraint, CSP
from pprint import pprint

class MapColoringConstraint(Constraint[str, str]):
    """ Define the map contraints and its .satisfied() method
        Inherits the attributes of Constraint class including a satisfied
        method that needs to be updated. """

    def __init__(self, place1: str, place2: str) -> None:
        """ Initializer. super() is used to call method from the superclass. """
        super().__init__([place1, place2])
        self.place1: str = place1  # 1st region that border the 2nd region
        self.place2: str = place2  # inverse

    def satisfied(self, assignment: Dict[str, str]) -> bool:
        """ Overrides the abstractmethod.  assignment is a dictionary with
            the current decisions that have satisfied the constraints to date.
            Checking to see the color of the two regions are not the same. """
        if self.place1 not in assignment or self.place2 not in assignment:
            return True  # This is a quick check. If not in assignment then no constraints

        # Otherwise check if the color of both regions are the same
        return assignment[self.place1] != assignment[self.place2]

if __name__ == "__main__":

    # Name of the regions of Australia
    variables: List[str] = ["Western Australia", "Northern Territory", "South Australia",
                            "Queensland", "New South Wales", "Victoria", "Tasmania"]

    # For each regions, assign a list of potential solutions (R, G, B)
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
        #domains[variable] = ["red", "green"]  # No solution

    csp: CSP[str, str] = CSP(variables, domains)

    # Define the binary constraints or simply which region borders another region
    csp.add_constraint(MapColoringConstraint("Western Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Western Australia", "South Australia"))
    csp.add_constraint(MapColoringConstraint("South Australia", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "Northern Territory"))
    csp.add_constraint(MapColoringConstraint("Queensland", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Queensland", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("New South Wales", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "South Australia"))
    csp.add_constraint(MapColoringConstraint("Victoria", "New South Wales"))
    csp.add_constraint(MapColoringConstraint("Victoria", "Tasmania"))

    # Run the constraint optimization algo
    solution: Optional[Dict[str, str]] = csp.backtracking_search()

    if solution is None:
        print("No solution found!")
    else:
        pprint(solution)
