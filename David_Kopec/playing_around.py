from generic_search import dfs, bfs, node_to_path, astar, Node, Stack
from typing import List, Generic, TypeVar

T = TypeVar('T')   # Create a generic type

#frontier: Stack[Generic[T]] = Stack()
frontier = Stack[int]()
#frontier: Stack[List[T]] = Stack()
bob = Stack()
bob.push("bob")
bob.push("robert")
bob.push(2)

allo: Stack[Node[T]] = Stack()

frontier.push(1)
frontier.push(2)
frontier.push(2)
print(frontier)
frontier.pop()
print(frontier)
print(bob)

allo.push(10)
allo.push(20)
allo.push(30)
allo.pop
print(allo)

my_node = Node(22, 33)
my_node2 = Node("two", "three")
print("my_node", type(my_node), my_node)
print(my_node2)

my_stack = Stack()
my_stack.push(my_node)
print(my_stack)

my_list: List[Node[T]] = []
my_list2 = [9, 8, 7]
#my_list.append(my_list)
my_list.append(my_node)
print("My_list", my_list)