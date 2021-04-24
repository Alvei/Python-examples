""" dataclasses remove boilerplates when defining classes.
    They automatically add generated special methods like __init__(), __repr__(), __eq__()

    Parameters:
    frozen=True:        become immutable and you can use them in hash

    order=Truee:        __lt__, __le__,__gt__ and __ge__ methods will be automagically generated.
                        You can make comparison of objects as if they were tuples of their fields in order.

    field function:     Needs to be imported. If field=False, cannot initialize variable and
                        it will be done by __post_init__()
    __post_init__():    Is called by __init__ to do something.

    asdict():           Needs to be imported. Returns properties as a dict
    astuple():          Needs to be imported. Returns properties as a tuple

    See also the PEP: https://python.org/dev/peps/pep-0557/… ->
    https://towardsdatascience.com/data-classes-in-python-8d1a09c1294b
    - rationale = define classes which exist primarily to store values accessible by attribute lookup
    - support static type checkers"""

from dataclasses import dataclass, field, asdict, astuple


@dataclass
class Bite:
    """ Most basic. """
    number: int
    title: str
    level: str = "Beginner"

    def __post_init__(self):
        """ Method of dataclasses that will be called by the __init__(). """
        self.title = self.title.capitalize()


@dataclass(frozen=True)
class Bite2:
    """ It is immutable and can be hashed. """
    number: int
    title: str
    level: str = "Beginner"


@dataclass
class CircleArea:
    r: int
    pi: float = 3.14

    @property
    def area(self):
        return self.pi * (self.r ** 2)

@dataclass(order=True)
class Vector:
    """ with order=True has built-in comparison but uses tuple. """
    x: int
    y: int

@dataclass(order=True)
class Vector2:
    """ with order=True has built-in comparison.
        Use field and __post_init__ to create more logical comparator. """
    magnitude: float = field(init=False) # By setting to False we say we do not allow initial value
    x: int
    y: int

    def __post_init__(self):
        self.magnitude = (self.x ** 2 + self.y ** 2) ** 0.5


@dataclass
class Employee:
    name: str
    lang: str = 'Python'


@dataclass
class Developer(Employee):
    """ Inherits attributes from Employee. """
    salary: int = 0 # had to put default to salary b/c preceded by lang which had default



def main():

    bite = Bite(1, "sum n numbers")
    print(bite)
    print(repr(bite))

    bite2 = Bite2(1, "sum n numbers")
    # bite2.level = 2 # Cannot change

    a = CircleArea(2)
    print(a)  # output: CircleArea(r=2, pi=3.14)
    print(a.area)  # output: 12.56



    # Silly comparison since it will be a tuple comparison!
    # Where the 1st item of the tuple is first compared
    v1 = Vector(8, 15)
    v2 = Vector(7, 20)
    print(v2 > v1)  # output: False

    v1 = Vector2(9, 12)
    print(v1)  # output: Vector(magnitude=15.0, x=9, y=12)
    v2 = Vector2(8, 15)
    print(v2)  # output: Vector(magnitude=17.0, x=8, y=15)
    print(v2 > v1)  # output: True

    print(f"Using asdict(): {asdict(v1)}")
    print(f"Using astuple(): {astuple(v1)}")

    Halil = Developer('Halil', 'Python', 5000)
    print(Halil)  # output: Developer(name='Halil', lang='Python', salary=5000)


if __name__ == "__main__":
    main()
