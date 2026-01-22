# Uppgift För att få åka Balder på Liseberg måste man vara 130 cm lång. Skriv ett program som kan säga om man får åka!

# Variables
min_height = 130

height = int(input("Hur lång är du i centimeter? "))

if height >= min_height:                                                # Use >= to also let through the correct length
    print(f"Grattis du är över {min_height}cm och du får åka Balder")

else:
    missing_centimeter = min_height - height
    print(f"Ledsen du är under {min_height}cm och får inte åka balder. Det saknas {missing_centimeter}cm ")

