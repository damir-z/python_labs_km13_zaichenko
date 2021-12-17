suits = ("diamonds", "clubs", "hearts", "spades")
cards = ("A", *range(2,11), "J", "Q", "K")

def card_generator():
    for suit in suits:
        for card in cards:
            yield suit, card

deck = card_generator()

while True:
    card = next(deck)
    print(f"{str(card[1]).ljust(2)} {card[0]}")