from .card import Card
import random

class Deck:

    def __init__(self):
        self.cards = []
        self.build()


    def build(self):
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for point_val in range(1,14):
                if point_val == 1:
                    string_val = "Ace"
                elif point_val == 11:
                    string_val = "Jack"
                elif point_val == 12:
                    string_val = "Queen"
                elif point_val == 13:
                    string_val = "King"
                else:
                    string_val = str(point_val)
                self.cards.append(Card(suit, point_val, string_val))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_cards(self, num_cards=1):
        if len(self.cards) < int(num_cards):
            return "Not enough cards in deck"
        else:
            dealt_cards = [ self.cards.pop() for i in range(num_cards) ]
            return dealt_cards

    def __str__(self):
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str