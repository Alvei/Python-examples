""" Creating a class with getter and setter using Properties.
    This will allow each of the properties to be updated when attribute is changed.
    Greate example of decorator in classes
    https://www.programiz.com/python-programming/property
"""
PI = 3.14159


class Circle():
    """ Definition of the class Circle."""

    def __init__(self, input_radius):
        self.__radius = input_radius

    def __str__(self):
        return "Radius: " + str(self.__radius)

    @property
    def radius(self):
        """ Defines the getter for private variable using @property"""
        # print "Inside the getter"
        return self.__radius

    @radius.setter
    def radius(self, value):
        # print "Inside the setter"
        self.__radius = value

    @property
    def diameter(self):
        """ Defines the getter for private variable using @property"""
        return 2 * self.__radius

    @property
    def area(self):
        """ Defines the getter for private variable using @property"""
        return PI * self.__radius**2


def main():
    """ Main code """
    c = Circle(5)
    print(f"radius = {c.radius}, diameter = {c.diameter}, area = {c.area}")

    c.radius = 6  # using the setter
    print(f"radius = {c.radius}, diameter = {c.diameter}, area = {c.area}")


if __name__ == '__main__':
    main()
