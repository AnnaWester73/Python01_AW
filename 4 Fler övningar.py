# uppgift 1a

print (" Det är 470km mellan stockholm och Göteborg")
print ("Uppgift 1a")
distance_km =470

carspeed_kmh = float(input("Hur fort går bilen i km/h?: "))

hours = distance_km / carspeed_kmh

print ("Du kommer sitta i bilen: ", hours, "h")


#Uppgift 1b

print("Uppgift 1b")
distance_km =470
# hur fort kommer du köra med bilen i km/h
carspeed_kmh = float(input("Hur fort går bilen i km/h?: "))
hours = distance_km / carspeed_kmh
minutes = hours * 60

print ("Du kommer sitta i bilen: ", minutes, "min   ")

print("Uppgift 1c")
distance_km =470
carspeed_kmh = float(input("Hur fort går bilen i km/h?: "))
hours = distance_km / carspeed_kmh

# Får fram hela timmar
time_hours = int(hours)

# Får fram hela minuter
time_minutes = (hours - time_hours) * 60
time_minutes = int(time_minutes)
print("Resan tar totalt med bil: ", time_hours, "h och ", time_minutes, "min")

#Uppgift 2
print("Uppgift 2")

import math

# Be användaren mata in längden på de två kortare sidorna
a = float(input("Ange längden på sida a: "))
b = float(input("Ange längden på sida b: "))

# Beräkna hypotenusan med Pythagoras sats
c = math.sqrt(a * a + b * b)

# Skriv ut resultatet
print(f"Hypotenusan är {c}")



#Uppgift 3a
print ("Uppgift 3a")
from datetime import date, timedelta  # Hämta dagens datum, Hämtar datum klasser från python
today = date.today()

# Skriv ut datumet
print(f"Dagens datum är: {today}")


#Uppgift 3b
print ("Uppgift 3b")

# Hämta dagens datum, Hämtar datum klasser från python och lägger på 7 dagar
from datetime import date
today = date.today()
sevendays = timedelta(days=7)
future_date = today + sevendays # lägger på 7 dagar från dagens datum

# Skriv ut vilket datum om 7 dagar
print(f"Om sju dagar är det datum: {future_date}")



