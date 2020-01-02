""" Inspired by Python Morsels.
    Write a function that accepts a string and returns a mapping
    (a dictionary or dictionary-like structure) that has words as
    the keys and the number of times each word was seen as the values.

    As a bonus, make sure your function works well with mixed case words.
    Even more of a bonus try to get your function to ignore punctuation outside of words.
    https://treyhunner.com/2015/11/counting-things-in-python/ """

from typing import Dict
from collections import Counter, defaultdict
import re

def count_words(phrase: str) -> Dict[str, int]:
    """ Uses Counter to do the work. Counter objects are a dictionary-like
        object specifically meant for counting the number of times
        things are seen and storing the things as keys and the times
        seen as values. You can think of it as essentially a set that counts
        the number of times it sees each thing, a multi-set of sorts."""

    # .findall() returns a list. Searchs for words, apostrophs or dashes.
    # \b is a forced word break
    search_result = re.findall(r"\b[\w'-]+\b", phrase.lower())
    return Counter(search_result)


def count_words_counter(phrase: str) -> Dict[str, int]:
    """ Uses Counter to do the work. Counter objects are a dictionary-like
        object specifically meant for counting the number of times
        things are seen and storing the things as keys and the times
        seen as values. You can think of it as essentially a set that counts
        the number of times it sees each thing, a multi-set of sorts.
        Does not pass the punctuation test. """
    return Counter(phrase.lower().split())


def count_words_defaultdict_class(phrase: str) -> Dict[str, int]:
    """ Enumerate and count words in a phrase.
        Uses the defaultdict class to do the work.
        Does not pass the punctuation test. """
    count = defaultdict(int)
    for word in phrase.lower().split():
        count[word] += 1
    return count

def count_words_basic(phrase: str) -> Dict[str, int]:
    """ Enumerate and count words in a phrase.
        While the setdefault trick is cool not efficient b/c two loops.
        Does not pass the ¿ test. """

    words = []
    # Strip the punctuation characters for the list created by .split() method.
    for word in phrase.lower().split():
        words.append(word.strip(',;.!?"()'))

    my_dict = {}
    # check to see if my_dict[key] exist. If not, set to zero, if yes, do nothing.
    for word in words:
        my_dict.setdefault(word, 0)
        my_dict[word] += 1

    return my_dict

if __name__ == "__main__":

    phrases = ["oh what a day what a lovely day", "don't stop believing",
            "Oh what a day what a lovely day", "Oh what a day, what a lovely day!",
            "¿Te gusta Python?"]

    print("BASIC")
    [print(count_words_basic(phrase)) for phrase in phrases]

    print("DEFAULTDICT CLASS")
    [print(count_words_defaultdict_class(phrase)) for phrase in phrases]

    print("COUNTER OBJECT")
    [print(count_words_counter(phrase)) for phrase in phrases]

    print("RE OBJECT")
    [print(count_words(phrase)) for phrase in phrases]

