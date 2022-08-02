from .deck import Deck
from .player import Player

class Game:
    def __init__(self,players, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(player) for player in players]
        """ self.player = Player("Player")
        self.dealer = Player("Dealer") """
        self.deal_cards(num_cards)
        self.hands = [player.show_hand() for player in self.players]

    def deal_cards(self, num_cards=5):
        for player in self.players:
            player.hand = self.deck.deal_cards(num_cards)
    def show_deck(self):
        [print(card) for card in self.deck.cards]
    """ @classmethod
    def show_deck(cls):
        print(cls.deck) """
    """ @staticmethod
    def get_winner(hands):
        winner = None
        for player in hands:
            if winner is None:
                winner = player
            elif player.hand.point_val > winner.hand.point_val:
                winner = player
        return winner """
#game = Game(['Player1','Players2','Players2'],5)
#print(game.show_deck())
#[print(player) for player in game.players]