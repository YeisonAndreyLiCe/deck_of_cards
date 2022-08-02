from .deck import Deck
from .card import Card 
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []#deck.Deck().deal_cards(num_cards)
    
    def __str__(self):
        return f"{self.name}'s hand: {self.hand}"

    def show_hand(self):
        for card in self.hand:
            card.card_info()
        return self.hand
    """ def discard_hand(self, deck):
        self.hand = self.hand.deal_cards(len(self.hand))
        return self.hand """