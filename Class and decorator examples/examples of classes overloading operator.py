""" Overloading an operator for a tuple vector"""


class Vector:
    """ Vectors are tuples of two elements"""

    def __init__(self, a: int, b: int) -> None:
        self.a, self.b = (a, b)  # Decomposes a tuple

    def __str__(self):
        return f"Vector ({self.a},{self.b})"

    def __add__(self, other):
        """ Defines a new way to do tuple additions """
        return Vector(self.a + other.a, self.b + other.b)


def main():
    """ Main code """
    v1 = Vector(2, 10)
    v2 = Vector(5, -2)
    print(f"V1 = {v1} and V2 = {v2}")
    print(f"V1 + V1 = {v1 + v2}")


if __name__ == '__main__':
    main()
