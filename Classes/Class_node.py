""" Class_node.py"""


class Node:
    """ Building block for the linked list implementation is the node.
        First, the node must contain the list item itself.
        In addition, each node must hold a reference to the next node.
        A reference to None will denote that there is no next node. """

    def __init__(self, init_data):
        """ Initialize the node. """
        self.data = init_data
        self.next = None

    def get_data(self):
        """ Getter method. """
        return self.data

    def get_next(self):
        """ Getter_method. """
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next
