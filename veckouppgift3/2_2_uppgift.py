print("Uppgift 2")
# Skapar en lista med de 6 heltalen som ingå
# Summa variabel som hanterar summeringen. Börjar på 0 för att inte addera en summa innan
# Startar en loop där alla heltal ingår. Där variabel number är ett heltal från listan

lista = [1, -2, 3, -2, 4, -3]
summa = 0
for number in lista:
    summa = summa + number

print("Summan av elementen i listan är " + str(summa))


print("----------------------------------------------------------------")
