from veckouppgift5.seek_user_red import autocomplete_list
#Acceptanskriterier (AK)
# AK1 – Hittar en användare i listan, returnera hela listan
# AK2 - Hittar flera användare i listan, returnera användare
# AK3 - Hittar inga användare,
# AK4 - Hittar användare med case sensitive, returnera användare
# AK5 – Ingen användare inmatad, returnera hela listan
# AK6 – Funktionen ska alltid returnera en lista

def test_returns_one_matching_elements():
    master_list = ["Anna", "Anne", "Mathias", "Emil", "Moa", "Ebba"]
    result = autocomplete_list("Anna", master_list)

    assert result == ["Anna"]

