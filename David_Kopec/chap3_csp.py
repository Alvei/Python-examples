""" Constraints-Statisfaction Problems (CSP) core functionality.
    CSPs are composed of variables with possible values that fall into ranges known
    as domains. Contraints between the variables must be satisfied.

    Inspired by David Kopec. Chapter 3.  """

from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod
V = TypeVar('V')  # Variable type
D = TypeVar('D')  # Domain type. This will be the range of a variable

class Constraint(Generic[V, D], ABC):
    """ The default implementation the constraint is an abstract class
        that will be overridded. The abstract class will never be instantiated.
        It includes a satisfied method to determine if contraint is satisfied"""
    def __init__(self, variables: List[V]) -> None:
        """ Initialized with a list of variables. """
        self.variables = variables

    # Must be overridden by subclasses
    @abstractmethod
    def satisfied(self, assignment: Dict[V, D]) -> bool:
        """ Empty function that will overidden. """
        ...

class CSP(Generic[V, D]):
    """ A Constraint Satisfaction Problem (CSP) consists of variables of type V
        that have ranges of values known as domains of type D and constraints
        that determine whether a particular variable's domain selection is valid. """

    def __init__(self, variables: List[V], domains: Dict[V, List[D]]) -> None:
        """ Initialize instance of class and in particular the constraints dictionary.
            domains is a Dict mapping variables to lists of possible values.
            constraints is a Disct that maps each variable to a list of contraints. """
        self.variables: List[V] = variables         # Variables to be constrained
        self.domains: Dict[V, List[D]] = domains    # Domain of each variable

        # Create an empty list of contraints for each variables.
        # Constraints on a variables will be created by add_constraint()
        self.constraints: Dict[V, List[Constraint[V, D]]] = {}
        for variable in self.variables:
            self.constraints[variable] = []
            if variable not in self.domains:
                raise LookupError("Every variable should have a domain assigned to it.")

    def add_constraint(self, constraint: Constraint[V, D]) -> None:
        """ Goes through all the variable touched by a specific constraint and
            add itself to the contraints maping for each of them. """
        for variable in constraint.variables:
            if variable not in self.variables:
                raise LookupError("Variable in constraint no in CSP.")
            else:
                self.constraints[variable].append(constraint)

    def consistent(self, variable: V, assignment: Dict[V, D]) -> bool:
        """ Check if the value assignment is consistent by checking
            all constraints for the variable against it. """
        for constraint in self.constraints[variable]:
            if not constraint.satisfied(assignment):
                return False
        return True             # default case

    def backtracking_search(self, assignment: Dict[V, D] = {}) -> Optional[Dict[V, D]]:
        """ Core backtracking search algorithm. Once you hit a wall in your search,
            you go back to the last known point where you made a decision before the wall,
            and choose a different path. It is a recursive depth-first algo. """

        # Assignment is complete if every variable is assigned (our base case for recursive search)
        if len(assignment) == len(self.variables):
            return assignment

        # Get all variables in the CSP but not in the assignment
        unassigned: List[V] = [v for v in self.variables if v not in assignment]
        # Get every possible domain value of the first unassigned variable
        first: V = unassigned[0]

        # Loop through the domain values for that variable. Create temp copy of assignment
        for value in self.domains[first]:
            local_assignment = assignment.copy()
            local_assignment[first] = value

            # We call .consistent() method. if we're still consistent, we recurse (continue)
            # .consistent() method will check all the contraints for that variable
            if self.consistent(first, local_assignment):
                # Pass the local_assignment to the .backtracking_search() method
                result: Optional[Dict[V, D]] = self.backtracking_search(local_assignment)

                # If we didn't find the result, we will end up backtracking
                if result is not None:
                    return result
        return None
