""" person.py
    Inspired from https://realpython.com/python-data-classes/ """
from dataclasses import dataclass, field, fields

@dataclass
class Person:
    """ Person with name and age attributes. """
    name: str
    age: int

    def celebrate_birthday(self) -> None:
        """ Adds a year to the instance of the class. """
        self.age += 1

def main():
    """ Test harness. """
    jdoe = Person('John Doe', 42)
    print(jdoe)
    jdoe.celebrate_birthday()
    print(jdoe)

if __name__ == "__main__":
    main()
