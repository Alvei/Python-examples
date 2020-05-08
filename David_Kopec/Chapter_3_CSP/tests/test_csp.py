""" test_csp.py NOT COMPLETED """
import pytest
from typing import Dict
import sys, os
# required to allow to find the file to test in directory above the test directory
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from csp import CSP, Constraint


def test_initialize():
    # Name of the regions of Australia
    variables: List[str] = ["Western Australia", "Northern Territory", "South Australia",
                            "Queensland", "New South Wales", "Victoria", "Tasmania"]

    # For each regions, assign a list of potential solutions (R, G, B)
    domains: Dict[str, List[str]] = {}
    for variable in variables:
        domains[variable] = ["red", "green", "blue"]
        #domains[variable] = ["red", "green"]  # No solution

    csp: CSP[str, str] = CSP(variables, domains)