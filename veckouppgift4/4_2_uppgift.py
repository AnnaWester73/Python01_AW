# När man spelar poker har man en hand med 5 kort, som man hoppas ska bli bättre än motståndarnas. Du ska bygga en funktion som kan utvärdera en pokerhand och tala om hur bra den är. Exempel på körning:
# poker_hand(cards)
# "Du fick ett par med valören: 5"
#skapar en lista av korten olika typer av kort
# 2-14
# Kategorier spader, hjärter ruter, klöver
# Bygg en funktion som jämför två spelkort och kan tala om ifall de har samma valör.

import random
from itertools import product

card_values = list(range(2, 15))
category = ["Spader", "Hjärter", "Ruter", "Klöver"]
card_quantity = 5

# Skapar en funktion som bygger en kortlek och drar slumpmässiga kort
# Skickar först in värde och sedan färgerna (category)
def deck_of_cards (card_values, category, card_quantity):

    # Skapar alla möjliga kombinationer av valör och färg
    # Varje spelkort representeras som en tuple: (valör, färg)
    # Drar slumpmässigt card_quantity kort från kortleken
    new_list = list(product(card_values, category))
    card = random.sample(new_list, card_quantity)

    return card

card = deck_of_cards(card_values, category, card_quantity)
print("Du fick kort: ",card)

# Tar ut vilka två värden jag fått på mina kort.
# Kort 1,Första elementet i listan och första elementet i tuplen,
# ger första kortets värde
# Kort 2, Andra elementet i listan och första elementet i tuplen,
# ger andra kortets värde
# Jämför sedan värden om det är lika eller olika

card_value_1 = card [0][0]
card_value_2 = card [1][0]

if card_value_1 == card_value_2:
    print("Korten är av samma valör: " , card_value_1)
else:
    print("Korten är av olika valör: " , card_value_1,"", card_value_2)