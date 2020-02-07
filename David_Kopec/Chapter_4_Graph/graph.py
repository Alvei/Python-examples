""" graph.py
    Graph class associates vertices with edges.

    Every vertex will ultimately be assigned an integer index, but will be stored as the
    user-defined generic type.
    Inspired From Classic Computer Science Problems in Python Chapter 4 by David Kopec. """

from typing import TypeVar, Generic, List, Optional
from edge import Edge

V = TypeVar('V') # type of the vertices in the graph

class Graph(Generic[V]):
    """ Generic graph that associates vertices with edges. """

    def __init__(self, vertices: List[V] = []) -> None:
        """ Initializes the graph.
            vertices are saved as list of generic type V and can be access as indexes.
            For each vertex, there is a list of all the Edges(u, v) touching that
            vertex. They will all have the same u (starting vertex). """
        self._vertices: List[V] = vertices
        self._edges: List[List[Edge]] = [[] for _ in vertices] # For each vertex empty list

    @property
    def vertex_count(self) -> int:
        """ Counts the number of vertices. """
        return len(self._vertices)

    @property
    def edge_count(self) -> int:
        """ Counts the number of edges. """
        return sum(map(len, self._edges))

    def add_vertex(self, vertex: V) -> int:
        """ Add a vertex to the graph and return its index. """
        self._vertices.append(vertex)
        self._edges.append([])       # Add empty list for edges
        return self.vertex_count - 1 # return index of added vertex

    def add_edge(self, edge: Edge) -> None:
        """ An undirected graph will always add edges in both directions. """
        self._edges[edge.u].append(edge)
        self._edges[edge.v].append(edge.reversed())

    def add_edge_by_indices(self, u: int, v: int) -> None:
        """ Add an edge using vertex indices (convenience method). """
        edge: Edge = Edge(u, v)
        self.add_edge(edge)   # call previous function

    def add_edge_by_vertices(self, first: V, second: V) -> None:
        """ Add an edge by looking up vertex indices (convenience method). """
        u: int = self._vertices.index(first)
        v: int = self._vertices.index(second)
        self.add_edge_by_indices(u, v)

    def vertex_at(self, index: int) -> V:
        """ Find the vertex at a specific index. """
        return self._vertices[index]

    # Find the index of a vertex in the graph
    def index_of(self, vertex: V) -> int:
        return self._vertices.index(vertex)

    def neighbors_for_index(self, index: int) -> List[V]:
        """ Find the vertices that a vertex at some index is connected to.
            map(function, iterator) returns an iterator hence the list.
            the function is .vertex_at()
            iterator is the list comprehension which is the index of
            2nd vertices of each edge of the vertex at index. """
        return list(map(self.vertex_at, [e.v for e in self._edges[index]]))

    def neighbors_for_vertex(self, vertex: V) -> List[V]:
        """ Lookup a vertice's index and find its neighbors (convenience method). """
        return self.neighbors_for_index(self.index_of(vertex))

    def edges_for_index(self, index: int) -> List[Edge]:
        """ Return all of the edges associated with a vertex at some index. """
        return self._edges[index]

    def edges_for_vertex(self, vertex: V) -> List[Edge]:
        """ Lookup the index of a vertex and return its edges (convenience method). """
        return self.edges_for_index(self.index_of(vertex))

    def __str__(self) -> str:
        """ Make it easy to pretty-print a Graph. """
        desc: str = ""
        for i in range(self.vertex_count):
            desc += f"{self.vertex_at(i)} -> {self.neighbors_for_index(i)}\n"
        return desc


if __name__ == "__main__":
    # test basic Graph construction
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles", "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta", "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
    city_graph.add_edge_by_vertices("Seattle", "Chicago")
    city_graph.add_edge_by_vertices("Seattle", "San Francisco")
    city_graph.add_edge_by_vertices("San Francisco", "Riverside")
    city_graph.add_edge_by_vertices("San Francisco", "Los Angeles")
    city_graph.add_edge_by_vertices("Los Angeles", "Riverside")
    city_graph.add_edge_by_vertices("Los Angeles", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Phoenix")
    city_graph.add_edge_by_vertices("Riverside", "Chicago")
    city_graph.add_edge_by_vertices("Phoenix", "Dallas")
    city_graph.add_edge_by_vertices("Phoenix", "Houston")
    city_graph.add_edge_by_vertices("Dallas", "Chicago")
    city_graph.add_edge_by_vertices("Dallas", "Atlanta")
    city_graph.add_edge_by_vertices("Dallas", "Houston")
    city_graph.add_edge_by_vertices("Houston", "Atlanta")
    city_graph.add_edge_by_vertices("Houston", "Miami")
    city_graph.add_edge_by_vertices("Atlanta", "Chicago")
    city_graph.add_edge_by_vertices("Atlanta", "Washington")
    city_graph.add_edge_by_vertices("Atlanta", "Miami")
    city_graph.add_edge_by_vertices("Miami", "Washington")
    city_graph.add_edge_by_vertices("Chicago", "Detroit")
    city_graph.add_edge_by_vertices("Detroit", "Boston")
    city_graph.add_edge_by_vertices("Detroit", "Washington")
    city_graph.add_edge_by_vertices("Detroit", "New York")
    city_graph.add_edge_by_vertices("Boston", "New York")
    city_graph.add_edge_by_vertices("New York", "Philadelphia")
    city_graph.add_edge_by_vertices("Philadelphia", "Washington")
    print(city_graph)

    # Reuse BFS from Chapter 2 on city_graph
    import sys
    sys.path.insert(0, '..') # so we can access the Chapter2 package in the parent directory
    from Chapter_2_Search.generic_search import bfs, Node, node_to_path

    bfs_result: Optional[Node[V]] = bfs("Boston", lambda x: x == "Miami", city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("Path from Boston to Miami:")
        print(path)

