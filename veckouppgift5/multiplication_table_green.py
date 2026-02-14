#Vi behöver en funktion som kan ge oss multiplikationstabellen.
#Parametern "n" talar om vilket tals tabell vi ska skapa.
#Parametern "limit" talar om var vi ska sluta.
#Om vi till exempel frågar efter 3:ans tabell, med limit==4, ska programmet räkna ut:

def multiplication_table( n, limit, ):
    if n < 1 or n > 10:
        raise ValueError("n must be between 1 and 10")

    result = []

    for i in range(1, limit +1 ):
        value = n * i
        print(f"{i} * {n} = {value}")
        result.append(value)
    return result
#print(multiplication_table(3, 4))