"""test_graph.py """
import pytest
from edge import Edge
from graph import Graph
from typing import Deque

def test_edge_by_vertices():
    triangle: Graph[str] = Graph(["A", "B", "C"])
    assert triangle.vertex_count == 3, "Triangle has 3 vertices"
    assert triangle.edge_count == 0, "Edges have not been created yet"

    triangle.add_edge_by_vertices("A", "B")
    triangle.add_edge_by_vertices("B", "C")
    triangle.add_edge_by_vertices("A", "C")
    assert triangle.edge_count == 6, "Triangle has 3 edges but bi-directional therefore we save 6"

def test_add_vertex_add_edge():
    triangle: Graph[str] = Graph()
    triangle.add_vertex("A")
    triangle.add_vertex("B")
    triangle.add_vertex("C")

    assert triangle.vertex_count == 3, "Triangle has 3 vertices"
    assert triangle.edge_count == 0, "Edges have not been created yet"

    edge_ab: Edge = Edge(1, 2)
    triangle.add_edge(edge_ab)
    assert triangle.edge_count == 2, "Only 1 edge defined by undirected therefore we save 2"

    edge_bc: Edge = Edge(triangle.index_of("B"), triangle.index_of("C"))
    triangle.add_edge(edge_bc)
    assert triangle.edge_count == 4, "Only 2 edge defined by undirected therefore we save 4"

def test_index():
    triangle: Graph[str] = Graph(["A", "B", "C"])
    triangle.add_edge_by_vertices("A", "B")
    triangle.add_edge_by_vertices("B", "C")
    triangle.add_edge_by_vertices("A", "C")

    assert triangle.vertex_at(1) == "B", "The second vertex is B"
    assert triangle.index_of("C") == 2, "Index of Vertex C is 2"
