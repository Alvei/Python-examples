""" Simple version of Queue ADT. In Chapter 2 of David Kopec, more generic version. """


class Queue:
    def __init__(self):
        """ Initialize Queue using list. """
        self.items = []

    def is_empty(self):
        """ O(1). """
        return self.items == []

    def enqueue(self, item):
        """ O(n). Linear time. """
        self.items.insert(0, item)

    def dequeue(self):
        """ O(1). """
        return self.items.pop()

    def peek(self):
        """ O(1). """
        return self.items[-1]

    def size(self):
        """ O(1). """
        return len(self.items)
