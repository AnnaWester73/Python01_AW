# Uppgift 1a
# variabler
print("Uppgift 1a")
nr1_value = input ("Skriv in ett heltal: ")
number1 = int(nr1_value)
#Skriv ut talet som användaren skrev in
print("Numret som skrevs in är ett heltal:", nr1_value)
print("----------------------------------------------------------------------------------")

# Uppgift 1b
#variabler
print("Uppgift 1b")
nr2_value = input ("Skriv in ett nytt heltal: ")
number2 = int(nr2_value) # omvandla talet till heltal
#resultat av test
print("Summan av de två talen är i uppgift 1a och 1b: ", number1 + number2)
print("----------------------------------------------------------------------------------")

#Uppgift 2a
# Testet är redan angivet med fasta inmatningsvärden. Testet går ut på att räckan ut vad jackan koster efter rabatt
print("Uppgift 2a")

# Faktiska värden som används i testet
jacket_price = 2000
rea_procent = 75.0

#uträckningar och resultat utskrivet
jacket_netto=jacket_price * rea_procent/100
print(" Jackan kostar efter rea:", jacket_netto)
print("----------------------------------------------------------------------------------")

# Uppgift 2b
print ("Uppgift 2b")
price_input = float(input("Vad kostar jackan? (pris i kronor): "))
discount_input = float(input("Ange en rabatt i procent (t.ex. 25): "))          # Använder float så att man kan ange procent i decimaler
discount_amount = price_input * discount_input / 100                            # Räknar ut hur mycket rabatt det blir
final_price = price_input - discount_amount                                           # räckar ut vad jackan kostar efter rea

# Skriver ut resultatet
print("Rabatten är:", discount_amount, "kronor")
print("Du betalar:", final_price, "kronor")
print("----------------------------------------------------------------------------------")