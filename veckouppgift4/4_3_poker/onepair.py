
# Importerar från filen colour_value och tar in alla element för värden

from colour_value import get_values

def one_pair (hand):
    values = get_values(hand)
    values.sort()                                   # Måste ha sort om jag inte har lagt det i filen colour_value.py

    new_values = []

    for value in values:
        if value in new_values:
            return True
        new_values.append(value)
        new_values.sort()

    return False