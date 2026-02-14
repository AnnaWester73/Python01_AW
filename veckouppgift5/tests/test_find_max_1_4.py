# Formulera testfall för en funktion som hittar största talet i en lista.
# Returnerar det största talet i listan
# Returnerar None om det inte finns något

from veckouppgift5.find_max_1_4 import find_max

def test_sorted():
    assert find_max([1, 2, 3]) == 3

def test_not_sorted ():
    assert find_max([3, 2, 1]) == 3

def test_negative ():
    assert find_max([-1, -2 , -3]) == -1

def test_empty_list ():
    assert find_max([]) is None

def test_one_element ():
    assert find_max([7]) == 7
