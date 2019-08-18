""" Uses class attributes and instance attributes
    Greate example of decorator in classes
    https://www.programiz.com/python-programming/property
"""


class Celsius(object):
    """ Class definition for Celcius. It has a class counter"""

    count = 0   # Class attribute

    def __init__(self, temperature=0):
        """ Using __temperature we are hidding the variable temperature"""
        self.__temperature = temperature
        Celsius.count += 1  # Increment the class attribute

    def to_farh(self):
        """ Convert Celsius to Farheneit"""
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        """ Defines the getter for private variable using @property"""
        print("Getting value")
        return self.__temperature   # Uses the private name

    @temperature.setter
    def temperature(self, value):
        """ Defines the setter with decorator and error checking"""
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self.__temperature = value  # Setting private name

    @classmethod
    def print_count_instances(cls):
        """ Keeps track of the number of instances of the class"""
        print("Celsius has", cls.count, "objects")


# Test harness
# #############

def main():
    """ Main code """
    num1 = Celsius(55)      # Initialize with 55

    print(num1.temperature)  # Answer is 55 ausing the getter function

    num1.temperature = 66    # Will use the setter function

    print(num1.temperature)     # Answer is 55 using the getter function
    num2 = Celsius(30)
    num3 = Celsius(80)
    Celsius.print_count_instances()


if __name__ == '__main__':
    main()
