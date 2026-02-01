#Bygg ett program där användaren kan lägga till saker till en att göra lista
#Tips: använd en loop, input och en variabel för listan.
#Exempel:


# 1. Se innehållet i din lista
# 2. Lägga till nya punkter i din lista
# Välj ett alternativ: 1
# Din lista är tom

todo_list = []

while True:
    print("-------------------------------------")
    print("1. Se innehåll i din lista")
    print("2. Lägg till nya saker i listan")
    print("3. Avsluta")
    print("-------------------------------------")

    val = input("Välj ett alternativ: ")

    if val == "1":
        # not ger sant värde och därför skriv det ut att listan är tom
        if not todo_list:
            print("Din lista är tom")

        # Skriver ut alla saker som lagt till i todo_listan på nya rader
        else:
            print("Din lista innehåller: ", todo_list)
            for ny_todo in todo_list:
                print("+", ny_todo)

    elif val == "2":
        ny_todo = input("Skriv en ny sak du måste komma ihåg att göra: ")
        todo_list.append(ny_todo)
        print("Ok, lade till", ny_todo)

    elif val == "3":
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val, försök igen.")