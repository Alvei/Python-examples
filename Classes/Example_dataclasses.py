""" dataclasses remove boilerplates when defining classes. They automatically add generated special methods like __init__() and __repr__() 

See also the PEP: https://python.org/dev/peps/pep-0557/… ->
- rationale = define classes which exist primarily to store values accessible by attribute lookup
- support static type checkers"""

from dataclasses import dataclass


@dataclass
class Bite:
    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        self.title = self.title.capitalize()


@dataclass(frozen=True)
class Bite2:
    number: int
    title: str
    level: str = "Beginner"

    # no __post_init__(self):


def main():
    print("In main")
    bite = Bite(1, "sum n numbers")
    print(repr(bite))

    bite2 = Bite2(1, "sum n numbers")
    bite2.level = 2


if __name__ == "__main__":
    main()
