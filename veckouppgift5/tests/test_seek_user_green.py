from veckouppgift5.seek_user_green import autocomplete_list
#Acceptanskriterier
# AK1 – Om exakt en match hittas ska endast den matchningen returneras i en lista
# AK2 - Hittar flera användare i listan, returnera användare
# AK3 - Hittar inga användare,
# AK4 - Hittar användare med case sensitive, returnera användare
# AK5 – Ingen användare inmatad, returnera hela listan
# AK6 – Funktionen ska alltid returnera en lista
# AK7 - Testar enbart att användare innehåller strängar

from veckouppgift5.seek_user_green import autocomplete_list

# AK1: Om exakt en match hittas ska endast den matchningen returneras i en lista
def test_returns_one_matching_element():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("Anna", master_list)

    assert result == ["Anna"]


# AK2: Om flera namn börjar på samma input ska alla matchningar returneras
def test_returns_multiple_matching_elements():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("Ann", master_list)

    assert result == ["Anna", "Anne"]


# AK3: Om inget matchar returnera tom lista
def test_returns_empty_list_when_no_match():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("Lena", master_list)

    assert result == []


# AK4: Sökningen ska inte bry sig om stora/små bokstäver
def test_is_case_insensitive():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("ann", master_list)

    assert result == ["Anna", "Anne"]


# AK5: Om input är tom ska hela listan returneras
def test_returns_full_list_when_input_empty():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]

    result = autocomplete_list("", master_list)

    assert result == master_list


# AK6: Resultatet ska alltid vara en lista (inte t.ex. en sträng eller None)
def test_always_returns_list():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("Anna", master_list)

    assert type(result) == list

# AK7 - Testar enbart att användare innehåller strängar
def test_ignores_non_string_values():
    master_list = ["Anna", "Anne",789, "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("Ann", master_list)

    assert result == ["Anna", "Anne"]
