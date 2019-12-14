""" Basic Circle class. Inspired by Python Morsels and
    https://www.programiz.com/python-programming/property
    that uses @property and @setter
"""
import math

class Circle():
    """ Circle with radius, area, and diameter.
        radius is an initialized attribute that cannot be negative. """

    def __init__(self, radius: float = 1) -> None:
        self.radius = radius

    def __repr__(self) -> str:
        return f"Circle({self.radius})"

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        """ Defines a private radius. """
        if value < 0.0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def diameter(self) -> float:
        """ Calculated from radius vs. stored. """
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter: float) -> None:
        """ Setter actually defines radius. """
        self.radius = diameter / 2.0

    @property
    def area(self) -> float:
        """ Attribute calculated using radius vs. being part of class instance. """
        return math.pi * self.radius**2


def main():
    """ Main code """

    c = Circle()
    print(f"radius = {c.radius}, diameter = {c.diameter}, area = {c.area:.2f}")

    c = Circle(2)
    print(f"radius = {c.radius}, diameter = {c.diameter}, area = {c.area:.2f}")


    c.radius = 1  # using the setter
    print(f"radius = {c.radius}, diameter = {c.diameter}, area = {c.area:.2f}")

    c.diameter = 6  # using the setter
    print(f"radius = {c.radius}, diameter = {c.diameter}, area = {c.area:.2f}")

 #   c.radius = -2  # using the setter

if __name__ == '__main__':
    main()
