#Tänk dig en funktion som kan användas för att visa sökresultat
# medan användaren skriver i ett sökfält.
# Funktionen ska ta två parametrar: input är det användaren skriver,
# master_list är en lista med alternativ som kan hittas.

#Kravlista:
#KR1: Exakt träff returneras som lista med ett element
#KR2: Om flera element börjar med input ska alla matchningar returneras i listan.
#KR3: Om inget matchar returnera tom lista
#KR4: Matchning ska ske utan hänsyn till stora och små bokstäver.
#KR5: Tom input ska hela listan returneras
#KR6: Funktionen ska alltid returnera en lista.
#KR7: Endast element av typen str i master_list ska utvärderas. Övriga ska ignoreras.

def autocomplete_list(user_input, master_list):
    # KR6 – Funktionen ska alltid returnera en lista
    if not isinstance(master_list, list):
        return []

    #KR5: Tom input ska hela listan returneras oavsett små eller stora bokstäver
    if user_input == "":
        return master_list

    user_input_lower = user_input.lower()

    # KR1, KR2, KR3, KR4, KR7
    # Tom lista och går igenom alla element i master_list
    # isinstance ignorerar alla element som inte är strängar
    # lower gör om allt till små bokstäver
    # Startswith kontrollerar om strängen börjar med det användaren skrev
    # Lägger in originalvärdet i user
    result = []

    for user in master_list:
        if isinstance(user, str):               #KR7 körs
            if user.lower().startswith(user_input_lower):
                result.append(user)

    return result