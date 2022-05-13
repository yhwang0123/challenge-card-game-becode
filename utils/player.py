from card import Card
import random
from random import shuffle


class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.cards = []  # the cards that the player has in his hands.
        self.turn_count = 0
        self.number_of_cards = 0
        self.history = []

    def play(self):
        card = random.choice(self.cards)  # randomly pick a Card in cards
        self.history += [card]
        print(
            f"Player{self.player_name} in Round {self.turn_count} played card: {self.value} {self.icon}."
        )
        return card

    def __str__(self):
        return f"Cards at hand:{self.cards},Round:{self.turn_count},Player name:{self.player_name},Number_of_cards:{self.number_of_cards} Cards played:{self.history}"


Elsa = Player("Elsa")
print(Elsa)


class Deck:
    def __init__(self):
        self.cards = []

    def full_deck(self):
        for color in ["black", "red"]:
            for icon in ["♥", "♦", "♣", "♠"]:
                for value in [
                    "A",
                    "2",
                    "3",
                    "4",
                    "5",
                    "6",
                    "7",
                    "8",
                    "9",
                    "10",
                    "J",
                    "Q",
                    "K",
                ]:
                    if icon in ["♥", "♦"] and color == "red":
                        card = Card(color, icon, value)
                        self.cards.append(card)
                    if icon in ["♣", "♠"] and color == "black":
                        card = Card(color, icon, value)
                        self.cards.append(card)
        return self.cards  # make a full list of 52 cards

    def shuffle(self):  # shuffle the deck
        random.shuffle(self.cards)

    def distribute(self, players: list):
        # distribute cards according to the number of players
        number_of_cards = int(52 / len(players))
        for player in players:
            for s in range(0, number_of_cards):
                top_card = self.cards[0]
                self.cards.remove(top_card)
                player.cards.append(top_card)


# code for test the full deck
mydeck = Deck()
mydeck.full_deck()
mydeck.shuffle()
for y in mydeck.cards:
    print(y.__str__())
