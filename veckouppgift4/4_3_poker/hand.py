# importerar random och importerar funktion deck of cards i filen create_decks

import random
from create_decks import deck_of_cards

# Drar fem slumpande kort
# Returnerar en lista med 5 kort (tuples) som heter Hand.
# Hand används sedan för att kontrollera olika pokerhänder.
# Har kommenterat bort print men hade den för att kunna kontrollera att jag fick 5 slumpade kort

QTY = 5

def draw_hand():
    deck = deck_of_cards()   # Anropar funktion skapar kortleken
    hand = random.sample(deck, QTY)
   # hand = [('Ruter', 11), ('Hjärter', 11), ('Spader', 11), ('Spader', 5), ('Klöver', 11)]
    return hand

# hand = draw_hand()

#print("Du fick kort:")
#for i, x in enumerate(hand, start=1):
#    print(f"{i}. {x}")

   #Testhänder - -------------------------------
    #Royal flush
    #hand = [('Ruter', 13), ('Ruter', 10), ('Ruter', 12 ), ('Ruter', 11), ('Ruter', 14)]
    #Straight flush
    #hand = [('Spader', 7), ('Spader', 5), ('Spader', 4), ('Spader', 8), ('Spader', 6)]
    #Four of a kind
    #hand = [('Ruter', 11), ('Hjärter', 11), ('Spader', 11), ('Spader', 5), ('Klöver', 11)]
    # Full house
    #hand = [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 11), ('Klöver', 3)]
    #Flush
    #hand = [('Klöver', 11), ('Klöver', 3), ('Klöver', 8), ('Klöver', 9), ('Klöver', 5)]
    #Straight
    #hand = [('Ruter', 7), ('Hjärter', 6), ('Spader', 3), ('Spader', 5), ('Klöver', 4)]
    #Three of a kind
    # hand = [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 5), ('Klöver', 3)]
    # Two pair
    # hand = [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 11), ('Klöver', 14)]
    # One pair
    # hand = [('Ruter', 11), ('Hjärter', 3), ('Spader', 3), ('Spader', 8), ('Klöver', 14)]
    #  ----------------------------------------------------------------