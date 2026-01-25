#Skriv ett program som kan omvandla en temperatur i grader Celsius till grader Fahrenheit.

print("Version 1")
celsius = float(input("Skriv in en temperatur i grader Celsius: ? "))

farenheit = (celsius * 9 / 5) + 32                                                    # Formel för att omvandla celius till Farenheit

print(f"Det blir {farenheit} grader i Farenheit.")

print("-----------------------------------------------------------------------------")


print('Version 2')
choice = input("Vilken temperatur vill du använda Celsius (Ange c) eller Farhrenheit (Ange f) ")

if choice == "c":                                                                       # Används när jag vill verifera ett inmatat och få det till ett True eller False.
    celsius = float(input("Skriv in en temperatur i grader Celsius ?: "))
    farenheit = (celsius * 9 / 5) + 32                                                # Formel för att omvandla celius till Farenheit
    print(f"Det blir {farenheit} grader i Farenheit.")

elif choice == "f":                                                                     # Används när jag vill verifera ett inmatat och få det till ett True eller False.
    farenheit = float(input("Skriv in en temperatur i grader Farhrenheit ? : "))
    celsius = (farenheit - 32) * 5 / 9
    print(f"Det blir {celsius} grader i Celsius.")

print("-----------------------------------------------------------------------------")


print('Version 3')
choice = input("Vilken temperatur vill du använda Celsius (Ange c) eller Farhrenheit (Ange f) ")

if choice.lower() == "c":                                                                       # Används när jag vill verifera ett inmatat och få det till ett True eller False. Använt lower för att göra om värde till små bokstäver för att få True värde.
    celsius = float(input("Skriv in en temperatur i grader Celsius ?: "))
    farenheit = (celsius * 9 / 5) + 32                                                          # Formel för att omvandla celius till Farenheit
    print(f"Det blir {farenheit} grader i Farenheit.")

elif choice.upper() == "F":                                                                     # Används när jag vill verifera ett inmatat och få det till ett True eller False. Använd mig av upper för att värdet görs om till stor bokstav
    farenheit = float(input("Skriv in en temperatur i grader Farhrenheit ? : "))
    celsius = round((farenheit - 32) * 5 / 9 ,1)                                                 # Round med en decimal
    print(f"Det blir {celsius} grader i Celsius.")

if celsius < 10:                                                                                  # Om celsius är mindre än 10 grader. Använder oavsett om man anger grader i Farenheit skrivs detta ut
    print("Sätt på dig vinterkläder, det är kallt.")

elif celsius >= 20:                                                                               # Om celsius är lika med 20 grader eller högre är det varmt. Använder avsett om man anger grader i Farenheit skrivs detta ut.
    print("Packa badkläder, det är varmt!")


print("-----------------------------------------------------------------------------")