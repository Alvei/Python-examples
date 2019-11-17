""" Overloading an operator for a tuple vector"""

import unittest

class Vector:
    """ Vectors are tuples of two elements"""

    def __init__(self, a: int, b: int) -> None:
        """ Initialize. """
        self._dir_x, self._dir_y = (a, b)  # Decomposes a tuple

    @property
    def dir_x(self):
        """ Getter. """
        return self._dir_x

    @property
    def dir_y(self):
        """ Getter. """
        return self._dir_y

    def __str__(self):
        return f"Vector ({self._dir_x},{self._dir_y})"

    def __add__(self, other):
        """ Defines a new way to do tuple additions """
        return Vector(self._dir_x + other._dir_x, self._dir_y + other._dir_y)

    def __sub__(self, other):
        return Vector(self._dir_x - other._dir_x, self._dir_y - other._dir_y)

class Test_Vector(unittest.TestCase):
    def setUp(self):
        self.v1 = Vector(2, 10)
        self.v2 = Vector(5, -2)

    def tearDown(self):
        del self.v1
        del self.v2

    def test_addition(self):
        print(self.v1 + self.v2)
        #self.assertEqual(self.v1 + self.v2, Vector(7,8))

def main():
    """ Main code """
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print("\nTest Harness ***")
    print(f"V1 = {v1} and V2 = {v2}")
    print(f"V1 + V2 = {v1 + v2}")
    print(f"V1 - V2 = {v1 - v2}")
    print(f"V1.x = {v1.dir_x} and V1.y = {v1.dir_y}")


if __name__ == '__main__':
    unittest.main()
    #main()
