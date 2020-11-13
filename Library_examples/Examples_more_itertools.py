""" Examples using functions from more_itertools - not a standard library.
https://more-itertools.readthedocs.io/en/stable/
https://martinheinz.dev/blog/16
https://towardsdatascience.com/tour-of-python-itertools-2af84db18a5e
Covers:
        divide()
        partition()
        consecutive_groups()
        side_effect()
        consume()
        collapse()
        split_at()
        bucket()
        map_reduce()
        filter_except()
        sort_together()
"""
import os


def try_divide():
    """Divides iterable into number of sub-iterables while maintaining order.
    Length of the sub-iterables might not be the same, as it
    depends on number of elements being divided and number of sub-iterables"""
    from more_itertools import divide

    group_1, group_2 = divide(2, [1, 2, 3, 4, 5, 6])
    print(f"\nOriginal: {list(range(1, 7))} => ")
    print(f"group1 = {list(group_1)}, group2 = {list(group_2)}")

    data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

    ans = [list(items) for items in divide(3, data)]
    print(f"Divide into subgroups of 3:\n{data}\nans:\n{ans}")
    # [['first', 'second', 'third'], ['fourth', 'fifth'], ['sixth', 'seventh']]


def try_partition():
    """Dividing our iterable using a predicate.
    1- splitting list of dates into recent ones and old ones.
    2- partitioning files based on their extension."""

    from datetime import datetime, timedelta
    from more_itertools import partition

    # Split based on age
    dates = [
        datetime(2015, 1, 15),
        datetime(2020, 1, 16),
        datetime(2020, 11, 7),
        datetime(2019, 2, 1),
        datetime(2020, 11, 2),
        datetime(2018, 2, 4),
    ]

    is_old = lambda x: datetime.now() - x < timedelta(days=30)
    old, recent = partition(is_old, dates)

    print(f"Original: {dates}")
    print(f"Old: {list(old)}")
    print(f"Recent: {list(recent)}")

    # Split based on file extension
    files = [
        "foo.jpg",
        "bar.exe",
        "baz.gif",
        "text.txt",
        "data.bin",
    ]

    ALLOWED_EXTENSIONS = ("jpg", "jpeg", "gif", "bmp", "png")
    is_allowed = lambda x: x.split(".")[1] in ALLOWED_EXTENSIONS

    allowed, forbidden = partition(is_allowed, files)
    print(f"Original: {files}")
    print(f"Allowed: {list(allowed)}")
    print(f"Forbidden: {list(forbidden)}")
    # list(allowed) ['bar.exe', 'text.txt', 'data.bin']
    # list(forbidden) ['foo.jpg', 'baz.gif']


def try_consecutive_group():
    """We have a list of dates, where some of them are consecutive. To be able to
    pass these dates to consecutive_groups function, we first have to convert
    them to ordinal numbers.  Use list comprehension to iterate over groups of
    consecutive ordinal dates created by consecutive_groups and convert them
    back to datetime.datetime using map & from ordinal functions."""

    import datetime
    from more_itertools import consecutive_groups

    dates = [
        datetime.datetime(2020, 1, 15),
        datetime.datetime(2020, 1, 16),
        datetime.datetime(2020, 1, 17),
        datetime.datetime(2020, 2, 1),
        datetime.datetime(2020, 2, 2),
        datetime.datetime(2020, 2, 4),
    ]

    ordinal_dates = []
    for date in dates:
        ordinal_dates.append(date.toordinal())

    groups = [
        list(map(datetime.datetime.fromordinal, group))
        for group in consecutive_groups(ordinal_dates)
    ]
    print("Consecutive Groups: ")
    for group in groups:
        print(f"{group}")


def try_side_effects():
    """ Cause side-effect when iterating over list of items."""
    from more_itertools import side_effect, consume

    num_events = 0
    events = range(0, 10)

    def _increment_num_events(_):
        """ Convenience function. """
        nonlocal num_events
        num_events += 1

    # Iterator that will be consumed
    event_iterator = side_effect(_increment_num_events, events)

    consume(event_iterator)

    print(num_events)


def try_collapse():
    """Allows you to flatten multiple levels of nesting. It also allows you
    to specify base type, so that you can stop flattening with one layer
    of lists/tuples remaining."""
    from more_itertools import collapse

    # Get all nodes of tree into flat list
    tree = [
        40,
        [25, [10, 3, 17], [32, 30, 38]],
        [78, 50, 93],
    ]  # [Root, SUB_TREE_1, SUB_TREE_2, ..., SUB_TREE_n]
    ans = list(collapse(tree))
    print(f"Before: {tree}")
    print(f"After: {ans}")

    # Get flat list of all files and directories
    my_dir = os.getcwd()
    my_tree = list(collapse(list(os.walk(my_dir))))
    print(my_tree)


def try_split_at():
    """Like basic split for strings, but here we have iterable instead of
    string and predicate function instead of delimiter."""

    from more_itertools import split_at

    lines = [
        "erhgedrgh",
        "erhgedrghed",
        "esdrhesdresr",
        "ktguygkyuk",
        "-------------",
        "srdthsrdt",
        "waefawef",
        "ryjrtyfj",
        "-------------",
        "edthedt",
        "awefawe",
    ]

    ans = list(split_at(lines, lambda x: "-------------" in x))
    #  [['erhgedrgh', 'erhgedrghed', 'esdrhesdresr', 'ktguygkyuk'],
    # ['srdthsrdt', 'waefawef', 'ryjrtyfj'], ['edthedt', 'awefawe']]
    print(ans)


def try_bucket():
    """Split iterable into multiple buckets based on some condition.
    Creates child iterables by splitting input iterable using key function."""
    from more_itertools import bucket

    class Cube:
        """ Cube """

        pass

    class Circle:
        """ Circle """

        pass

    class Triangle:
        """ Triangle """

        pass

    shapes = [Circle(), Cube(), Circle(), Circle(), Cube(), Triangle(), Triangle()]

    # Bucket object s, <more_itertools.more.bucket object at 0x7fa65323f210>
    shape_bucket = bucket(shapes, key=lambda x: type(x))

    print(f"\nCube: {list(shape_bucket[Cube])}")
    #  [<__main__.Cube object at 0x7f394a0633c8>,
    # <__main__.Cube object at 0x7f394a063278>]
    print(f"\nCircle: {list(shape_bucket[Circle])}")
    # [<__main__.Circle object at 0x7f394a063160>,
    # <__main__.Circle object at 0x7f394a063198>,
    # <__main__.Circle object at 0x7f394a063320>]


def try_map_reduce():
    """Allows us to specify 3 functions: key function (for categorizing),
    value function (for transforming) and finally reduce function."""
    from more_itertools import map_reduce

    data = "Sentence has words of various lengths, short ones & long ones".split()
    print(f"\nData: {data}")

    keyfunc = lambda x: len(x)
    result = map_reduce(data, keyfunc)
    print(f"keyfunc = len(x): {result}")
    # defaultdict(None, {
    #   4: ['This', 'both', 'ones', 'long', 'ones'],
    #   8: ['sentence'],
    #   3: ['has', 'it,', 'and'],
    #   5: ['words', 'short'],
    #   2: ['of', 'in'],
    #   7: ['various', 'lengths']})

    valuefunc = lambda x: 1
    result = map_reduce(data, keyfunc, valuefunc)
    print(f"valuefunct = 1: {result}")
    # defaultdict(None, {
    #   4: [1, 1, 1, 1, 1],
    #   8: [1],
    #   3: [1, 1, 1],
    #   5: [1, 1],
    #   2: [1, 1],
    #   7: [1, 1]})

    reducefunc = sum
    result = map_reduce(data, keyfunc, valuefunc, reducefunc)
    print(f"reducefunct = sum: {result}")
    # defaultdict(None, {
    #   4: 5,
    #   8: 1,
    #   3: 3,
    #   5: 2,
    #   2: 2,
    #   7: 2})


def try_sort_together():

    """
        Name     |    Address    | Date of Birth |   Updated At
    ----------------------------------------------------------------
    John           |               |  1994-02-06   |   2020-01-06
    Ben            |               |  1985-04-01   |   2019-03-07
    Andy           |               |  2000-06-25   |   2020-01-08
    Mary           |               |  1998-03-14   |   2018-08-15
    """

    from more_itertools import sort_together

    cols = [
        ("John", "Ben", "Andy", "Mary"),
        ("1994-02-06", "1985-04-01", "2000-06-25", "1998-03-14"),
        ("2020-01-06", "2019-03-07", "2020-01-08", "2018-08-15"),
    ]

    ans = sort_together(cols, key_list=(1, 2))  # sort based on col 1 then 2
    #  [('Ben', 'John', 'Mary', 'Andy'), ('1985-04-01', '1994-02-06',
    # '1998-03-14', '2000-06-25'), ('2019-03-07', '2020-01-06',
    # '2018-08-15', '2020-01-08')]
    print(ans)


def try_filter_except():
    """Scenario: Received mixed data, that contains text and numb. and all
    of in string form. You want to work only with numbers (floats/ints)."""
    from more_itertools import filter_except

    data = ["1.5", "6", "not-important", "11", "1.23E-7", "remove-me", "25"]

    ans = map(float, filter_except(float, data, TypeError, ValueError))
    print(f"Original data: {data}")
    print(f"Keep only the float: {list(ans)}")
    #  [1.5, 6.0, 11.0, 1.23e-07, 25.0]


def main():
    """ Test Harness"""
    # try_divide()
    # try_partition()
    # try_consecutive_group()
    # try_side_effects()
    # try_collapse()
    # try_split_at()
    # try_bucket()
    # try_map_reduce()
    # try_sort_together()
    try_filter_except()


if __name__ == "__main__":
    main()
