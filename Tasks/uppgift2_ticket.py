# Uppgift 2 skriva kod där koden ska räkna ut hur mycket pengar som ska betalas tillbaka
# Koden innehåller variablar för inmatning som sedan används i uträkningen

print("Uppgift 2")

# Nedan är vilka variablar som används i testet och gör om att alla värden måste vara ett heltal
number_of_tickets = int(input("Hur många biljetter ska köpas: "))
ticket_price = int(input("Ange pris per biljett: "))
money_paid = int(input("Ange hur mycket du betalar: "))
number_of_people = int(input("Hur många personer ska dela på pengarna: "))

# Räknar ut totalkostand för alla biljetter och vad som ska betalas tillbaka. Nya varibler
total_ticket_cost = number_of_tickets * ticket_price            # total_ticket_cost är som används i slutet av testet vid print
money_left = money_paid - total_ticket_cost                     # money_left är som används i slutet av testet vid print

# information om hur mycket som blir över.
print("Det blir", money_left, "kronor över.")

# information om vad varje person får tillbaka
# Värdet i variabeln money_left används i formel för ett nytt värde som skrivs ut
share_per_person = money_left / number_of_people
print("Varje person får", share_per_person, "kronor.")

