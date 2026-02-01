# Uppgift 5 version 2 Gissa talet
# Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa det
# Om man gissar för lågt eller för högt ska spelet tala om det.
# Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.
# Slumpa ett hemligt tal
# secret = random.randint(1, 100)
# Importerar funktionen random som är standard i python för att slumpa tal
# Lägg till funktion skriv ut om man är nära ifall man gissar högst 5 ifrån det rätta svaret.
# "Nu börjar det brännas!"

import random

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

# Slumpa ett hemligt tal
random_number = random.randint(1, 100)

guess_number = 0

while True:
    guess = int(input("Gissa: "))
    guess_number = guess_number + 1

    # Räknar om skilland mellan tal och random tal
    # och kollar talet är mindre eller lika med 5 och skilt från 5
    if abs(guess - random_number) <= 5 and guess != random_number:
        print("Nu börjar det brännas!")

    if guess < random_number:
        print("Nej, det är för lågt!")
    elif guess > random_number:
        print("Nej, det är för högt!")
    else:
        print("Det är rätt!! Du gjorde det på", guess_number, "gissningar.")
        break