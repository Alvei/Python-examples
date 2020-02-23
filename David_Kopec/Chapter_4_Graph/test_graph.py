"""test_graph.py """
import pytest
from edge import Edge
from graph import Graph
from typing import Deque

@pytest.fixture
def triangle():
    triangle: Graph[str] = Graph(["A", "B", "C"])
    triangle.add_edge_by_vertices("A", "B")
    triangle.add_edge_by_vertices("B", "C")
    triangle.add_edge_by_vertices("A", "C")
    return triangle

@pytest.fixture
def rectangle():
    rectangle: Graph[str] = Graph(["A", "B", "C", "D"])
    rectangle.add_edge_by_vertices("A", "B")
    rectangle.add_edge_by_vertices("B", "C")
    rectangle.add_edge_by_vertices("C", "D")
    rectangle.add_edge_by_vertices("D", "A")
    return rectangle

def test_counts(triangle):
    assert triangle.vertex_count == 3, "Triangle has 3 vertices"
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

def test_index(triangle):
    assert triangle.index_of("C") == 2, "Index of Vertex C is 2"
    assert triangle.index_of("B") == 1, "Index of Vertex B is 1"

def test_vertex_not_present(triangle):
    with pytest.raises(ValueError):
        triangle.index_of("D")

def test_vertex(triangle):
    assert triangle.vertex_at(1) == "B", "The second vertex is B"

def test_index_not_present(triangle):
    with pytest.raises(IndexError):
        triangle.vertex_at(4)

def test_remove_edge_index(triangle):
    assert triangle.edge_count == 6, "Full triangle"
    triangle.remove_edge_by_indices(0, 1)

    # Check all vertices
    assert triangle.vertex_count == 3, "Check the Vertex are still the same"
    assert triangle.vertex_at(0) == "A", "The first vertex is A"
    assert triangle.vertex_at(1) == "B", "The second vertex is B"
    assert triangle.vertex_at(2) == "C", "The third vertex is C"
    assert triangle.index_of("A") == 0, "Index of Vertex A is 0"
    assert triangle.index_of("B") == 1, "Index of Vertex B is 1"
    assert triangle.index_of("C") == 2, "Index of Vertex C is 2"

    # Check all edges
    assert triangle.edge_count == 4, "Removed on edge"
    assert triangle.edges_for_vertex("A") == [Edge(0, 2)], "Edges of Vertex A"
    assert triangle.edges_for_vertex("B") == [Edge(1, 2)], "Edges of Vertex B"
    assert triangle.edges_for_vertex("C") == [Edge(2, 1), Edge(2, 0)], "Edges of Vertex C"

def test_remove_vertice_at_index(triangle):
    assert triangle.edge_count == 6, "Full triangle"

    triangle.remove_vertex_at_index(1)
    assert triangle.vertex_count == 2, "Removed one vertex"
    assert triangle.edge_count == 2, "Removed one edge"

def test_neighbors_for_vertex(rectangle):
    assert rectangle.vertex_count == 4, "Full rectangle"
    assert rectangle.edge_count == 8, "Full rectangle"

    assert rectangle.neighbors_for_vertex("A") == ["B","D"], "A connected to [B, C]"
    assert rectangle.neighbors_for_vertex("B") == ["A","C"], "A connected to [A, C]"
    assert rectangle.neighbors_for_vertex("C") == ["B","D"], "A connected to [B, D]"
    assert rectangle.neighbors_for_vertex("D") == ["C","A"], "A connected to [C, A]"

def test_neighbors_for_no_vertex(rectangle):
    with pytest.raises(ValueError):
        assert rectangle.neighbors_for_vertex("E")



