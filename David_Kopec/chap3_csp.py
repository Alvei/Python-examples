""" Constraints-Statisfaction Problems (CSP) core functionality. CSPs are composed of variables with possible
    values that fall into ranges known as domains. Contraints between the variables must be satisfied.

    There are two classes. The Abstract Constraint class and the CSP class which brings variables-domains-constraints together.

    Generic is indicating that the types of the variables and the domains are not known at the time of class definition.
    In other words, we do not know what the type of variables will be, and we do not know what the type of the domains will be.
    Since, we don’t know, we need a place holder. V is a placeholder for whatever the type of the variables ends up being
    (could be a string, int, etc.). D is a placeholder for whatever the type of the domains will end up being.
    Throughout the definition of the class, anywhere you see V, that will end up being filled in with V’s actual type.

    Imagine the alternative. If we hardcoded variables as being strings and domains as being integers, then we would have
    a constraint type that would work well for some problems but not others. Instead, we have flexibility here.

    Note that Python without type hints wouldn’t require this at all—so without the type hints, we wouldn’t need to worry
    at all about the types because they could be anything.

    Inspired From Classic Computer Science Problems in Python Chapter by David Kopec. """

from typing import Generic, TypeVar, Dict, List, Optional
from abc import ABC, abstractmethod
V = TypeVar('V')  # Variable type
D = TypeVar('D')  # Domain type. This will be the range of a variable

class Constraint(Generic[V, D], ABC):
    """ The default implementation the constraint is an abstract class that will be overridded for each problem.
        The abstract class will never be instantiated.
        It includes a .satisfied() method to determine if contraints are satisfied. """

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
        # Constraints on a variables will be created by .add_constraint() method
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

            self.constraints[variable].append(constraint)   # Default

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
            and choose a different path. It is a recursive depth-first algo.
            The 1st time it is called, it will initialize the assignment Dict. """

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
