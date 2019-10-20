
"""
Experiment with getter and setter decorators
Created on Sat Mar 10 15:03:06 2018

"""


class Duck():
    """ Simple class that uses decorators
        @property goes before the getter method
        @name.setter goes before the setter method
        It usese name mangling for privacy by using self.__name
    """

    def __init__(self, inputName):
        self.__name = inputName

        @property
        def name(self):
            print('\tInside the getter')
            return self.__name

        @name.setter
        def name(self, inputName):
            print('\tInside the setter')
            self.__name = inputName


fowl = Duck("Howard")

fowl.name = "Donald"

print(fowl.name)


class Circle():
    """ Simple circle class to show the use of @property decorator
        Cool to note that the diameter constantly change with the change in radius
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
print(f"Radius {c.radius} and Diameter {c.diameter}")

c.radius = 7
print(f"Radius {c.radius} and Diameter {c.diameter}")


class A():
    """ Simple class to show how to create a class specific vs.
        instance method()
        Need to use the @classmethod decorator and use cls to refer back to the class
    """
    count = 0

    def __init__(self):
        A.count += 1

    def exclaim(sefl):
        print("\tI'm in A!")

    @classmethod
    def kids(cls):
        print(f"A has {cls.count} little objects")


easy_a = A()
brezzy_a = A()
whezzy_a = A()
A.kids()  # call the class method


class CoyoteWeapon():
    """ Simple class to show the use of the @staticmethod decorator.
        It can be called from an uninstantiated class object. """
    @staticmethod
    def commercial():
        print("This CoyoteWeapon has been brought to you by Acme")


CoyoteWeapon.commercial()
