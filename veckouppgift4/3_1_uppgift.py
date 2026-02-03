# Om man lägger ihop talen 1 + 2 + 3 + 4 + …
# så kommer talens summa att bli större och större.
# Förr eller senare kommer man förbi 21.
# Skriv en funktion som skriver ut
# det första talet i talserien som är större än 21.

def first_over_21(tal,max_sum):
    summa = 0
    while summa <= max_sum:
        summa = summa + tal
        tal = tal + 1
        print("Summa",summa,"tal",tal)
    return tal

tal = 1
max_sum = 21
print(first_over_21(tal,max_sum))