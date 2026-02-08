

# Importerar från filen colour_value och tar in alla element för värden
from colour_value import get_values

def two_pair (hand):

    values = get_values(hand)
    values.sort()                                       # Sortering behövs för att while loop ska fungera

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

