import random

SPADE = '♠'
CLUB = '♣'
HEART = '♥'
DIAMOND = '♦'

VALID_SUIT = CLUB + SPADE + HEART + DIAMOND
VALID_RANK = 'A23456789JQK'


class Card:
    def __init__(self, rank, suit):
        if rank not in VALID_RANK or suit not in VALID_SUIT:
            raise ValueError
        else:
            self.rank = rank
            self.suit = suit

    def points(self):
        if self.rank in "JQK":
            return 10
        elif self.rank in "A":
            return 1
        else:
            return int(self.rank)

    def __str__(self):
        return '{}{}'.format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if len(self.cards) == 0:
            return 'Empty'
        else:
            return_str = ""
            for card in self.cards:
                return_str += str(card) + " "
            return return_str

    def __len__(self):
        return len(self.cards)

    def set_standard(self):
        for suit in VALID_SUIT:
            for rank in VALID_RANK:
                self.cards.append(Card(rank, suit))

    def deal_card(self):
        if len(self.cards) > 0:
            return_card = self.cards[0]
            self.cards = self.cards[1:]
            return return_card
        else:
            return None

    def remove_card(self, position):
        if position >= 0 and position < len(self.cards):
            return_card = self.cards[position]
            del self.cards[position]
            return return_card
        else:
            raise IndexError  # if here, the caller gave an index out of range, so let's raise that exception

    def add_card(self, card):
        if card != None:
            self.cards.append(card)

    def shuffle(self):
        self.cards = random.sample(
            self.cards, len(self.cards)
        )  # sample without replacement the entire number of cards in deck

    def points(self):
        card_points = 0
        for card in self.cards:
            card_points += card.points()
        return card_points
