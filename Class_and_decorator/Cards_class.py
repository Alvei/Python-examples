""" Cards_class.py
    Each card is represented as a tuple of strings denoting the suit and rank.
    The deck is represented as a list of cards. create_deck() creates a regular
    deck of 52 playing cards, and optionally shuffles the cards. deal_hands() deals the deck of cards to four players.
    Finally, play() plays the game.
    Inspired from https://realpython.com/python-type-checking/#duck-types-and-protocols """
import random
from typing import List

""" Used Unicode glyphs like ♠ directly in the source code.
    We could do this because Python supports writing source code in UTF-8 by default. """
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

def create_deck(shuffle: bool = False) -> List[tuple]:
    """Create a new deck of 52 cards"""
    deck = [(s, r)
            for r in RANKS
            for s in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck):
    """Deal the cards in the deck into 4 hands"""
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)
    names = "P1 P2 P3 P4".split()
    hands = {n: h
            for n, h in zip(names, deal_hands(deck))}
    print(hands)


if __name__ == "__main__":
    play()