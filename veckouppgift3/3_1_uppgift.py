print("Uppgift 3 kvittoräknare")

print("Välkommen till kvittokompis! Avsluta genom att skriva: quit eller q ")

summa = 0
value = ""
# varje gång det kommer in ett tal är värdet sant eftersom jag nedan angivit att en inmatning måste vare ett float
# Anger jag ett quit eller q kommer villkoret bli falsk och avbrytas
# Inmatat värde blir float och varje tal adderas i listan "belopp" och sedan summeras inmatade värden

while value != "quit" and value != "q":
    value = input("Skriv en ett belopp: ")

    if value == "quit" or value == "q":
        break
    tal= float(value)
    summa = summa + tal

print("Det blir" ,summa,"kr totalt. Välkommen åter!")

