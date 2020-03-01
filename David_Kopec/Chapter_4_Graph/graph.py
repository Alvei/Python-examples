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

    def remove_edge_by_indices(self, u, v):
        """ Remove an edge using vertex indices (convenience method).
            for exercise 4.7.1. Need to remove both directions. """
        self._edges[u].remove(Edge(u, v))
        self._edges[v].remove(Edge(v, u))

    def remove_edge_by_vertices(self, first, second):
        """ Remove edge by looking up vertex indices (convenience method)..
            for exercise 4.7.1 """
        u = self.index_of(first)
        v = self.index_of(second)
        remove_edge_by_indices(u, v)

    def remove_vertex_at_index(self, u) -> None:
        """ Remove a vertex of indice [u] to the graph and return its index.
            Part of exercise 4.7.1"""

        # Need to do a list copy since we will remove elements form
        # the list and vertex_edges would change during the loop
        vertex_edges: List[Edge] = self._edges[u].copy()

        # Cycle through the edges of that vertex [u] to capture 2nd indice [v]
        for edge in vertex_edges: # _edges[u] is a list of edges at vertex u
            self.remove_edge_by_indices(edge.u, edge.v)

        # Convert the index u into the vertex to be removed.
        temp_vertex: V = self.vertex_at(u)

        # Find all the location where the vertex was found. Should be only 1
        loc = [i for i, value in enumerate(self._vertices) if value == temp_vertex]
        self._vertices.pop(loc[0])

        # Go back and remove the empty list in the edge list that
        # correspond to the vertex
        self._edges.pop(loc[0])

        # Loop over all the vertex and all the edges in that vertex
        for index_v, vertex in enumerate(self._edges):
            for index_e, edge in enumerate(vertex):
                # If the indice of the vertex of this edge are bigger than the vertex
                # indice removed, reduce it by 1. Need to do the reverse as well.
                if edge.u >= u:
                    self._edges[index_v][index_e] = Edge(edge.u-1, edge.v)
                if edge.v >= u:
                    self._edges[index_v][index_e] = Edge(edge.u, edge.v-1)

    def vertex_at(self, index: int) -> V:
        """ Find the vertex at a specific index. """
        try:
            vertex = self._vertices[index]
        except IndexError:
            raise IndexError(f"\n*** IndexError => There is no Vertex for the index: '{index}'\n")
        else:
            return vertex

    def index_of(self, vertex: V) -> int:
        """ Find the index of a vertex in the graph. """
        try:
            index = self._vertices.index(vertex)
        except ValueError as error:
            #print(f"*** ValueError => There is no index for the Vertex: '{vertex}'\n")
            raise ValueError(f"\n*** ValueError => There is no index for the Vertex: '{vertex}'\n")
        else:
            return index

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
    city_graph: Graph[str] = Graph(["Seattle", "San Francisco", "Los Angeles", \
        "Riverside", "Phoenix", "Chicago", "Boston", "New York", "Atlanta", \
        "Miami", "Dallas", "Houston", "Detroit", "Philadelphia", "Washington"])
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
    print(f"Vertices: {city_graph.vertex_count} and edges: {city_graph.edge_count}")

    print(f"Removing one city: {city_graph.vertex_at(12)} ...")
    city_graph.remove_vertex_at_index(12)
    print(f"Vertices: {city_graph.vertex_count} and edges: {city_graph.edge_count}")
    #print(city_graph)

    # Reuse BFS from Chapter 2 on city_graph
    import sys

    # so we can access the Chapter2 package in the parent directory
    sys.path.insert(0, r'..\Chapter_2_search')
    from three_search_algo import bfs, Node, node_to_path

    """ Breadth-First-Search algorithm. Uses Queue Data element.
        initial: starting point for search.
        goal_test: simple comparison fonction with input type T that returns a bool.
        successors: function that returns a List[T] of all potential next steps or returns None. """

    city = "Boston"
    #city_graph.index_of("London")
    #city = "London"
    connected_city = city_graph.neighbors_for_vertex(city)

    bfs_result: Optional[Node[V]] = bfs("Boston", lambda x: x == "Miami",\
         city_graph.neighbors_for_vertex)
    if bfs_result is None:
        print("No solution found using breadth-first search!")
    else:
        path: List[V] = node_to_path(bfs_result)
        print("\nPath from Boston to Miami:")
        print(path)
