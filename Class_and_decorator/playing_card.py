""" playing_card.py
    Each card is represented as a tuple of strings denoting the suit and rank.
    Deck is represented as a list of cards. create_deck() creates a regular
    deck of 52 playing cards, and optionally shuffles the cards.
    deal_hands() deals the deck of cards to four players.
    Finally, play() plays the game.
    Using Aliases.
    Inspired from https://realpython.com/python-type-checking/#duck-types-and-protocols """
import random
from pprint import pprint
from typing import List, Tuple, Sequence, TypeVar, Optional

""" Used Unicode glyphs like ♠ directly in the source code because
    Python supports writing source code in UTF-8 by default. """
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
SUITS = '♣ ♢ ♡ ♠'.split()

# Define aliases for type hinting
Card = Tuple[str, str]
Deck = List[Card]

# Create a specific type that will only allow str and Card
Choosable = TypeVar("Choosable", str, Card)

def create_deck(shuffle: bool = False) -> Deck:
    """Create a new deck of 52 cards. """
    deck = [(suit, rank)
            for rank in RANKS
            for suit in SUITS]
    if shuffle:
        random.shuffle(deck)
    return deck

def deal_hands(deck: Deck) -> Tuple[Deck, Deck, Deck, Deck]:
    """Deal the cards in the deck into 4 hands. """
    # list[start:end:stride], therefore deck[0::4], means start at 0 till the end stride=4
    return (deck[0::4], deck[1::4], deck[2::4], deck[3::4])

def choose(items: Sequence[Choosable]) -> Choosable:
    """ Choose and return a random item. """
    return random.choice(items)

def player_order(names: Sequence[str], start: Optional[str]=None) -> Sequence[str]:
    """ Rotate player order so that start goes first. """
    if start is None:
        start = choose(names)
    start_idx = names.index(start)
    return names[start_idx:] + names[:start_idx]

def play():
    """Play a 4-player card game"""
    deck = create_deck(shuffle=True)

    names = "P1 P2 P3 P4".split()

    # Create a dictionary of each players hands
    hands = {name: hand
             for name, hand in zip(names, deal_hands(deck))}

    start_player = choose(names)
    turn_order = player_order(names, start=start_player)
    #pprint(hands)

    while hands[start_player]:
        for name in turn_order:
            card = choose(hands[name])
            hands[name].remove(card)
            print(f"{name}: {card[0] + card[1]:<3} ", end="")
        print()



if __name__ == "__main__":
    play()
