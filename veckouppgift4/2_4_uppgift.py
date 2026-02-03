#Skriv en funktion med namnet last.
# Den ska ta en lista som parameter och returnera det sista elementet i listan.
# last([1, 2, 3]) → 3


def last(value):
    return value[-1]

value = [1, 2 ,3]
print(last(value))

# istället för att skapa en lista i förväg skickas värdena direkt till funktionen
# rekommenderas att användas om "listan av värden inte ska användas någon annanstans
# Personligen tycker jag alternativ ovan är tydligare

def last(value):
    return value[-1]

print(last([1, 2, 3]))