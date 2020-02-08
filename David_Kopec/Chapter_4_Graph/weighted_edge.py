""" weigthed_edge.py
    Augment the Edge class with weighted edges.
    Inspired From Classic Computer Science Problems in Python Chapter 4 by David Kopec. """
from __future__ import annotations
from dataclasses import dataclass
from edge import Edge

@dataclass
class WeightedEdge(Edge):
    """ Created a subclass of Edge. This weight can represent the distances between
        vertices, the intensity of a connection etc. This is required for Jarnik's algo. """
    weight: float

    def reversed(self) -> WeightedEdge:
        """ Still undirected network so you can have two edges for each direction. """
        return WeightedEdge(self.v, self.u, self.weight)

    # so that we can order edges by weight to find the minimum weight edge
    def __lt__(self, other: WeightedEdge) -> bool:
        """ Overload lower than. """
        return self.weight < other.weight

    def __str__(self) -> str:
        """ Default print function. """
        return f"{self.u} {self.weight}> {self.v}"
