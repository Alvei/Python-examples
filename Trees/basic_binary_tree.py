""" basic_binary_tree.py
    Each node is represented by an integer node.
    They have specific properties. First they have two childs (can be null).
    On any given node, the right child is bigger than the parent node.
    On any given node, the left child is smaller than the parent node.
    Binary tree makes searching very efficient.
    inspired by
    https://github.com/joeyajames/Python/blob/master/Trees/BinarySearchTree.py
    https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/

    NOTE : mypy basic_binary_tree.py --no-strict-optional
"""
from typing import Optional

class Node:
    """ Contains data variable to type value and left, right pointers.
        Helper class. """
    def __init__(self, val: Optional[int]=None) -> None:
        self.value: Optional[int] = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

    def __repr__(self):
        """ Default printing behavior. """
        return f"{self.value}"

    def insert(self, data: int) -> bool:
        """ Insert a node to the right or left of a parent node.
            Return False only if trying to insert duplicate. """

        # Do not allow duplicates
        if self.value == data:
            return False

        # New node is to the left of parent node
        if self.value > data:
            # Already have left node? recursive call making current left node == "parent"
            if self.left:
                return self.left.insert(data)
            # Default, otherwise create a new left node
            self.left = Node(data)
            return True
        else:
            if self.right:
                return self.right.insert(data)
            # Default
            self.right = Node(data)
            return True

    def find(self, data: int) -> bool:
        """ Find a specific node. """

        # If it is the current root/parent
        if self.value == data:
            return True

        if self.value > data:       # Go to the left
            if self.left:           # If left exist, then recurse
                return self.left.find(data)
            # Default
            return False
        else:                   # Got to the right recursively
            if self.right:
                return self.right.find(data)
            # Default
            return False

    def preorder(self):
        """ Preorder traverse. Preorder (Root, Left, Right) : 1 2 4 5 3. """
        if self:
            print(f"{str(self.value)}, ", end='')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        """ Postorder traverse. Postorder (Left, Right, Root) : 4 5 2 3 1. """
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(f"{str(self.value)}, ", end='')

    def inorder(self):
        """ Inorder traverse. Inorder (Left, Root, Right) : 4 2 5 1 3.  """
        if self:
            if self.left:
                self.left.inorder()
            print(f"{str(self.value)}, ", end='')
            if self.right:
                self.right.inorder()

    def get_height(self) -> int:
        """ Calculate the height of the tree recursively. """

        # If both branch are available, recursively call each branch
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 1

class Tree:
    """ Contains nodes and corresponding methods. """
    def __init__(self) -> None:
        """ Initialize a tree. """
        self.root: Optional[Node] = None

    def insert(self, data: int) -> bool:
        """ Interface method. node.insert() does all the work.
            If root node exist call recursive node.insert() else create the root node. """
        if self.root:
            return self.root.insert(data)
        # Default
        self.root = Node(data)
        return True

    def find(self, data: int) -> bool:
        """ Interface method. node.find() does all the work.
            If the root is defined, call the node.find() method recursively. """
        if self.root is None:
            return False
        # Default
        return self.root.find(data)

    def preorder(self):
        """ Interface method. node.preorder() does all the work. """
        if self.root is not None:
            print("\nPreOrder (Root, Left, Right): \t", end='')
            self.root.preorder()

    def postorder(self):
        """ Interface method. node.postorder() does all the work. """
        if self.root is not None:
            print("\nPostOrder (Left, Right, Root):\t", end='')
            self.root.postorder()

    def inorder(self):
        """ Interface method. node.inorder() does all the work. """
        if self.root is not None:
            print("\nInOrder (Left, Root, Right):\t", end='')
            self.root.inorder()

    def get_height(self) -> int:
        """ Interface method. node.get_height() does all the work.
            Returns -1 if root does not exist. """
        if self.root is None:
            return -1
        # Default
        return self.root.get_height()

    def delete_tree(self) -> None:
        """ Remove tree. """
        self.root = None

    def is_empty(self) -> bool:
        """ Check if the tree has root. """
        return self.root is None

    def remove_root(self) -> None:
        """ Remove the root node. """

        print(f"Removing the root node {self.root}")

        # Root has no child, empty tree
        if self.root.left is None and self.root.right is None:
            self.root = None

        # Move the left child to become the root
        elif self.root.left and self.root.right is None:
            self.root = self.root.left

        # Move the right child to become the root
        elif self.root.left is None and self.root.right:
            self.root = self.root.right

        # There are two childs for the root
        elif self.root.left and self.root.right:
            del_node_parent = self.root
            del_node = self.root.right
            while del_node.left:
                del_node_parent = del_node
                del_node = del_node.left

            self.root.value = del_node.value
            if del_node.right:
                if del_node_parent.value > del_node.value:
                    del_node_parent.left = del_node.right
                elif del_node_parent.value < del_node.value:
                    del_node_parent.right = del_node.right
            else:
                if del_node.value < del_node_parent.value:
                    del_node_parent.left = None
                else:
                    del_node_parent.right = None

    def remove(self, data: int) -> bool:
        """ Remove a node. """
		# Empty tree
        if self.root is None:
            return False

		# Data is the root node
        if self.root.value == data:
            self.remove_root() # Done removing the root node
            return  True

        parent = None
        node = self.root

		# Find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.left
            elif data > node.value:
                node = node.right

		# case 1: data not found
        if node is None or node.value != data:
            return False

		# case 2: remove-node has no children
        elif node.left is None and node.right is None:
            if data < parent.value:
                parent.left = None
            else:
                parent.right = None
            return True

		# case 3: remove-node has left child only
        elif node.left and node.right is None:
            if data < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left
            return True

		# case 4: remove-node has right child only
        elif node.left is None and node.right:
            if data < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right
            return True

		# case 5: remove-node has left and right children
        else:
            del_node_parent = node
            del_node = node.right
            while del_node.left:
                del_node_parent = del_node
                del_node = del_node.left

            node.value = del_node.value
            if del_node.right:
                if del_node_parent.value > del_node.value:
                    del_node_parent.left = del_node.right
                elif del_node_parent.value < del_node.value:
                    del_node_parent.right = del_node.right
            else:
                if del_node.value < del_node_parent.value:
                    del_node_parent.left = None
                else:
                    del_node_parent.right = None

def main():
    """ Main func for testing.
                50
             /      \
            30       70
            /\       /   \
         20   40    60   80
    """
    bst = Tree()
    list_nodes = [50, 30, 20, 40, 70, 60, 80]  # Root is 50
    for node in list_nodes:
        print(f"Node is {node}: {bst.insert(node)}")

    bst.preorder()  # Preorder (Root, Left, Right)  : 50, 30, 20, 40, 70, 60, 80
    bst.postorder() # Postorder (Left, Right, Root) : 20, 40, 30, 60, 80, 70, 50
    bst.inorder()   # Inorder (Left, Root, Right)   : 20, 30, 40, 50, 60, 70, 80
    print(f"\nHeight is {bst.get_height()}")  # should be 3

    bst2 = Tree()
    list_nodes = [1, 2, 4, 5, 3]  # Root is 1
    print("\nNode: ", end="")
    for node in list_nodes:
        bst2.insert(node)
        print(f" {node}, ", end='')

    bst2.preorder()  # Preorder (Root, Left, Right)  : 1, 2, 4, 3, 5
    bst2.postorder() # Postorder (Left, Right, Root) : 3, 5, 4, 2, 1
    bst2.inorder()   # Inorder (Left, Root, Right)   : 1, 2, 3, 4, 5
    print(f"\nHeight is {bst.get_height()}")  # should be 3

    print(f"Removing 4:")
    bst2.remove(4)
    bst2.preorder()
    print(f"\nRemoving 1:")
    bst2.remove(1)
    bst2.preorder()

if __name__ == "__main__":
    main()
