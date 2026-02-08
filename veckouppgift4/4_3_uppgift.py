# Bygg första versionen av poker_hand(cards). Med hjälp av de andra funktionerna ska den ta reda på om man har ett par, dvs det finns två kort med samma valör.

# Fortsätt att lägga till fler kontroller till funktionen.
# Tips! Du kan göra en funktion som skriver ut kortvärdet snyggare:
# pretty_print_card(["hjärter", 5]) → "hjärter fem
# Ett par (två lika kort)
#Två par
# Ej Gjort Tretal (tre lika)
# Ej gjort Straight (5 kort i följd, t.ex. 7-8-9-10-11)
#Flush / färg (alla kort har samma färg)
# ej gjort Hus (par och tretal med olika valörer)
# ej gjortFyrtal
# Straight flush (5 kort i följd, med samma färg)
# Femtal


import random
from itertools import product

card_values = list(range(2, 15))
colour = ["Spader", "Hjärter", "Ruter", "Klöver"]
card_quantity = 5

# Skapar en funktion som bygger en kortlek och drar slumpmässiga kort
# Skickar först in värde och sedan färgerna (category)
def deck_of_cards (card_values, colour, card_quantity):

    # Skapar alla möjliga kombinationer av valör och färg
    # Varje spelkort representeras som en tuple: (valör, färg)
    # Drar slumpmässigt card_quantity kort från kortleken
    new_list = list(product(card_values, colour))
    card = random.sample(new_list, card_quantity)

    return card

card = deck_of_cards(card_values, colour, card_quantity)
print("Du fick kort:")

# Skapar en card_item för att inte förstöra listan card
for i, card_item in enumerate(card, start=1):
    print(f"{i}. {card_item}")

# Skapar en tom lista
# Plockar ut alla värden från card
# Jämför varje värde med första värdet
# Avbryter direkt med False om något skiljer sig
# Returnerar True först när alla värden är kontrollerade
def femtal(card):

    values = []

    for value,colour in card:
        values.append(value)

    first_value = values[0]
    for value in values:
        if value != first_value:
            return False
    else:
        return True


femtal (card)

# Funktion som kontrollerar alla card_quantity har samma värde följt av varandra och samma colour
def straight_flush (card):

    flush_colour = card[0][1]

    for value, colour in card:
        if flush_colour != colour:
            return False

    card_values = [value for value, colour in card]
    card_values.sort()

    next_value = card_values[0]
    for value in card_values[1:]:           # För att börja med andra värdet
        if value != next_value + 1:
            return False
        next_value = value
    return True

straight_flush (card)

# Skapar en tom lista
# Plockar ut alla färg värden från card
# Jämför varje färg värde med första värdet
# Avbryter direkt med False om något skiljer sig
# Returnerar True först när alla värden är kontrollerade
def suit(card):
    colours = []

    for value, colour in card:
        colours.append(colour)

    first_colour = colours[0]
    for colour in colours:
        if colour != first_colour:
            return False
    else:
        return True

suit (card)

# funktion som kollar om det finns 2 par
# skapar en tom lista
# plockar ut alla kortvärden från card och lägger dem i listan values
# Sorterar alla värden
# 2 variabler som börjar med inga par
# while loop som jämför värden 2 och 2
# kollar
def two_pair (card):

    values = []

    for value, colour in card:
        values.append(value)
    values.sort()

    pairs = 0
    one_pair = 0

    while one_pair < len(values) - 1:                       # Sista index -1
        if values[one_pair] == values[one_pair + 1]:
            pairs = pairs + 1
            if pairs == 2:
                return True
            one_pair = one_pair + 2
        else:
            one_pair = one_pair + 1
    return False

two_pair (card)

# funktion som kollar om du har ett par
# skapar en tom lista då jag bara vill addera kortens värden
# Lägger sedan in alla values från card i listan values
# Sorterar den nya listan när alla värden finns i listan
# kollar varje värde i listan med nästa värde
# Så fort jag hittar en värde som är lika skickar jag true. Hittar då ett par
def one_pair (card):
    values = []
    for value, colour in card:
        values.append(value)
    values.sort()

    for value in range(len(values) - 1):
        if values[value] == values[value + 1]:
            return True

one_pair (card)

def poker_hand(card):

    if femtal (card) == True:
        print("Du har femtal")

    elif straight_flush (card) == True:
        print("Du har straight flush")

    elif suit (card) == True:
        print("Du har färg")

    elif two_pair (card) == True:
        print("Du har två par")

    elif one_pair (card) == True:
        print("Du har ett par (Har ingen funktion för triss eller fyrtal")

    else:
        print("Du har ingen poker hand")

poker_hand(card)








