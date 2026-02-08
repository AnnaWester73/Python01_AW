from colour_value import get_values, get_colours


# Funktion som kontrollerar om man har stege
def stege (hand):

    # Hämtar värden och sorterar lista
    values = get_values(hand)
    values.sort()

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


