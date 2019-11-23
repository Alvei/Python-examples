
"""
Experiment with getter and setter decorators.  """

class Duck():
    """ Simple class that uses decorators
        @property goes before the getter method. @name.setter goes before the setter method
        It uses name mangling for privacy by using self.__name.
    """

    def __init__(self, input_name: str):
        """ Initialize. """
        self.__name = input_name

    @property
    def name(self) -> str:
        """ Getter function. """
        print('\tInside the getter')
        return self.__name

    @name.setter
    def name(self, input_name: str) -> None:
        """ Setter function. """
        print(f"\tInside the setter with {input_name}")
        self.__name = input_name

    def __str__(self) -> str:
        """ Display class. """
        return f"This is my class {self.__name}"

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


class Generic():
    """ Simple class to show how to create a class specific vs. instance method().
        Need to use the @classmethod decorator and use cls to refer back to the class.
    """
    count = 0

    def __init__(self) -> None:
        """ Initialization increments the instance variable count. """
        Generic.count += 1

    def exclaim(self):
        """ Print something. """
        print("\tI'm in A!")

    @classmethod
    def kids(cls):
        """ Print class variable. """
        print(f"A has {cls.count} little objects")

class CoyoteWeapon():
    """ Simple class to show the use of the @staticmethod decorator.
        It can be called from an uninstantiated class object. """

    @staticmethod
    def commercial():
        """ Prints static function. """
        print("This CoyoteWeapon has been brought to you by Acme")

    def __str__(self) -> str:
        """ Display class. """
        return f"This is coyote class"


def main():
    """ Test Harness """
    print("\nExample 1:")
    fowl = Duck("Howard") # Initialize
    fowl.name = "Donald"  # Use the setter
    print(fowl.name)
    print(fowl)

    print("\nExample 2: Circle")
    my_circle = Circle(5)
    print(f"Radius {my_circle.radius} and Diameter {my_circle.diameter}")

    my_circle.radius = 7
    print(f"Radius {my_circle.radius} and Diameter {my_circle.diameter}")

    print("\nExample 3: Generic and @classmethod")
    easy_a = Generic()
    brezzy_a = Generic()
    whezzy_a = Generic()
    Generic.kids()  # call the class method

    print("\nExample 4: @staticmethod. Calling without initializing 1st")
    CoyoteWeapon.commercial()

if __name__ == "__main__":
    main()
