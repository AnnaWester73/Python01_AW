# Importerar från filen colour_value och tar in alla element för värden
from colour_value import get_values

# Kontrollerar om handen innehåller fyrtal
# hämtar cards som jag fått i min filen create_decks
def tretal(hand):
    values = get_values(hand)

    for value in values:
        if values.count(value) == 3:
            return True

    return False