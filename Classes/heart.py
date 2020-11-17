""" hearts.py
    Inspired by Realpython.
    https://realpython.com/python-type-checking/#playing-with-python-types-part-2

    Rules:
    1. Four players play with a hand of 13 cards each.
    2. Player holding the ♣2 starts the first round, and must play ♣2.
    3. Players take turns playing cards, following the leading suit if possible.
    4. Player playing the highest card in the leading suit wins the trick,
       and becomes start player in the next turn.
    5. A player can not lead with a ♡ until a ♡ has already been played in an earlier trick.
    6. After all cards are played, players get points if they take certain cards:
        - 13 points for the ♠Q
        - 1 point for each ♡
    7. A game lasts several rounds, until one player has 100 points or more.
    The player with the least points wins."""

from collections import Counter
import random
import sys
from typing import Any, Dict, List, Optional, Sequence, Tuple, Union
from typing import overload

class Card:
    """ Create Card. Uses Unicode character for the suit. """

    SUITS = "♠ ♡ ♢ ♣".split()
    RANKS = "2 3 4 5 6 7 8 9 10 J Q K A".split()

    def __init__(self, suit: str, rank: str) -> None:
        """ Initialize Card with a suit and rank. """
        self.suit = suit
        self.rank = rank

    @property
    def value(self) -> int:
        """ The value of a card is rank as a number. """
        return self.RANKS.index(self.rank)

    @property
    def points(self) -> int:
        """Points this card is worth. """
        if self.suit == "♠" and self.rank == "Q":
            return 13
        if self.suit == "♡":
            return 1
        return 0

    def __eq__(self, other: Any) -> Any:
        """ Equality comparator. """
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other: Any) -> Any:
        """ Lower than comparator. """
        return self.value < other.value

    def __repr__(self) -> str:
        return f"{self.suit}{self.rank}"

class Deck(Sequence[Card]):
    """ Deck of cards. Depends on class Card.
        .create() is a class method to create the Deck.
        .play() is a method to remove the card from the hand.
        .deal() is a method to deal the Deck to all players and create hands.
        .add_card() """

    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards

    @classmethod
    def create(cls, shuffle: bool = False) -> "Deck":
        """Create a new deck of 52 cards. """
        cards = [Card(suit, rank)
            for rank in Card.RANKS for suit in Card.SUITS]
        if shuffle:
            random.shuffle(cards)
        return cls(cards)

    def play(self, card: Card) -> None:
        """Play one card by removing it from the deck. """
        self.cards.remove(card)

    def deal(self, num_hands: int) -> Tuple["Deck", ...]:
        """Deal the cards in the deck into a number of hands. """
        return tuple(self[i::num_hands]
                     for i in range(num_hands))

    def add_cards(self, cards: List[Card]) -> None:
        """Add a list of cards to the deck. """
        self.cards += cards

    def __len__(self) -> int:
        """ Return the length of the object. """
        return len(self.cards)

    @overload
    def __getitem__(self, key: int) -> Card: ...

    @overload
    def __getitem__(self, key: slice) -> "Deck": ...

    def __getitem__(self, key: Union[int, slice]) -> Union[Card, "Deck"]:
        if isinstance(key, int):
            return self.cards[key]
        elif isinstance(key, slice):
            cls = self.__class__
            return cls(self.cards[key])
        else:
            raise TypeError("Indices must be integers or slices")

    def __repr__(self) -> str:
        return " ".join(repr(c) for c in self.cards)

class Player:
    """ Create a Player class.
        .play_card() gives a random card from Players hand and then removes it. """

    def __init__(self, name: str, hand: Optional[Deck] = None) -> None:
        """ Initialize Player with a name and a hand. """
        self.name = name
        self.hand = Deck([]) if hand is None else hand

    def playable_cards(self, played: List[Card], hearts_broken: bool) -> Deck:
        """List which cards in hand are playable this round. """
        if Card("♣", "2") in self.hand:
            return Deck([Card("♣", "2")])

        lead = played[0].suit if played else None
        playable = Deck([c for c in self.hand if c.suit == lead]) or self.hand
        if lead is None and not hearts_broken:
            playable = Deck([c for c in playable if c.suit != "♡"])
        return playable or Deck(self.hand.cards)

    def non_winning_cards(self, played: List[Card], playable: Deck) -> Deck:
        """List playable cards that are guaranteed to not win the trick"""
        if not played:
            return Deck([])

        lead = played[0].suit
        best_card = max(c for c in played if c.suit == lead)
        return Deck([c for c in playable if c < best_card or c.suit != lead])

    def play_card(self, played: List[Card], hearts_broken: bool) -> Card:
        """Play a card from a cpu player's hand. """
        playable = self.playable_cards(played, hearts_broken)
        non_winning = self.non_winning_cards(played, playable)

        # Strategy
        if non_winning:
            # Highest card not winning the trick, prefer points
            card = max(non_winning, key=lambda c: (c.points, c.value))
        elif len(played) < 3:
            # Lowest card maybe winning, avoid points
            card = min(playable, key=lambda c: (c.points, c.value))
        else:
            # Highest card guaranteed winning, avoid points
            card = max(playable, key=lambda c: (-c.points, c.value))
        self.hand.cards.remove(card)
        print(f"{self.name} -> {card}")
        return card

    def has_card(self, card: Card) -> bool:
        return card in self.hand

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name!r}, {self.hand})"

class HumanPlayer(Player):
    """ Create a human player. """
    def play_card(self, played: List[Card], hearts_broken: bool) -> Card:
        """Play a card from a human player's hand"""
        playable = sorted(self.playable_cards(played, hearts_broken))
        p_str = "  ".join(f"{n}: {c}" for n, c in enumerate(playable))
        np_str = " ".join(repr(c) for c in self.hand if c not in playable)
        print(f"  {p_str}  (Rest: {np_str})")
        while True:
            try:
                card_num = int(input(f"  {self.name}, choose card: "))
                card = playable[card_num]
            except (ValueError, IndexError):
                pass
            else:
                break
        self.hand.play(card)
        print(f"{self.name} => {card}")
        return card

class HeartsGame:
    """ Run the game.
        .play()
        .play_round()
        .player_order() """

    def __init__(self, *names: str) -> None:
        self.names = (list(names) + "P1 P2 P3 P4".split())[:4]
        self.players = [Player(n) for n in self.names[1:]]
        self.players.append(HumanPlayer(self.names[0]))

    def play(self) -> None:
        """ Play a game of Hearts until one player go bust. """
        score = Counter({n: 0 for n in self.names})
        while all(s < 100 for s in score.values()):
            print("\nStarting new round:")
            round_score = self.play_round()
            score.update(Counter(round_score))
            print("Scores:")
            for name, total_score in score.most_common(4):
                print(f"{name:<15} {round_score[name]:>3} {total_score:>3}")

        winners = [n for n in self.names if score[n] == min(score.values())]
        print(f"\n{' and '.join(winners)} won the game")

    def play_round(self) -> Dict[str, int]:
        """ Play a round of the Hearts card game. """
        deck = Deck.create(shuffle=True)
        for player, hand in zip(self.players, deck.deal(4)):
            player.hand.add_cards(hand.cards)
        start_player = next(
            p for p in self.players if p.has_card(Card("♣", "2"))
        )
        tricks = {p.name: Deck([]) for p in self.players}
        hearts = False

        # Play cards from each player's hand until empty
        while start_player.hand:
            played: List[Card] = []
            turn_order = self.player_order(start=start_player)
            for player in turn_order:
                card = player.play_card(played, hearts_broken=hearts)
                played.append(card)
            start_player = self.trick_winner(played, turn_order)
            tricks[start_player.name].add_cards(played)
            print(f"{start_player.name} wins the trick\n")
            hearts = hearts or any(c.suit == "♡" for c in played)
        return self.count_points(tricks)

    def player_order(self, start: Optional[Player] = None) -> List[Player]:
        """Rotate player order so that start goes first. """
        if start is None:
            start = random.choice(self.players)
        start_idx = self.players.index(start)
        return self.players[start_idx:] + self.players[:start_idx]

    @staticmethod
    def trick_winner(trick: List[Card], players: List[Player]) -> Player:
        lead = trick[0].suit
        valid = [
            (c.value, p) for c, p in zip(trick, players) if c.suit == lead
        ]
        return max(valid)[1]

    @staticmethod
    def count_points(tricks: Dict[str, Deck]) -> Dict[str, int]:
        return {n: sum(c.points for c in cards) for n, cards in tricks.items()}

if __name__ == "__main__":
    # Read player names from the command line
    player_names = sys.argv[1:]
    game = HeartsGame(*player_names)
    game.play()