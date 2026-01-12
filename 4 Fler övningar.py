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






