""" Cards_class.py
    Each card is represented as a tuple of strings denoting the suit and rank.
    Deck is represented as a list of cards. create_deck() creates a regular
    deck of 52 playing cards, and optionally shuffles the cards.
    deal_hands() deals the deck of cards to four players.
    Finally, play() plays the game.
    Inspired from https://realpython.com/python-type-checking/#duck-types-and-protocols """
import random
from pprint import pprint
from typing import List, Tuple

""" Used Unicode glyphs like ♠ directly in the source code because
    Python supports writing source code in UTF-8 by default. """
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def create_deck(shuffle: bool = False) -> List[Tuple[str, str]]:
    """Create a new deck of 52 cards. """
    deck = [(suit, rank)
            for rank in RANKS
            for suit in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: List[Tuple[str, str]]) -> Tuple[List[Tuple[str, str]], \
        List[Tuple[str, str]], List[Tuple[str, str]], List[Tuple[str, str]]]:
    """Deal the cards in the deck into 4 hands"""
    # list[start:end:stride], therefore deck[0::4], means start at 0 till the end stride=4
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)

    names = "P1 P2 P3 P4".split()

    # Create a dictionary of each players hands
    hands = {name: hand
             for name, hand in zip(names, deal_hands(deck))}
    pprint(hands)


if __name__ == "__main__":
    play()
