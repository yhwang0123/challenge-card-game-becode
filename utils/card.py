# Build a class called Symbol with color and icon:
class Symbol:
    colors = ["black", "red"]
    icons = ["♥", "♦", "♣", "♠"]

    def __init__(self, color, icon):
        self.color = color
        self.icon = icon

    def __str__(self):
        return f"{self.color} of {self.icon}"


card1 = Symbol("black", "♣")
print(card1)

# Build a class Card to hold information for playing cards
class Card(Symbol):
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self, color, icon, value: str):
        super().__init__(color, icon)
        self.value = value

    def __str__(self):
        return f"Color of Card:{self.color},Icon of Card:{self.icon},Value of Card:{self.value}"


card2 = Card("black", "♣", "3")
print(card2)
