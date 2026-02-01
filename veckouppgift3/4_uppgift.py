#uppgift 4 Figurerar med loopar
# Skapar en loop som ska köras 6 gånger
# Nästa lopp styr antal tecken som ska skrivas ut 8st
# Variabel y byts ut till rad
# Variabel x byts ut till kolumn
# Variabel s används för att skapa strängen som ska skrivas ut.
# För nytt mönster så att # inte flyttas x==1 istället för x==y

print("uppgift 4a")

for rad in range(1,7):
    utskrift= ""
    for kolumn in range(1,9):
        if kolumn == 1:
            utskrift = utskrift + "#"
        else:
            utskrift = utskrift + "."
    print(utskrift)

print("uppgift 4b")

for rad in range(1,7):
    utskrift= ""
    for kolumn in range(1,9):
        if kolumn == rad:
            utskrift = utskrift + "#"
        else:
            utskrift = utskrift + "."
    print(utskrift)


print("uppgift 4c")

# Byter ut variblar x och y till logiska
# För nytt mönster så att # byter ut if x >= 3 and x <= 5 istället för if x == 1.
# När loopen gör steg 3,4,5 blir det tecken

for rad in range(1,7):
    utskrift= ""
    for kolumn in range(1,9):
        if kolumn >= 3 and kolumn <= 5:
            utskrift = utskrift + "#"
        else:
            utskrift = utskrift + "."
    print(utskrift)

print("uppgift 4d")

# Lägger till en if sats för utskrift av rad 3. Där alla tecken ska vara #
# Byter ut variblar x och y till logiska

for rad in range(1,7):
    utskrift= ""
    for kolumn in range(1,9):
        if kolumn == 3 or rad == 3:
            utskrift = utskrift + "#"
        else:
            utskrift = utskrift + "."
    print(utskrift)


print("uppgift 4e")

# Programmet ska köras 6 gånger
# Antal tecken som ska skrivas ut 8st
# Variabel som talar om vart # ska skrivas ut första gången
# Formel där # flyttas ett steg till vänster efter varje körning

fast_pos = 4
move_pos = 5

for rad in range(6):
    utskrift = ""
    for kolumn in range(8):
        if kolumn == fast_pos or kolumn == move_pos:
            utskrift = utskrift + "#"
        else:
            utskrift = utskrift + "."
    print(utskrift)
    move_pos = move_pos - 1

print("uppgift 4f")

# Programmet ska köras 6 gånger
# Antal tecken som ska skrivas ut 8st
# Variabel som talar om vart # ska skrivas ut första gången
# Formel där # flyttas in och en formel där # flyttas ut och en rad skrivs ut 2 gånger

left_pos = 0
right_pos = 5

for rad in range(6):
    utskrift = ""
    for kolumn in range(8):
        if kolumn == left_pos or kolumn == right_pos:
            utskrift = utskrift + "#"
        else:
            utskrift = utskrift + "."
    print(utskrift)

    # flyttas in
    if rad < 2:
        left_pos = left_pos + 1
        right_pos = right_pos - 1

    # Samma rad skrivs ut 3 och 4 gången (första utskrivna raden = 0)
    elif rad == 2:
        left_pos = left_pos
        right_pos = right_pos

    # flyttas ut
    elif rad > 2:
        left_pos = left_pos - 1
        right_pos = right_pos + 1

