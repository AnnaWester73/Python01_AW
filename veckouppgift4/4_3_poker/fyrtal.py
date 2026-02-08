
# Importerar från filen colour_value och tar in alla element för värden
from colour_value import get_values

# Kontrollerar om handen innehåller fyrtal
# hämtar hand som jag fått i min filen create_decks
def fyrtal(hand):
    values = get_values(hand)

    for value in values:
        if values.count(value) == 4:
            return True

    return False