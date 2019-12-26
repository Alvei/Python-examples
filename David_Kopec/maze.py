""" Inspired by David Kopec. """
from enum import Enum
import random
from math import sqrt
from typing import List, NamedTuple, Callable, Optional

class Cell(str, Enum):
    """ xxx """
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class MazeLocation(NamedTuple):
    """ Refer to individual location in the maze. """
    row: int
    column: int