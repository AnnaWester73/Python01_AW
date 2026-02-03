#i stället för att använda talserien, slumpa tal mellan 1 och 13.
# (talen i en vanlig kortlek)
# Tips: importera modulen random och använd funktionen randint för att slumpa tal.
#Exempel: card = random.randint(1, 13)

import random

def random_card():
    tal = random.randint(1, 13)
    return tal
print(random_card())

