# När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
# poker_hand(cards)
# "Du fick ett par med valören: 5"
#skapar en lista av korten olika typer av kort
# 2-14
# Kategorier spader, hjärter ruter, klöver

import random
from itertools import product

card_values = list(range(2, 15))
category = ["Spader", "Hjärter", "Ruter", "Klöver"]
card_quantity = 1

#Skapar en funktion för alla kort i en kortlek
def deck_of_cards (category, card_values, card_quantity):

    # Skapar upp alla varianter av de två listorna
    # Väljer ett kort random från listan
    new_list = list(product(card_values, category))
    card = random.sample(new_list, card_quantity)

    return card

print("Du fick kort: ",deck_of_cards(card_values, category,card_quantity))









