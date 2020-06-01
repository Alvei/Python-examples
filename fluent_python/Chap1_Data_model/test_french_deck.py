""" test_french_deck.py
    Data Structure:
        Deck is a list of 52 Cards
        Card is a namedtuple
"""

from french_deck import FrenchDeck, Card
import collections          # To get namedtuple
from random import choice   # To help with picking random cards

def test_create_card():
    """ Test creation of a Card. """
    card1 = Card('7', 'hearts')
    card2 = Card('J', 'diamonds')

    assert card1 == Card(rank='7', suit='hearts')
    assert card2 == Card(rank='J', suit='diamonds')
    assert card1 != Card(rank='2', suit='hearts')

def test_create_deck():
    """ Test creation of Deck. """
    deck = FrenchDeck()
    assert len(deck) == 52
    assert Card('Q', 'hearts') in deck              # Leverage existing _contains__ operator
    assert Card('Z', 'clubs') not in deck           # Leverage existing _contains__ operator
    assert deck[0] == Card(rank='2', suit='spades')
    assert deck[-1] == Card(rank='A', suit='hearts')

def test_deck_getitem():
    """ Leverages the slicing operator that was defined. """
    deck = FrenchDeck()
    # First 3 cards for first suit - Spades
    assert deck[:3] == [Card(rank='2', suit='spades'),
                        Card(rank='3', suit='spades'),
                        Card(rank='4', suit='spades')]
    # Figures for 1st suit
    assert deck[9:13] == [Card(rank='J', suit='spades'),
                        Card(rank='Q', suit='spades'),
                        Card(rank='K', suit='spades'),
                        Card(rank='A', suit='spades')]
    # First 3 cards for 2nd suit - Diamonds
    assert deck[13:16] == [Card(rank='2', suit='diamonds'),
                        Card(rank='3', suit='diamonds'),
                        Card(rank='4', suit='diamonds')]
    # All the aces by skiping by 13 cards
    assert deck[12::13] == [Card(rank='A', suit='spades'),
                        Card(rank='A', suit='diamonds'),
                        Card(rank='A', suit='clubs'),
                        Card(rank='A', suit='hearts')]

def test_sorting():
    """ First doing it manualy. Then use the function. """
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    deck = FrenchDeck()
    suits = 'spades diamonds clubs hearts'.split()

    cards = [Card('7', 'diamonds'), # rank 7 is rank_value = 5, diamonds is 1, therefore 5*4+1 = 21
             Card('J', 'hearts')]   # rank J is rank_value = 9, hearts 2, therefore 9*4+2 = 38
    expected_ans = [21, 38]
    for i, card in enumerate(cards):
        rank_value = FrenchDeck.ranks.index(card.rank)
        ans = rank_value * 4 + suit_values[card.suit]
        assert ans == expected_ans[i]