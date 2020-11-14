""" Examples_collections.py
Counter
defaultdict
OrderedDict
deque
ChainMap
namedtuple()

https://stackabuse.com/introduction-to-pythons-collections-module/
https://book.pythontips.com/en/latest/collections.html
https://towardsdatascience.com/pythons-collections-module-high-performance-container-data-types-cb4187afb5fc
https://docs.python.org/3/library/collections.html
"""
from collections import (
    Counter,
    defaultdict,
    OrderedDict,
    deque,
    ChainMap,
    namedtuple,
)
import json


def try_counter():
    """Counter is a subclass of the dictionary object.
    Takes an iterable or a mapping as the argument and returns a
    Dictionary. In this dictionary, a key is an element in the
    iterable or the mapping and value is the number of times that
    element exists in the iterable or the mapping.
    Counter has three additional functions:
      elements(): Returns a list containing all the elements Counter object
      most_common([n]): returns a dictionary which is ordered
      subtract([interable-or-mapping]): takes iterable (list) or mapping (dictionary)
                        as an argument and deducts elements count using that argument"""

    my_list = ["a", "b", "c", "d", "d", "d", "b"]
    my_count = Counter(my_list)

    print(f"Counter: {my_count}")
    print(f"Counter elements: {my_count.elements()}")
    print(f"Counter elements: {list(my_count.elements())}")
    print(f"Counter most common: {list(my_count.most_common())}")

    dict_a = {"A": 3.0, "C": 4.0, "B": 6.0}
    dict_b = {"A": 3.0, "C": 5.0, "D": 1.0}

    counter_a = Counter(dict_a)
    counter_a.subtract(dict_b)
    print(f"\nsustracted = {counter_a}")
    # Counter({'B': 6.0, 'A': 0.0, 'C': -1.0, 'D': -1.0})


def try_defaultdict():
    """The defaultdict works exactly like a python dictionary, except for it does not
    throw KeyError when you try to access a non-existent key. Instead, it initializes
    the key with the element of the data type that you pass as an argument at the creation
    of defaultdict. The data type is called default_factory."""

    nums = defaultdict(int)  # Defining the default
    nums["one"] = 1
    nums["two"] = 2
    print(nums["three"])
    count = defaultdict(int)
    names_list = (
        "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split()
    )
    for name in names_list:
        count[name] += 1
    print(f"Counting names: {count}")

    colours = (
        ("Yasoob", "Yellow"),
        ("Ali", "Blue"),
        ("Arham", "Green"),
        ("Ali", "Black"),
        ("Yasoob", "Red"),
        ("Ahmed", "Silver"),
    )

    favourite_colours = defaultdict(list)  # Defining the default

    for name, colour in colours:
        favourite_colours[name].append(colour)

    print(f"List of colours: {favourite_colours}")

    # output
    # defaultdict(<type 'list'>,
    #    {'Arham': ['Green'],
    #     'Yasoob': ['Yellow', 'Red'],
    #     'Ahmed': ['Silver'],
    #     'Ali': ['Blue', 'Black']
    # })

    # One other very important use case is when you are appending
    # to nested lists inside a dictionary.
    tree = lambda: defaultdict(tree)
    some_dict = tree()
    some_dict["colours"]["favourite"] = "yellow"
    print(json.dumps(some_dict))


def try_ordereddict():
    """dictionary where keys maintain the order in which they are inserted, which means
    if you change the value of a key later, it will not change the position of the key"""
    my_list = ["a", "c", "c", "a", "b", "a", "a", "b", "c"]
    cnt = Counter(my_list)
    ordict = OrderedDict(cnt.most_common())
    for key, value in ordict.items():
        print(key, value)


def try_deque():
    """ The deque is a list optimized for inserting and removing items. """
    my_list = ["a", "b", "c", "a"]
    deq = deque(my_list)
    print(f"Original list: {deq}")
    deq.append("d")
    deq.appendleft("e")
    print(f"New list with e as prefix and d as sufix: {deq}")
    deq.pop()
    deq.popleft()
    print(f"New list after pop() and popleft(): {deq}")
    print(f"Counting how often a is present in list: {deq.count('a')}")


def try_chainmap():
    """ChainMap is used to combine several dictionaries or mappings.
    It returns a list of dictionaries."""
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "b": 4}
    print(f"dict1={dict1} and dict2={dict2}")
    chain_map = ChainMap(dict1, dict2)
    print(f"ChainMap result: {chain_map.maps}")
    print(f"What is value for key=a: {chain_map['a']}")
    print(f"What is value for key=b: {chain_map['b']} which is the first key found.")
    dict2["c"] = 5
    print(f"ChainMap result after updating c=5: {chain_map.maps}")
    print(list(chain_map.keys()))
    print(list(chain_map.values()))
    dict3 = {"e": 5, "f": 6}
    new_chain_map = chain_map.new_child(dict3)
    # Notice that new dictionary is added to the beginning of ChainMap list.
    print(f"ChainMap result: {new_chain_map.maps}")


def try_namedtuple():
    """The namedtuple() returns a tuple with names for each position in the tuple.
    One of the biggest problems with ordinary tuples is that you have to remember
    the index of each field of a tuple object. This is obviously difficult.
    The namedtuple was introduced to solve this problem."""

    Student = namedtuple("Student", "fname, lname, age")  # Define the tuple keys
    stud1 = Student("John", "Clarke", "13")
    print(stud1.fname)
    stud2 = Student._make(["Adam", "joe", "18"])  # Using a list to initialize
    print(stud2)
    stud3 = stud1._asdict()  # Create an OrderedDict
    print(f"type: {type(stud3)} {stud3}")
    stud2 = stud1._replace(age="14")
    print(f"s1: {stud1}")
    print(f"s2=s1 with age = 14: {stud2}")
    Animal = namedtuple("Animal", "name age type")
    perry = Animal(name="perry", age=31, type="cat")
    print(perry.name, perry[0])


def main():
    """ Test Harness. """
    # try_counter()
    # try_defaultdict()
    # try_ordereddict()
    # try_deque()
    # try_chainmap()
    try_namedtuple()


if __name__ == "__main__":
    main()
