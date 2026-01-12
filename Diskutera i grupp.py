# Variabler för hur många biljetter och hur många personer som ska dela på pengarna som blir över
number_of_tickets = int(input("Hur många biljetter ska köpas: "))
ticket_price = int(input("Ange pris per biljett: "))
money_paid = int(input("Ange hur mycket du betalar: "))
number_of_people = int(input("Hur många personer ska dela på pengarna: "))

# Räknar ut totalkostand för alla biljetter och vad som ska betalas tillbaka. Nya varibler
total_ticket_cost = number_of_tickets * ticket_price
money_left = money_paid - total_ticket_cost

# information om hur mycket som blir över.
print("Det blir", money_left, "kronor över.")

# information om vad varje person får tillbaka
share_per_person = money_left / number_of_people
print("Varje person får", share_per_person, "kronor.")