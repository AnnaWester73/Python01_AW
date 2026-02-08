
from colour_value import get_values


# Kåk består av exakt två olika värden: 3 + 2
def house(hand):
    values = get_values(hand)

    # set tar bort dubbletter från values så jag bara för unika värden
    unique_values = set(values)

    # Kontrollerar om jag har 2 olika värden
    if len(unique_values) != 2:
        return False

    # Kontrollerar om jag har exakt 3 eller 2 av samma värde
    for value in unique_values:
        count = values.count(value)
        if count not in (2, 3):
            return False

    return True
