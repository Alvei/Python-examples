""" test_basic_binary_tree.py """
from basic_binary_tree import Node, Tree

def test_node_init_empty():
    node = Node()
    assert node.value == None
    assert node.left == None
    assert node.right == None

def test_node_init_root():
    node = Node(4)
    assert node.value == 4
    assert node.left == None
    assert node.right == None

def test_node_insert_left():
    node = Node(4)
    assert node.insert(3) == True
    #assert node.left == 3
    assert type(node.left) == type(Node())
    assert node.right == None

def test_node_insert_right():
    node = Node(4)
    assert node.insert(5) == True
    assert node.left == None
    assert type(node.right) == type(Node())
    assert node.right == Node(5)

def test_loading_tree():
    bst = Tree()
    list_nodes = [50, 30, 20, 40, 70, 60, 80]  # Root is 50
    for node in list_nodes:
        assert bst.insert(node) == True

def test_loading_tree_with_duplicate():
    bst = Tree()
    list_nodes = [50, 30, 30, 20, 40, 40, 70]
    answers = [True, True, False, True, True, False, True]
    for index, node in enumerate(list_nodes):
        assert bst.insert(node) == answers[index]

    #bst.preorder()  # Preorder (Root, Left, Right)  : 50, 30, 20, 40, 70, 60, 80
    #bst.postorder() # Postorder (Left, Right, Root) : 20, 40, 30, 60, 80, 70, 50
    #bst.inorder()   # Inorder (Left, Root, Right)   : 20, 30, 40, 50, 60, 70, 80