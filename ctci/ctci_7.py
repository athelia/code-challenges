# CTCI 7 Object-Oriented Design
from random import shuffle
from typing import Union


# 7.1 Deck of Cards
class Card:
    names_to_ranks = {"Ace": 1, "Jack": 11, "Queen": 12, "King": 13}

    def __init__(self, suit: str, rank: Union[int, str]):
        self.suit = suit if suit in ["Clubs", "Diamonds", "Hearts", "Spades"] else None
        self.rank = rank if rank in range(14) else None
        self.rank = (
            Card.names_to_ranks[rank]
            if rank in ["Ace", "Jack", "Queen", "King"]
            else self.rank
        )

        if not self.suit and not self.rank:
            raise ValueError(
                f"{suit} is not one of 'Clubs', 'Diamonds', 'Hearts', or 'Spades'"
                "and {value} is not an integer up to 13 or one of 'Ace', 'Jack', 'Queen', 'King'"
            )
        if not self.suit:
            raise ValueError(
                f"{suit} is not one of 'Clubs', 'Diamonds', 'Hearts', or 'Spades'"
            )
        if not self.rank:
            raise ValueError(
                f"{rank} is not an integer up to 13 or one of 'Ace', 'Jack', 'Queen', 'King'"
            )

        self.name = f"{Deck.ranks_to_names[self.rank]} of {self.suit}"

    def __repr__(self):
        return f"<Card {self.name}>"


class Deck:
    ranks_to_names = {
        1: "Ace",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Jack",
        12: "Queen",
        13: "King",
    }

    def __init__(self):
        self.deck = []
        self.discarded = []
        for rank in range(14):
            for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
                self.deck.append(Card(suit=suit, rank=rank))
        self.shuffle()

    def shuffle(self):
        shuffle(self.deck)

    def draw(self) -> Card:
        return self.deck.pop()


class CardGame:
    def __init__(self, players: int):
        self.players = players if type(players) is int else None
        self.hands = [[] for _ in range(self.players + 1)]
        self.deck = Deck()

    def deal(self, qty_cards):
        for player in range(self.players + 1):
            for _ in range(qty_cards):
                self.hands[player].append(self.deck.draw())

    @classmethod
    def score(cls, hand):
        return sum(card.rank for card in hand)

    def determine_winner(self):
        scores = [CardGame.score(hand) for hand in self.hands]

