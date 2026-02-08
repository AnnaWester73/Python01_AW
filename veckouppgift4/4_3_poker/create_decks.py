from itertools import product

colours = ["Spader", "Hjärter", "Ruter", "Klöver"]
card_values = list(range(2, 15))

# Skapar en komplett kortlek med 52 kort.
def deck_of_cards ():
    cards = list(product(colours, card_values))
    return cards

# cards = deck_of_cards()
# print(len(cards))     # Skriver ut 52
# print(cards[:2])      # skriver ut de 2 första tuplerna i listan



