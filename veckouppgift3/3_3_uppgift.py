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


# Frågar om dricks och anger jag inget blir det 10%
# räknar ut total summa med dricks
# Räknar ut vad varje person ska betala med dricks och skriver ut resultat
dricks_input = input("Ange dricks (enter = 10%:) ")

if dricks_input == "":
    dricks_procent = 10
else:
    dricks_procent = float(dricks_input)

summa_dricks = summa + (summa * dricks_procent  / 100)

antal_personer = float(input("Ange hur många personer summan ska delas på: "))
per_person = summa_dricks / antal_personer


print("Det blir" ,summa_dricks,"kr totalt, alltså" , per_person,  "per person. Välkommen åter!")

#print("Skriv ut vilka inmatade talen är ",belopp,)