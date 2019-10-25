# This only works in python 3.7
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

    def celebrate_birthday(self) -> None:
        self.age += 1

def main():
    jdoe = Person('John Doe', 42)
    jdoe.celebrate_birthday()
    print(jdoe)

if __name__ == "__main__":
    main()