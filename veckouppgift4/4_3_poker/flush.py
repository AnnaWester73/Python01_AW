from colour_value import get_values, get_colours


# Funktion som kontrollerar om korten bildar en stege och har samma färg (straight flush)
def straight_flush (hand):

    # Hämtar värden och färger via funktioner i colour_value.py och sorterar värden i valour för kontroll i straight_flush som behövs
    values = get_values(hand)
    colours = get_colours(hand)
    values.sort()

    # Kontrollerar att alla kort har samma färg
    check_colour = colours[0]
    for colour in colours:
        if colour != check_colour:
            return False

    # Kontrollerar om värdena bildar en stege
    # Skapar variabler för att göra loopen lättare att förstå
    # Loopen körs (antal värden - 1) gånger för att jämföra varje värde med nästa

    for i in range(len(values) - 1):
        current = values[i]
        expected_next =current +1
        actual_next = values[i + 1]
        if actual_next != expected_next:
            return False

    return True


