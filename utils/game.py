from player import Player
from player import Deck


class Board:
    def __init__(self, players: list):
        self.players = players
        self.turn_count = 0
        self.active_cards = []
        self.history_cards = []

    def start_game(self):
        deck = Deck()
        deck.full_deck()
        deck.distribute(self.players)
        self.players.play()
        active_cards = player.cards.pop()
        history_cards = active_cards.append
        turn_count += 1
        if turn_count > str(52 / len(players)):
            pass
            return f"Round {self.turn_count},List of active cards:{self.active_cards},The number of cards:{self.history}."
