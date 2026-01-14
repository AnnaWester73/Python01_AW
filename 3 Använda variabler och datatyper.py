# Uppgift 1a
# skriv in ett heltal
from ipaddress import summarize_address_range

print ("Uppgift 1a")
number1_input = input ("Skriv in ett heltal: ")

# omvandla talet till heltal
number1 = int(number1_input)
#Skriv ut talet som användaren skrev in
print ("Numret som skrevs in är:", number1)
print("----------------------------------------------------------------------------------")


# Uppgift 1b
#Skriv in ett nytt heltal
print ("Uppgift 1b")
number2_input = input ("Skriv in ett nytt heltal: ")

# omvandla talet till heltal
number2 = int(number2_input)

print("Summan av de två talen är: ", number1 + number2)
print("----------------------------------------------------------------------------------")

#Uppgift 2a
print ("Uppgift 2a")
jacket_price = 2000
rea_procent = 75.0
jacket_netto=jacket_price * rea_procent/100
print(" Jackan kostar efter rea:", jacket_netto)
print("----------------------------------------------------------------------------------")

# Uppgift 2b
# Frågar användaren efter jackans pris
print ("Uppgift 2b")
price_input = input("Vad kostar jackan? (pris i kronor): ")
price = float(price_input)

# Frågar användaren efter rabatt i procent, t.ex. 25 eller 25%
discount_input = input("Ange en rabatt i procent (t.ex. 25 eller 25%): ")

# Tar bort procenttecknet om det finns
discount_input = discount_input.replace("%", "")

# Gör om till tal
discount_percent = float(discount_input)

# Räknar ut hur mycket rabatt det blir
discount_amount = price * discount_percent / 100

# Räknar ut slutpriset
final_price = price - discount_amount

# Skriver ut resultatet
print("Rabatten är:", discount_amount, "kronor")
print("Du betalar:", final_price, "kronor")
print("----------------------------------------------------------------------------------")