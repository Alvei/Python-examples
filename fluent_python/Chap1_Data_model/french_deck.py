""" french_deck.py
    Inspired from Fluent Python.
    https://github.com/fluentpython/example-code/blob/master/01-data-model/vector2d.py
    Namedtuple makes your tuples self-document. You can easily understand what is going
    on by having a quick glance at your code. And as you are not bound to use integer
    indexes to access members of a tuple, it makes it more easy to maintain your code.
    Moreover, as namedtuple instances do not have per-instance dictionaries, they are
    lightweight and require no more memory than regular tuples. This makes them faster
    than dictionaries. However, do remember that as with tuples, attributes in namedtuples
    are immutable.
    By implementing the special methods __len__ and __getitem__, our FrenchDeck behaves like
    a standard Python sequence, allowing it to benefit from core language features (e.g.,
    iteration and slicing). Iteration is often implicit. If a collection has no __contains__
    method, the in operator does a sequential scan.
"""
import collections          # To get namedtuple
from random import choice   # To help with picking random cards

# Leverage the namedtuple data structure for the basic class
# With namedtuples you don’t have to use integer indexes for accessing members of a tuple.
# You can think of namedtuples like dictionaries but unlike dictionaries they are immutable.
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    """ Create a class to support cards. Two class variables: ranks, suits. """
    # List comprehension to create the numbers, then add the figures.
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    # Quick way to create a suit
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self) -> None:
        """ Initialize the deck. Leverage list comprehension. The deck is a list of 52 cards. """
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self) -> int:
        """ Size of the deck of cards. """
        return len(self._cards)

    def __getitem__(self, position: int) -> Card:
        """ Returns the card in a position.
            It delegrate to the [] operator the heavy work.
            It therefore supports slicing, iterate, and reverse operator. """
        return self._cards[position]

# Global variable
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card: Card) -> int:
    """ Here is a function that ranks cards by that rule,
        returning 0 for the 2 of clubs and 51 for the ace of spades.
        The power of the choices of data structure comes through in the calculation of ans."""
    no_suits = len(suit_values) # answer is always 4

    """ card.rank accesses the tuple rank attribute
        FrenchDeck.ranks.index() returns the location in a specific suit.
        rank_value is an int """
    rank_value = FrenchDeck.ranks.index(card.rank)

    """ Calculate the location across the full deck. The order is all the rank = 2 first
        then all the rank = 3. Then for each rank it is club->diamond->hearts->spades.
        ans = location in a suit * 4 + value of suits
        E.g, for 5 of heart. 5 becomes 3 because we start counting at 2 -> index 0, heart = 2
            ans = 3 * 4 + 2 = 14
        E.g., for J of spade. J becomes 9 (11-2) and spade is 3
            ans = 9 * 4 + 3 = 39
    """
    ans = rank_value * no_suits + suit_values[card.suit]
    #print(f"{card}: {rank_value*no_suits} + {suit_values[card.suit]} = {ans}")
    return ans

def main():
    """ Simple main program. """
    base_card = Card('7', 'diamonds')
    # Access the attributes of the namedtuple
    print(f"\nCard: {base_card}, rank: {base_card.rank}, suit: {base_card.suit}")

    deck = FrenchDeck()
    print(f"Random card: {choice(deck)}\n")

    """ # __getitem__ leverages iterator operator
    for card in deck:
        print(card)

    # __getitem__ leverages reserved function
    print("\nREVERSED")
    for card in reversed(deck):
        print(card) """

    # Print all the cord in sorted order by rank 1st
    for card in sorted(deck, key=spades_high):
        print(card)

if __name__ == "__main__":
    main()
