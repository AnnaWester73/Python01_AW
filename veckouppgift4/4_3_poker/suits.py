from colour_value import get_values, get_colours

# Jämför varje färg värde med första värdet
# Avbryter direkt med False om något skiljer sig
# Returnerar True först när alla värden är kontrollerade

def suit(hand):

    colours = get_colours(hand)

    check_colour = colours[0]
    for colour in colours:
        if colour != check_colour:
            return False
    else:
        return True
