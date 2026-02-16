# Testfall för 3:ans tabell 1-10
#AK1 Testar tal där limit = 4
#AK2 Testar listan att listans längd är = 4
#AK3 Testar tal utanför 1-10 ska ge Error

from veckouppgift5.multiplication_table_green import multiplication_table
import pytest

#AK1 Testar tal där limit = 4
def test_in_limit():
    assert multiplication_table (3,4) == [3, 6, 9, 12]

#AK2 Testar listan att listans längd är = 4
def test_length_is_limit():
    result = multiplication_table(3, 4)
    assert len(result) == 4

# AK6 – Tal utanför 1–10 ska ge Error
def test_n_outside_range_low():
    with pytest.raises(ValueError):
        multiplication_table(0, 4)

def test_n_outside_range_high():
    with pytest.raises(ValueError):
        multiplication_table(11, 4)






