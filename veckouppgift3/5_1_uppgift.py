# Uppgift 5 Gissa talet
# Gör ett spel som slumpar ett hemligt tal mellan 1 och 100. Sedan ska man försöka gissa det
# Om man gissar för lågt eller för högt ska spelet tala om det.
# Efter att man har gissat rätt ska spelet skriva ut antalet gissningar.
# Slumpa ett hemligt tal
# secret = random.randint(1, 100)
# Importerar funktionen random som är standard i python för att slumpa tal

import random

print("Välkommen till gissa talet! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är?")

# Slumpa ett hemligt tal
random_number = random.randint(1, 100)

guess_number = 0

while True:
    guess = int(input("Gissa: "))
    guess_number = guess_number + 1

    if guess < random_number:
        print("Nej, det är för lågt!")
    elif guess > random_number:
        print("Nej, det är för högt!")
    else:
        print("Det är rätt!! Du gjorde det på", guess_number, "gissningar.")
        break