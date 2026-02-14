import pytest
from veckouppgift5.is_sorted_ascendin_2_4 import is_sorted_ascending
#Uppift 4a Vilka ekvivalensklasser har numbers?
# Tom lista = True
# Lista med ett element = True
# Sorterad lista med element = True
# Osorterad lista med element = False
# Lista med lika värden = True
# Ogiltig data i listan tex "Hej" None = Type error ( Importerar pytest)

# Uppgift 4c testall
# AK 1 Testar om lisan är tom
def test_empty_list():
    assert is_sorted_ascending([]) is True

# AK 2 Testar Lista med ett element
def test_single_element():
    assert is_sorted_ascending([1]) is True

# AK 3 Sorterad lista
def test_sorted_list():
    assert is_sorted_ascending([1, 2, 3]) is True

# AK 4 Testar om listen inte är sorterad
def test_unsorted_two_elements():
    assert is_sorted_ascending([3, 2, 1]) is False

# AK 5 testera om listan har samma värden
def test_same_values():
    assert is_sorted_ascending([1, 1,2 ,2 , 3]) is True

# AK 6 testar om det inte är giltiga värden
def test_not_a_list():
    with pytest.raises(TypeError):
        is_sorted_ascending("123")


