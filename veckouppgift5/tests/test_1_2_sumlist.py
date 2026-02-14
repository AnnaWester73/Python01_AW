from veckouppgift5.sum_list_1_2 import sum_list

# Testar summan av en tom lista.
def test_empty_list():
    expected = 0
    actual =  sum_list([])
    assert actual == expected

# Testfunktionen testar flera olika listor och kontrollerar att summan stämmer i varje fall
# Om alla assert är sanna fortsätter programmet
def test_number_list():
    # TODO: testa med listor som har ett, två respektive fem element.
    assert sum_list([5]) == 5
    assert sum_list([5, 6]) == 11
    assert sum_list([7, 8, 9, 10, 11, 12]) == 57

