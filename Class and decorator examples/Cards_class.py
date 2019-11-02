""" Cards_class.py
    Inspired from https://realpython.com/python-data-classes/ """
from dataclasses import dataclass, field, fields
from typing import List

""" Used Unicode glyphs like ♠ directly in the source code.
    We could do this because Python supports writing source code in UTF-8 by default. """
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def make_french_deck():
    """ Create a traditional 52 card deck. """
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass(order=True)
class PlayingCard:
    """ Class defining a card with rank (numbers) and suit attributes. """
    sort_index: int = field(init=False, repr=False)
    rank: str
    suit: str

    def __post_init__(self):
        self.sort_index = (RANKS.index(self.rank) * len(SUITS)
                           + SUITS.index(self.suit))

    def __str__(self):
        """ Clean printing. """
        return f'{self.suit}{self.rank}'

@dataclass()
class Deck:
    """ Deck definition as a list of PlayingCard. Use field() to set default. """
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        """Note the !s specifier in the {c!s} format string.
           It means that we explicitly want to use the str() representation of each PlayingCard. """
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f"{self.__class__.__name__}({cards})"

def main():
    """ Test harness. """

    # Deck with two cards
    queen_of_hearts = PlayingCard('Q', '♡')
    ace_of_spades = PlayingCard('A', '♠')
    two_cards = Deck([queen_of_hearts, ace_of_spades])
    print(two_cards)

    print("\n", Deck(), "\n")
    print("\n", Deck(sorted(make_french_deck())), "\n")

    ace_of_spades = PlayingCard('A', '♠')
    queen_of_hearts = PlayingCard('Q', '♡')
    print(f"{ace_of_spades} {ace_of_spades > queen_of_hearts} {queen_of_hearts}")

if __name__ == "__main__":
    main()
