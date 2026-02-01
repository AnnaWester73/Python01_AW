#Bygg ett program där användaren kan lägga till saker till en att göra lista
#Tips: använd en loop, input och en variabel för listan.
#Exempel:


# 1. Se innehållet i din lista
# 2. Lägga till nya punkter i din lista
# 3. Markera som klart
# 4. Se färdiga saker
# 5. Lägg tillbaka färdiga saker
# Välj ett alternativ: 1
# Din lista är tom

# Skapar tomma listor för saker som ska göras och som är klara
todo_list = []
completed_list = []

while True:
    print("-------------------------------------")
    print("1. Se innehåll i din lista")
    print("2. Lägg till nya saker i listan")
    print("3. Markera som klar")
    print("4. Se färdiga saker")
    print("5. Lägg tillbaka färdiga saker")
    print("6. Avsluta")
    print("-------------------------------------")

    val = input("Välj ett alternativ: ")

    if val == "1":
        # not ger sant värde och därför skriv det ut att listan är tom
        if not todo_list:
            print("Din lista är tom")
        # Annars skriver ut vad listan innehåller
        else:
            print("Din lista innehåller: ")
            for task in todo_list:
                print("+", task)

    elif val == "2":
        task = input("Skriv en ny sak du måste komma ihåg att göra: ")
        todo_list.append(task)
        print("Ok, lade till", task)

    elif val == "3":
        if not todo_list:
            print("Listan är tom. Finns inget att markera som klart!")
        else:
            print("Skriv in vad du är klar med: ")
            # Enumerate går igenom allt som finns i listan och ger nummer och värde
            # index är nummer som skrivs ut till task.(uppgiften)
            for index, task in enumerate(todo_list):
                print(index, ".", task)

            selected_number = int(input("Ange numret: "))
            if 1 <= selected_number <= len(todo_list):
                # pop tar bort sak ur listan istället för remove med hjälp av värde
                completed_task = todo_list.pop(selected_number)
                completed_list.append(completed_task)
                print("Tog nu bort:", completed_task, "i listan!")
            else:
                print("Ogiltigt val, försök igen.")

    elif val == "4":
        if not completed_list:
            print("Inga färdiga saker ännu.")
        else:
            print("Färdiga saker:")
            for index, task in enumerate(completed_list):
                print(index, ".", task)

    elif val == "5":
        if not completed_list:
            print("Det finns inga saker att lägga tillbaka.")
        else:
            print("Vad vill du lägga tillbala?")
            for index, task in enumerate(completed_list):
                print(index, ".", task)

            selected_number = int(input("Ange numret: "))
            if 0 <= selected_number <= len(completed_list):
                task = completed_list.pop(selected_number)
                todo_list.append(task)
                print("Tillbakalagd i todo-listan:", task)
            else:
                print("Ogiltigt val.")


    elif val == "6":
        print("Programmet avslutas.")
        break

    else:
        print("Ogiltigt val, försök igen.")