import math
from math import hypot

print("Uppgift 1a")
distance_km =470
carspeed_kmh = float(input("Hur fort går bilen i km/h?: "))
time = distance_km / carspeed_kmh
print ("Du kommer sitta i bilen: ", time, "h")                                           # Får fram tal för tiden i ett floattal
print("----------------------------------------------------------------------------------")

print("Uppgift 1b")
distance_km =470
carspeed_kmh = float(input("Hur fort går bilen i km/h?: "))
time = distance_km / carspeed_kmh                                                      # Får fram tal för tiden i floattal
minutes = time * 60                                                                    # Får fram antal minuter
print ("Du kommer sitta i bilen: ", minutes, "min   ")
print("----------------------------------------------------------------------------------")

print("Uppgift 1c")
distance_km =470
carspeed_kmh = float(input("Hur fort går bilen i km/h?: "))
time = int(distance_km / carspeed_kmh)                                                  # Får fram hela tiden tiden i floattal
total_time_minutes = time * 60                                                          # Total antal minuter
hours = total_time_minutes // 60                                                        # Får fram i timmar
minutes = total_time_minutes % 60                                                       # Får fram i minuter
print("Resan tar totalt med bil: ", hours, "h och ", minutes, "min")
print("----------------------------------------------------------------------------------")

print("Uppgift 2")
a = float(input("Ange längden på sida a: "))
b = float(input("Ange längden på sida b: "))

# Beräkning av hyptoehnysans formel
# a2 = a * a
# b2 = b * b
# c = a2 + b2
# hyp = √c
hypotenuse = math.sqrt(a * a + b * b)
print("Hypotenusan är " + str(hypotenuse))                                                  # Skriv ut resultatet
print("----------------------------------------------------------------------------------")

print("Uppgift 3a")
from datetime import date                                                                   # Hämta dagens datum, Hämtar datum klasser från python
today_date = date.today()
print("Dagens datum är: " + str(today_date))                                                # Skriv ut datumet
print("----------------------------------------------------------------------------------")


print ("Uppgift 3b")
from datetime import date, timedelta                                  # Hämta datum och delta för antal dagar
today = date.today()
add_days = timedelta(input("Ange antal dagar: "))
new_date = today + add_days

# Skriv ut vilket datum om 7 dagar
print("Framtida datum är: "+ str(new_date))



