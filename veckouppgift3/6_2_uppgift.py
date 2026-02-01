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
    print("3. Markera som klar")
    print("4. Avsluta")
    print("-------------------------------------")

    val = input("Välj ett alternativ: ")

    if val == "1":
        # not ger sant värde och därför skriv det ut att listan är tom
        if not todo_list:
            print("Din lista är tom")

        # Skriver ut alla saker som lagt till i todo_listan på nya rader
        else:
            print("Din lista innehåller: ")
            for ny_todo in todo_list:
                print("+", ny_todo)

    elif val == "2":
        ny_todo = input("Skriv en ny sak du måste komma ihåg att göra: ")
        todo_list.append(ny_todo)
        print("Ok, lade till", ny_todo)

    elif val == "3":
        if not todo_list:
            print("Listan är tom. Finns inget att markera som klart!")
        else:
            print("Skriv in vad du är klar med: ")
            # Enumerate går igenom allt som finns i listan och ger index och värde
            # Ger varje sak ett nummer som startar på 1
            # i ger ett löpnummer på allt som är i listan
            for seqno, ny_todo in enumerate(todo_list, start=1):
                print(seqno, ".", ny_todo)

            nr = int(input("Ange numret: "))
            if 1 <= nr <= len(todo_list):
                klar_sak = todo_list.pop(nr - 1)
                print("Tog nu bort:", klar_sak, "i listan!")
            else:
                print("Ogiltigt val, försök igen.")




    elif val == "4":
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val, försök igen.")