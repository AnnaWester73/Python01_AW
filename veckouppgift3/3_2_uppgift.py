print("Uppgift 3 kvittoräknare version 2")

print("Välkommen till kvittokompis! Avsluta genom att skriva: quit  ")

# Varibel där Beloppet ingår med värde 0
# skapar en lopp där allt är sant så länge jag anger ett float tal. När jag anger quit eller q är villkoret falskt
# Gör om alla inmatade värden till float tal, Gick inte att lägga det i while villkoret då jag fix krasch.
# Summerar alla inmatade tal

summa = 0

while True:
    value= input("Skriv en ett belopp: ")

    if value == "quit" or value == "q":
        break
    tal= float(value)
    summa = summa + tal

# Räknar ut vad varje person ska betala och skriver ut resultat
antal_personer = float(input("Ange hur många personer summan ska delas på: "))
per_person = summa / antal_personer

print("Det blir" ,summa,"kr totalt, alltså" , per_person,  "per person. Välkommen åter!")

