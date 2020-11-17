""" Implement deck of cards, with type hinting, using classes.
    Inspired by realpython
    https://realpython.com/python-type-checking/#playing-with-python-types-part-2 """
import random
import sys
from typing import List, Optional

class Card:
    """ Create Card. Uses Unicode character for the suit. """

    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:
        """ Initialize Card with a suit and rank. """
        self.suit = suit
        self.rank = rank

    def __repr__(self) -> str:
        return f"{self.suit}{self.rank}"

class Deck:
    """ Deck of cards. Depends on class Card.
        .create() is a class method to create the Deck.
        .deal() is a method to deal the Deck to all players and create hands. """

    def __init__(self, cards: List[Card]) -> None:
        """ Initialize Deck with a list of cards. """
        self.cards = cards

    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
        """ Create a new deck of 52 cards.
            This should be done for the whole deck, not for each hand. Therefore classmethod.
            Need to use "Deck" in type hint since Deck class is being defined. """

        cards = [Card(suit, rank)
                 for rank in Card.RANKS
                 for suit in Card.SUITS
                 ]

        if shuffle:
            random.shuffle(cards) # Shuffles a list of Card

        # Take the list of Card and convert into the class Deck?
        return cls(cards)

    def deal(self, num_hands: int):
        """Deal the cards in the deck into a number of hands. """
        # Get and define the class of the object. save in local cls
        cls = self.__class__

        # Create num_hands decks from the deck by starting at i and skipping num_hands
        return tuple(cls(self.cards[i::num_hands])
                     for i in range(num_hands))

class Player:
    """ Create a Player class.
        .play_card() gives a random card from Players hand and then removes it. """

    def __init__(self, name: str, hand: Deck) -> None:
        """ Initialize Player with a name and a hand. """
        self.name = name
        self.hand = hand

    def play_card(self) -> Card:
        """Play a card from the player's hand. """
        # Get a random card inside the hand. cards is an attribute of Deck.
        card = random.choice(self.hand.cards)
        self.hand.cards.remove(card)

        # !r is to call the __repr__ and <3 is left aligned with 3 spaces
        print(f"{self.name}: {card!r:<3}  ", end="")
        return card

class Game:
    """ Runs the game. two instance variables: deck and hands
        .play() sets-up the game and then plays all Players cards.
        .player_order() creates a list of Players to play the hands. """

    def __init__(self, *names: str) -> None:
        """ Set up the Deck and deal cards to 4 players.
            When type hinting on a *xxx only gives type but not List[type]. """
        deck = Deck.create(shuffle=True)

        # In original solution. Not sure why so complicated. Changed it.
        # self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
        self.names = "P1 P2 P3 P4".split()

        # Create all hands. zip will combine the list of names with the list of hands (Decks).
        # The dictionary comprehension will assign name with a Player intialization
        self.hands = {
            n: Player(n, h)
            for n, h in zip(self.names, deck.deal(4))
        }

    def play(self) -> None:
        """Play a card game. """
        start_player = random.choice(self.names)
        turn_order = self.player_order(start=start_player)

        # Play cards from each player's hand until start_player hand empty
        # Note that hands is an attribute/dictionary of the class.
        # Then pick the hand of the Player instance. Then the cards of the Deck attribute.
        while self.hands[start_player].hand.cards:
            # For each Player, play_card() to offer/remove/print a card
            for name in turn_order:
                self.hands[name].play_card()
            print()

    def player_order(self, start: Optional[str] = None) -> List[str]:
        """ Rotate player order so that start goes first. """
        if start is None:
            start = random.choice(self.names)

        # Get location of the 1st name in the list of names
        start_idx = self.names.index(start)

        # Create the list of names by rotating through the list
        return self.names[start_idx:] + self.names[:start_idx]

if __name__ == "__main__":
    # Read player names from command line
    player_names = sys.argv[1:]
    game = Game(*player_names)          # Initialize the game
    game.play()
