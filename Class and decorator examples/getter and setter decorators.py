
"""
Experiment with getter and setter decorators.  """

class Duck():
    """ Simple class that uses decorators
        @property goes before the getter method. @name.setter goes before the setter method
        It uses name mangling for privacy by using self.__name
    """

    def __init__(self, input_name):
        self.__name = input_name

        @property
        def name(self) -> str:
            """ Getter function. """
            print('\tInside the getter')
            return self.__name

        @name.setter
        def name(self, input_name: str) -> None:
            """ Setter function. """
            print('\tInside the setter')
            self.__name = input_name

class Circle():
    """ Simple circle class to show the use of @property decorator.
        Cool to note that the diameter constantly change with the change in radius. """

    def __init__(self, radius: float) -> None:
        """ Initialize the Circle. Make the radius private with _ """
        self._radius = radius

    @property
    def radius(self) -> float:
        """ Like a getter function. """
        return 2 * self._radius

    @radius.setter
    def radius(self, radius: float):
        """ Setter function. """
        self._radius = radius

    @property
    def diameter(self) -> float:
        """ Like a getter function. """
        return 2 * self._radius


class A():
    """ Simple class to show how to create a class specific vs. instance method().
        Need to use the @classmethod decorator and use cls to refer back to the class.
    """
    count = 0

    def __init__(self) -> None:
        """ Initialization increments the instance variable count. """
        A.count += 1

    def exclaim(self):
        print("\tI'm in A!")

    @classmethod
    def kids(cls):
        print(f"A has {cls.count} little objects")

class CoyoteWeapon():
    """ Simple class to show the use of the @staticmethod decorator.
        It can be called from an uninstantiated class object. """

    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")


def main():

    print("\nExample 1:")
    fowl = Duck("Howard") # Initialize
    fowl.name = "Donald"  # Use the setter
    print(fowl.name)

    print("\nExample 2:")
    c = Circle(5)
    print(f"Radius {c.radius} and Diameter {c.diameter}")

    c.radius = 7
    print(f"Radius {c.radius} and Diameter {c.diameter}")

    print("\nExample 3:")
    easy_a = A()
    brezzy_a = A()
    whezzy_a = A()
    A.kids()  # call the class method

    print("\nExample 4:")
    CoyoteWeapon.commercial()

if __name__ == "__main__":
    main()