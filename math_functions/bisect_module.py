""" Using the bisect module example. """
from bisect import bisect
# GRADES and BREAKPOINTS have the same numbers of elements
GRADES = "FEDCBA"
BREAKPOINTS = [30, 44, 66, 75, 85]

def grade(num: float):
    """ Convert a decimal grade into a letter grade.
        Bisect returns the index of the list BREAKPOINTS where hitting BP means letter above """
    return GRADES[bisect(BREAKPOINTS, num)]

print(f"grade for 66: {grade(66)}")
hwk: list = [33, 99, 77, 44, 12, 88]
print(list(map(grade, hwk)))

