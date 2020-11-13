""" Series of examples using functions from itertools.
An iterable: object that can return an ITERATOR. It has an __iter__ method that returns an iterator.
             Anything you can loop over with a for loop. Sequences are very commmon iteratbles
             (e.g., list, tuples and strings). Sequences have a unique features: they can be
             indexed starting at 0, they have a length and they can be sliced.
             Sets, dictionaries, files and ITERATORS are also iterables but not sequences.

An iterator: object with a __next__ method. It has a state and once consumed they are gone.
             The only thing you can do with iterator is ask them for the next item using
             __next__. Generators, zip, map, filter, file objiects are iterators.
             They have no length and cannot be indexed.

multiple assignment, star expression and many built-in functions rely on iterators.

Infinite Iterators: count(), cycle(), repeat()
Terminating Iterators: chain(), dropwhile(), takewhile(), groupby(), tee()
Combinatoric Iterators: permutations(), combinations(),

Resources:
https://opensource.com/article/18/3/loop-better-deeper-look-iteration-python
https://towardsdatascience.com/tour-of-python-itertools-2af84db18a5e
https://medium.com/fintechexplained/advanced-python-itertools-library-the-gem-of-python-language-99da37dfcca2
"""
import sys
import itertools as it
import operator
import time
from typing import Iterable, Iterator


def try_zip_longest() -> None:
    """ Examples. """

    names = "Pierre Marc Ottawa Eric Martin Ozzy".split()
    countries = "Australia Canada Global France".split()

    # This will truncate the lists since they are not of the same lenght
    ans_zip = zip(names, countries)
    print(f"Type for zip: {type(ans_zip)}")
    ans = list(ans_zip)
    print(f"First: {ans}")

    # Adding  Name in shortest Iterator = countries
    ans = list(it.zip_longest(names, countries))
    print(f"Second: {ans}")

    # Same but with a fillvalue other than None
    ans = list(it.zip_longest(names, countries, fillvalue="Worldwide"))
    print(f"Third: {ans}")


def try_repeat():
    """ Repeat an item. """

    to_repeat = "hello"
    how_many_times = 5
    my_repeater = it.repeat(to_repeat, how_many_times)
    print(f"type repeat object: {type(my_repeater)}")
    for i in my_repeater:
        print(i)


def try_compress() -> None:
    """Takes iterable and boolean selector and outputs items
    of the iterable where the corresponding element in the selector is True."""

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
    ans = it.compress(dates, bools)
    print(f"type for compress: {type(ans)}")
    print(list(ans))  # Compress returns iterator!
    #  ['2020-02-04', '2020-01-24', '2020-02-10', '2020-02-15']


def try_accumulate() -> None:
    """ This function accumulates results of some (binary) function. """

    data = [3, 4, 1, 3, 5, 6, 9, 0, 1]
    print(data)

    ans = list(it.accumulate(data, max))  # running maximum
    #  [3, 4, 4, 4, 5, 6, 9, 9, 9]
    print(ans)

    ans2 = list(it.accumulate(range(1, 11), operator.mul))  # Factorial
    #  [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 36
    print(ans2)


def try_chain():
    """This method lets us create an iterator that returns elements from
    all of the input iterables in a sequence until there are no elements left.
    Hence, it can treat consecutive sequences as a single sequence."""

    chains = it.chain([1, 2, 3], ["a", "b", "c"], ["End"])
    for index in chains:
        print(index)


def try_cyle() -> None:
    """ Cycles through an iterable. """

    for cyc in it.cycle("/-\|"):
        print(cyc, end="\r")
        time.sleep(0.2)


def pairwise(iterable: Iterable) -> Iterator:
    """tee creates multiple iterators from one, which allows us to remember what happened.
    s -> (s0, s1), (s1, s2), (s2, s3), ..."""

    var1, var2 = it.tee(iterable, 2)
    next(var2, None)
    return zip(var1, var2)


def try_tee():
    """Split an iterable and generate new iterables from the input.
    The output is also an iterator that returns the iterable for the given number of items."""

    iterable = ["FM", "AM"]
    new_iterable = it.tee(iterable, 5)
    for i in new_iterable:
        print(list(i))


def try_dropwhile():
    """Pass an iterable along with a condition and this function will start evaluating
    the condition on each of the elements until the condition returns False for an element.
    As soon as the condition evaluates to False for an element, this function will then
    return the rest of the elements of the iterable."""

    jobs = ["job1", "job2", "job3", "job10", "job4", "job5"]
    ans = it.dropwhile(lambda x: len(x) == 4, jobs)
    print(f"type dropwhile: {type(ans)}")
    for i in ans:
        print(i)


def try_takewhile():
    """returns all of the elements of an iterable until the first condition returns False
    and then it does not return any other element."""

    jobs = ["job1", "job2", "job3", "job10", "job4", "job5"]
    ans = it.takewhile(lambda x: len(x) == 4, jobs)
    for i in ans:
        print(i)


def try_groupby():
    """Constructs an iterator after grouping the consecutive elements of an iterable.
    The function returns an iterator of key, value pairs where the key is the group key and
    the value is the collection of the consecutive elements that have been grouped by the key."""

    iterable = "FFFAARRHHHAADDMMAAALLIIKKK"
    my_groupby = it.groupby(iterable)
    for key, group in my_groupby:
        print("Key:", key)
        print("Group:", list(group))


def try_islice():
    """ Slice any iteratable. """

    log_file = ["first line", "second line", "third line", "fourth line"]

    # Traditional implention
    for i, line in enumerate(log_file):
        if i >= 3:
            break
        print(line)

    # Lazy implementation to grab first 3 lines
    subset = it.islice(log_file, 3)
    for line in subset:
        print(line)


def try_permutations():
    """ create an iterator that returns successive permutations of elements in input iterable. """

    iterable = "FM1"
    length = 3
    permutations = it.permutations(iterable, length)

    print(f"Iterable: {iterable}")
    for permutation in permutations:
        print(permutation)


def try_combinations():
    """Construct an iterator to return sub-sequences of elements of a given length.
    Treat elements as unique based on their position and only the distinct elements are returned."""

    iterable = "FM1"
    length = 2
    combinations = it.combinations(iterable, length)

    print(f"Iterable: {iterable}")
    for combination in combinations:
        print(combination)


def main():
    """ Test harness. """

    lots_of_fours = it.repeat(4, times=100_000_000)
    lots_of_fours_long = [4] * 100_000_000
    print(f"\nrepeat: {type(lots_of_fours)} size: {sys.getsizeof(lots_of_fours)}")
    print(f"list: {type(lots_of_fours_long)} size: {sys.getsizeof(lots_of_fours_long)}")
    try_zip_longest()
    # try_compress()
    # try_accumulate()
    # try_islice()

    # ### Infinite Iterators ###
    # try_repeat()
    # try_cyle()

    # ### Terminating Iterators ###
    # try_chain()
    # s = ["s0", "s1", "s2", "s3"]
    # print(list(pairwise(s)))
    # try_tee()
    # try_dropwhile()
    # try_takewhile()
    # try_groupby()

    # ### Combinatoric Iterators ###
    # try_permutations()
    try_combinations()


if __name__ == "__main__":
    main()
