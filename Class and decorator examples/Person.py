# This only works in python 3.7
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def celebrate_birthday(self):
        self.age += 1

jdoe = Person('John Doe', 42)
jdoe.celebrate_birthday()
print(jdoe)