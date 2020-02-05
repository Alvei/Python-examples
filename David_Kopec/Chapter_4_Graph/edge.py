""" edge.py
    Defines an Edge class. With minimal functionality

    @dataclass decorator saves some tedium by automatically creating an __init__() method
    that instantiates instance variables for any variables declared with type annotation
    in the class body
    Inspired From Classic Computer Science Problems in Python Chapter 4 by David Kopec. """

from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Edge:
    """ Edge is defined as a connection between two vertices. """
    u: int # The "from" vertex
    v: int # The "to" vertiex

    def reversed(self) -> Edge:
        """ XXX """
        return Edge(self.v, self.u)

    def __str__(self) -> str:
        """ Printing method. """
        return f"{self.u} -> {self.v}"