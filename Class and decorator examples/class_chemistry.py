""" Simple examples of defining a class with private attributes.
    Using Atomic elements
    Greate example of decorator in classes
    https://www.programiz.com/python-programming/property
    Created Aug 2016."""


class Element():
    """Atomic element class with private attributes"""

    def __init__(self, name=None, symbol=None, number=0):
        """Include default names for private variables"""
        self.__name = name
        self.__symbol = symbol
        if number < 0:
            raise ValueError("Negative atomic number is not possible")
        self.__number = number

    def __str__(self):
        return "Name : " + str(self.__name) \
            + ", Symbol : " + str(self.__symbol)\
            + ", Number : " + str(self.__number)

    # Getter and setter for name using decorators
    @property
    def name(self):
        """ Defines the getter using @property decorator"""
        return self.__name

    @name.setter
    def name(self, value):
        """ Defines the setter with decorator"""
        self.__name = value

    # Getter and setter for symbol
    @property
    def symbol(self):
        """ Defines the getter using @property decorator"""
        return self.__symbol

    @symbol.setter
    def symbol(self, value):
        """ Defines the setter with decorator"""
        self.__symbol = value

    # Getter and setter for atomic number
    @property
    def number(self):
        """ Defines the getter using @property decorator"""
        return self.__number

    @number.setter
    def number(self, value):
        """ Defines the setter with decorator and error checking"""
        if value < 0:
            raise ValueError("Negative atomic number is not possible")
        self.__number = value

    def __add__(self, other):
        """ Defines an overload for addition"""
        new_atomic_number = self.__number + other.__number
        new_element = Element(number=new_atomic_number)
        return new_element  # returns an object that is an Element

    def __eq__(self, other):
        """ Defines an overload for equality"""
        if self.__number != other.__number:
            print("1st attribute is not equal")
            return False
        if self.__name != other.__name:
            print("2nd attribute is not equal")
            return False
        if self.__symbol != other.__symbol:
            print("3rd attribute is not equal")
            return False
        # Default
        return True

    def __mul__(self, other):
        """ Defines an overload for multiplication"""
        new_atomic_number = other.__number * self.__number
        new_element = Element(number=new_atomic_number)
        return new_element  # returns an object that is an Element


# Test harness


def main():
    """ Main code """
    hydrogen = Element("Hydrogen", "H", 1)
    oxygen = Element()  # Initialize oxygen
    print(hydrogen)
    print(oxygen)

    # Now define oxygen one by one
    oxygen.name = "Oxygen"
    oxygen.symbol = "O"
    oxygen.number = 16
    print(oxygen)

    h_plus_o = hydrogen + oxygen
    print("hydrogen + oxygen", h_plus_o)

    h_times_o = hydrogen * oxygen
    print("hydrogen * oxygen", h_times_o)

    print("H == H?", hydrogen == hydrogen)
    print("H == O?", hydrogen == oxygen)


if __name__ == '__main__':
    main()
