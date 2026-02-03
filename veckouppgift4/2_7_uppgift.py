#Bygg en funktion med namnet average.
# Den ska ta parametrar: x och y. Båda ska vara tal.
# Funktionen ska returnera medelvärdet.
# Till exempel så räknar man ut medelvärdet av 4 och 8
# genom med formeln: (4 + 8) / 2, vilket blir 6.
# Tips: det kan vara enklare att använda fler variabler.

def average(x, y):
    summa = x + y
    medel = summa/2
    return int(medel)

print(average (4,8))
