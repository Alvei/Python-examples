# Inspired from mCoding
import dataclasses
import inspect
from dataclasses import dataclass, field
from pprint import pprint

#import attr


class ManualComment:
    """ Very combursom creation of a data encapsulation class. """
    def __init__(self, id: int, text: str):
        """ Constructor. """
        self.id: int = id
        self.text: str = text

    def __repr__(self):
        return "{}(id={}, text={})".format(self.__class__.__name__, self.id, self.text)

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) == (other.id, other.text)
        else:
            return NotImplemented

    def __ne__(self, other):
        result = self.__eq__(other)
        if result is NotImplemented:
            return NotImplemented
        else:
            return not result

    def __hash__(self):
        return hash((self.__class__, self.id, self.text))

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) < (other.id, other.text)
        else:
            return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) <= (other.id, other.text)
        else:
            return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) > (other.id, other.text)
        else:
            return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.id, self.text) >= (other.id, other.text)
        else:
            return NotImplemented

# Writing frozen makes it immutable and therefore hashable
# new methods are automatically created. 
# Writing order, adds methods to facilitate comparisons
@dataclass(frozen=True, order=True)
class Comment:
    id: int
    text: str = ""
    replies: list[int] = field(default_factory=list, repr=False, compare=False)


# @attr.s(frozen=True, order=True, slots=True)
# class AttrComment:
#     id: int = 0
#     text: str = ""


def main():
    comment = Comment(1, "I just subscribed!")
    print(f"\ndataclass:\t\t{comment}")

    # Use dataclasses methods to convert
    print(f"Convert to tuple:\t{dataclasses.astuple(comment)}")
    print(f"Convert to dict:\t{dataclasses.asdict(comment)}")


    copy = dataclasses.replace(comment, id=3)
    print(f"\nCopy with replace:\t{copy}\n")

    pprint(inspect.getmembers(Comment, inspect.isfunction))


if __name__ == '__main__':
    main()