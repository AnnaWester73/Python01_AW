print("Uppgift 3a")
# Skapar en lista med 5 filer (strängar

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Ondskan"]
print(filmer)

print("----------------------------------------------------------------")


print("Uppgift 3b")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Ondskan"]
filmer.append("Fellowship of the ring")
print(filmer)

print("----------------------------------------------------------------")


print("Uppgift 3c")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan
# Lägger till en film först i listan med insert

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Onskan"]
filmer.append("Fellowship of the ring")
filmer.insert(0, "The two towers")
print(filmer)

print("----------------------------------------------------------------")


print("Uppgift 3d")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan
# Lägger till en film först i listan med insert
# Frågar vilket index filmen Fellowship har i listan

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Onskan"]
filmer.append("Fellowship of the ring")
filmer.insert(0, "The two towers")
position_fellowship = filmer.index("Fellowship of the ring")
print("Filmen har position: " + str(position_fellowship))
# print("Filmen har position: ", filmer.index("Fellowship of the ring"))

print("----------------------------------------------------------------")

print("Uppgift 3e")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan
# Lägger till en film först i listan med insert
# Tar bort en film i listan
# Frågar vilket index filmen Fellowship har i listan. Ja byt index

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Onskan"]
filmer.append("Fellowship of the ring")
filmer.insert(0, "The two towers")
filmer.remove("Matrix")
position_fellowship = filmer.index("Fellowship of the ring")
print("Filmen har position: " + str(position_fellowship))

print("----------------------------------------------------------------")

print("Uppgift 3f")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan
# Lägger till en film först i listan med insert
# Tar bort en film i listan
# Frågar hur många filmer (strängar) som finns i listan

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Onskan"]
filmer.append("Fellowship of the ring")
filmer.insert(0, "The two towers")
filmer.remove("Matrix")
antal = len(filmer)
print("Hur filmer ligger i listan nu: " + str(antal))

print("----------------------------------------------------------------")

print("Uppgift 3g")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan
# Lägger till en film först i listan med insert
# Tar bort en film i listan
# Vänder ordning på listan

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Onskan"]
filmer.append("Fellowship of the ring")
filmer.insert(0, "The two towers")
filmer.remove("Matrix")
filmer.reverse()
print("Skriv ut listan baklänges (sista filmen först): " + str(filmer))

print("----------------------------------------------------------------")

print("Uppgift 3h")
# Skapar en lista med 5 filer (strängar)
# Lägger till en film sist i listan
# Lägger till en film först i listan med insert
# Tar bort en film i listan
# Sorterar listan i bokstavsordning

filmer = ["Matrix", "Hajen", "Gladiator", "Scarface", "Onskan"]
filmer.append("Fellowship of the ring")
filmer.insert(0, "The two towers")
filmer.remove("Matrix")
filmer.sort()
print("Skriv ut listan bokstavsordning: " + str(filmer))