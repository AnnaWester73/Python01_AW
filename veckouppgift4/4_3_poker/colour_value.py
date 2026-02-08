# Funktion som plockar ut värden och färger
# Döper funktion till get_ som sedan användas av flera pokerhand för att få med mig värde eller färger
# Gör ingen sortering av values. Det görs i de pokerhänder där det behövs

def get_values(cards):
    values = []

    for colour, value in cards:
        values.append(value)
 #       values.sort()                      # Provat och sortera här utan att göra det i andra pokerhänder filer
    return values


def get_colours(cards):
    colours = []
    for colour, value in cards:
        colours.append(colour)
    return colours