print("version 1")

number1 = float(input("Ange tal nr1: "))
number2 = float(input("Ange tal nr2: "))
number3 = float(input("Ange tal nr3: "))

summa = number1 + number2 + number3

print(f"Summa : {number1} + {number2} + {number3} = {summa} ")

print("------------------------------------------------------------------")


print("version 2")

number1 = float(input("Ange tal nr1: "))        #10
number2 = float(input("Ange tal nr2: "))        #20
number3 = float(input("Ange tal nr3: "))        #30

if number1 > number2  > number3:
    print(f"{number1} är störst")

elif number1 < number3 < number2:
    print("")

elif number2 >= number1 and number2 >= number3:
    print(f"{number2} är störst")

else:
    print(f"{number3} är störst")

print("------------------------------------------------------------------")

print("version 3")

number1 = float(input("Ange tal nr1: "))
number2 = float(input("Ange tal nr2: "))
number3 = float(input("Ange tal nr3: "))

# Jämför tal 1 är det större än tal2 och tal3.
if number2 < number1 > number3:
    print(f"{number1} är störst")

# Jämför om tal2 är större än tal1 och tal3
elif number1 < number2 > number3:
    print(f"{number2} är störst")

# Jämför om tal3 är större än tal1 och tal3
elif number1 < number3 > number2:
    print(f"{number3} är störst")

# Jämför om två lika tal. Är tal1 lika med tal2 och tal1 och tal2 är större än tal3.
elif number1 == number2 and number1 > number3:
    print(f"{number1} och {number2} är störst och {number3} är minst")

# Jämför om alla tal är lika
elif number1 == number2 == number3:
    print("Alla är lika stora")


print("------------------------------------------------------------------")

print("version 4")

number1 = float(input("Ange tal nr1: "))
number2 = float(input("Ange tal nr2: "))
number3 = float(input("Ange tal nr3: "))

# Om alla tal är lika är alla tal mellerst och skrivs ut.
if number1 == number2 == number3:
    print(f"Alla tal är lika och det mellersta är {number1}")

# Om alla tal är olika
# Fall 1 där tal1 är mellerst. Mindre än tal 2 och större än tal 3

elif number2 > number1 > number3:
    print(f" Tal {number1} är mellerst ")

# Fall 2 där tal2 är mellerst. Mindre än tal1 och större än tal3
elif number1 > number2 > number3:
    print(f" Tal {number2} är mellerst ")

# Fall 3 där tal 3 är mellerst. Mindre än tal1 och större än tal2
elif number1 > number3 > number2:
    print(f" Tal {number3} är mellerst ")

# Fall 4 där tal1 är mellerst. Mindre än tal 3 och större än tal 2
elif number2 < number1 < number3:
    print(f" Tal {number1} är mellerst ")

# Fall 5 där tal2 är mellerst. Mindre än tal 3 och större än tal 1
elif number1 < number2 < number3:
    print(f" Tal {number2} är mellerst ")

# Fall 6 där tal3 är mellerst. Mindre än tal 2 och större än tal 1
elif number1 < number3 < number2:
    print(f" Tal {number3} är mellerst ")

else:
    print("Det finns inga mellersta tal")