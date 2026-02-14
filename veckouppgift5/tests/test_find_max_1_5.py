# Winner takes it all brukar det ju heta, men nu ska vi försöka ge
# lite heder åt alla andrapristagare. Formulera testfall för en funktion
# som hittar näst största talet i en lista!
# Returnerar det nästa största talet i listan
# Returnerar None om det inte finns något
# Om det är delad förstaplats så returneras det talet


from veckouppgift5.find_max_1_5 import find_2nd_max

def test_find_2nd_max():

    # Normalfall för andra plats
    assert find_2nd_max([1, 2, 3, 4, 5]) == 2
    assert find_2nd_max([3, 1, 2, 3, 5]) == 2

    # Delad förstaplats (ska returnera maxvärdet)
    assert find_2nd_max([1, 1, 3, 4, 5]) == 1
    assert find_2nd_max([4, 5, 2, 1, 2, 3]) == 2

    assert find_2nd_max([]) is None         # Tom lista
    assert find_2nd_max([1]) is None        # Bara ett tal
    assert find_2nd_max([1, 1]) == 1     # Delad första plats
