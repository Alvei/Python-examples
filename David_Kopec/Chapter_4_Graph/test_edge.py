"""test_edge.py """
import pytest
from edge import Edge

def test_edge():
    new_edge: Edge = Edge(1, 2)
    assert type(new_edge) == Edge
    assert new_edge == Edge(1, 2)

def test_reverse():
    new_edge: Edge = Edge(1, 2)
    assert new_edge.reversed() == Edge(2, 1)