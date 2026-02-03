#Skriv en funktion med namnet cut_edges.
# Den ska ta en lista som parameter.
# När den anropas ska den returnera en ny lista,
# där den har tagit bort första och sista elementet.
# cut_edges([1, 2, 3, 4]) → [2, 3]

# För att funktionen ska returnera en lista [2, 3] används hakparenteser.
# Utan hakparenteser returneras värdena som en tuple (2, 3).
# [] → lista
# () → tuple
# Python returnerar tuple som standard vid flera returvärden


def cut_edges(value):
    new_list = value[1:-1]
    return new_list

value = [1, 2, 3, 4]
print(cut_edges(value))