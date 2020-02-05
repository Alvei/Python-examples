"""test_graph.py """
import pytest
from graph import Graph
from typing import Deque

def test_edge_by_vertices():
    triangle: Graph[str] = Graph(["A", "B", "C"])
    assert triangle.vertex_count == 3, "Triangle has 3 vertices"

    triangle.add_edge_by_vertices("A", "B")
    triangle.add_edge_by_vertices("B", "C")
    triangle.add_edge_by_vertices("A", "C")

    assert triangle.edge_count == 6, "Triangle has 3 edges but bi-directional"

def test_add_vertex():
    triangle: Graph[str] = Graph()
    triangle.add_vertex("A")
    triangle.add_vertex("B")
    triangle.add_vertex("C")
    assert triangle.vertex_count == 3, "Triangle has 3 vertices"
    assert triangle.edge_count == 0, "Edges have not been created yet"