""" Series of examples using functions from more_itertools - not a standard library.
https://towardsdatascience.com/tour-of-python-itertools-2af84db18a5e
"""
from typing import Iterable, Iterator


def try_divide():
    """ Divides iterable into number of sub-iterables.
    the length of the sub-iterables might not be the same,
    as it depends on number of elements being divided and number of sub-iterables """
    from more_itertools import divide

    data = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]

    ans = [list(l) for l in divide(3, data)]
    print(f"Divide into subgroups of 3:\n{data}\nans:\n{ans}")
    #  [['first', 'second', 'third'], ['fourth', 'fifth'], ['sixth', 'seventh']]


def main():
    """ Test Harness"""
    try_divide()


if __name__ == "__main__":
    main()
