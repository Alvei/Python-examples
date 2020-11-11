""" Series of examples using functions from itertools.
https://towardsdatascience.com/tour-of-python-itertools-2af84db18a5e
"""
from typing import Iterable, Iterator


def try_zip_longest() -> None:
    """ Examples. """
    from itertools import zip_longest

    names = "Pierre Marc Ottawa Eric Martin Ozzy".split()
    countries = "Australia Canada Global France".split()

    # This will truncate the lists since they are not of the same lenght
    ans = list(zip(names, countries))
    print(f"First: {ans}")

    # Adding  Name in shortest Iterator = countries
    ans = list(zip_longest(names, countries))
    print(f"Second: {ans}")

    # Same but with a fillvalue other than None
    ans = list(zip_longest(names, countries, fillvalue="Worldwide"))
    print(f"Third: {ans}")


def try_compress() -> None:
    """ Takes iterable and boolean selector and outputs items
    of the iterable where the corresponding element in the selector is True. """
    from itertools import compress

    dates = [
        "2020-01-01",
        "2020-02-04",
        "2020-02-01",
        "2020-01-24",
        "2020-01-08",
        "2020-02-10",
        "2020-02-15",
        "2020-02-11",
    ]

    # Second sequence
    counts = [1, 4, 3, 8, 0, 7, 9, 2]

    # Convert second sequence to boolean
    bools = [n > 3 for n in counts]
    print(list(compress(dates, bools)))  # Compress returns iterator!
    #  ['2020-02-04', '2020-01-24', '2020-02-10', '2020-02-15']


def try_accumulate() -> None:
    """ This function accumulates results of some (binary) function. """
    from itertools import accumulate
    import operator

    data = [3, 4, 1, 3, 5, 6, 9, 0, 1]
    print(data)

    ans = list(accumulate(data, max))  # running maximum
    #  [3, 4, 4, 4, 5, 6, 9, 9, 9]
    print(ans)

    ans2 = list(accumulate(range(1, 11), operator.mul))  # Factorial
    #  [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 36
    print(ans2)


def try_cyle() -> None:
    """ """
    # Cycling through players
    from itertools import cycle

    players = ["John", "Ben", "Martin", "Peter"]

    next_player = cycle(players).__next__
    player = next_player()
    #  "John"

    player = next_player()
    #  "Ben"
    #  ...

    # Infinite Spinner
    import time

    for c in cycle("/-\|"):
        print(c, end="\r")
        time.sleep(0.2)


def pairwise(iterable: Iterable) -> Iterator:
    """ tee creates multiple iterators from one, which allows us to remember what happened.
    s -> (s0, s1), (s1, s2), (s2, s3), ...
    """
    from itertools import tee

    a, b = tee(iterable, 2)
    next(b, None)
    return zip(a, b)


def main():
    """ Test harness. """
    # try_zip_longest()
    # try_compress()
    # try_accumulate()
    # try_cyle()
    s = ["s0", "s1", "s2", "s3"]
    print(list(pairwise(s)))


if __name__ == "__main__":
    main()
