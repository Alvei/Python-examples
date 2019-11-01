""" person.py
    This only works in python 3.7. """
from dataclasses import dataclass, field, fields
from math import asin, cos, radians, sin, sqrt

from typing import List

""" Used Unicode glyphs like ♠ directly in the source code.
    We could do this because Python supports writing source code in UTF-8 by default."""
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()
EARTH_RADIUS = 6371                             # Earth radius in kilometers

@dataclass
class Person:
    """ Person with name and age attributes. """
    name: str
    age: int

    def celebrate_birthday(self) -> None:
        """ Adds a year to the instance of the class. """
        self.age += 1

def make_french_deck():
    """ Create a traditional 52 card deck. """
    return [PlayingCard(r, s) for s in SUITS for r in RANKS]

@dataclass
class PlayingCard:
    """ Class defining a card with rank (numbers) and suit attributes. """
    rank: str
    suit: str

    def __str__(self):
        """ Clean printing. """
        return f'{self.suit}{self.rank}'

@dataclass
class Deck:
    """ Deck definition as a list of PlayingCard. """
    cards: List[PlayingCard] = field(default_factory=make_french_deck)

    def __repr__(self):
        cards = ', '.join(f'{c!s}' for c in self.cards)
        return f"{self.__class__.__name__}({cards})"

@dataclass
class Position:
    """ Position of a point with longitude and lattitude. """
    name: str
    lon: float = field(default=0.0, metadata={'unit': 'degrees'})
    lat: float = field(default=0.0, metadata={'unit': 'degrees'})

    def distance_to(self, other):
        """ Calculate the distance between one position and another, along the Earth’s
            surface using the haversine formula. """

        lam_1, lam_2 = radians(self.lon), radians(other.lon)
        phi_1, phi_2 = radians(self.lat), radians(other.lat)
        radicand = (sin((phi_2 - phi_1) / 2)**2
                    + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
        return 2 * EARTH_RADIUS * asin(sqrt(radicand))

def main():
    """ Test harness. """
    jdoe = Person('John Doe', 42)
    jdoe.celebrate_birthday()
    print(jdoe)


    print(Position('Null Island'))
    oslo = Position('Oslo', 10.8, 59.9)
    vancouver = Position('Vancouver', -123.1, 49.3)
    print(f"Distance from {oslo.name} to {vancouver.name}: {oslo.distance_to(vancouver):.2f} Km")
    lat_unit = fields(Position)[2].metadata['unit']
    print(f"Latitude Unites: {lat_unit}")

    # Deck with two cards
    queen_of_hearts = PlayingCard('Q', 'Hearts')
    ace_of_spades = PlayingCard('A', 'Spades')
    two_cards = Deck([queen_of_hearts, ace_of_spades])
    print(two_cards)

    ace_of_spades = PlayingCard('A', '♠')
    print(ace_of_spades)

    print("\n", make_french_deck())

if __name__ == "__main__":
    main()
