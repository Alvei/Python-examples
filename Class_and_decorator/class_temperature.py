""" Uses class attributes and instance attributes
    Greate example of decorator in classes
    https://www.programiz.com/python-programming/property
"""


class Celsius():
    """ Class definition for Celcius. It has a class counter"""

    count: int = 0   # Class attribute

    def __init__(self, temperature: float=0) -> None:
        """ Using __temperature we are hidding the variable temperature"""
        self.__temperature: float = temperature
        Celsius.count += 1  # Increment the class attribute

    def to_farh(self) -> float:
        """ Convert Celsius to Farheneit"""
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self) -> float:
        """ Defines the getter for private variable using @property"""
        print("\tGetting value")
        return self.__temperature   # Uses the private name

    @temperature.setter
    def temperature(self, value: float) -> None:
        """ Defines the setter with decorator and error checking"""
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("\tSetting value")
        self.__temperature = value  # Setting private name

    @classmethod
    def print_count_instances(cls) -> None:
        """ Keeps track of the number of instances of the class"""
        print(f"Celsius has {cls.count} objects")

    def __str__(self) -> str:
        return str(self.__temperature)


def main():
    """ Main code """
    print(f"***Initialize with {55}***")
    num1 = Celsius(55)
    print(f"The temperature is {num1.temperature}")  # Answer is 55 using the getter function

    print(f"***Using the setter with {66}***")
    num1.temperature = 66
    print(f"The temperature is {num1.temperature}")  # Answer is 66 using the getter function

    num2 = Celsius(30.)
    num3 = Celsius(80.)
    print(f"two first temperatures: {num2}, {num3}")
    Celsius.print_count_instances()


if __name__ == '__main__':
    main()
