import random


class Dice:
    def __init__(self):
        self.sides = 6

    def roll(self):
        return random.randint(1, self.sides)


class Cards:
    def __init__(self):
        self.symbol = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8',
                      '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.deck = [(rank, symbol)
                     for symbol in self.symbol for rank in self.ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


task = input("Enter 'dice' to roll a dice or 'cards' to deal a card: ").lower()
if task == 'dice':
    dice = Dice()
    print(f'You rolled a {dice.roll()}')
elif task == 'cards':
    cards = Cards()
    cards.shuffle()
    print(f'You were dealt the {cards.deal()}')
else:
    print("Invalid input. Please enter 'dice' or 'cards'.")
