balance = int(input("Ange ett heltal värde och verifiera om talet är större än 0: "))                # Int bara heltal
zero_value = 0
result = balance > zero_value
print("Värde är: " + str( bool(result)))
print("-----------------------------------------------------")

balance = float(input("Ange ett numeriskt värde och verifiera om talet är större än 0: "))      # float med decimaler
zero_value = 0
result = balance > zero_value
print("Värde är: " , bool(result))                       # Bra och komma ihåg att , gör att jag inte behöver lägga till str när jag blandar olika värden i print
print("-------------------------------------------------")

balance = float(input("Ange ett numeriskt värde och verifiera om talet är större än 0: "))      # float med decimaler
zero_value = 0
result = balance > zero_value
print("Värde är: " , bool(result))
if balance > zero_value:
    print("Grattis värdet är större än 0")
else:
    print("Ledsen värdet är mindre än 0")

print("körs alltid eftersom den ligger utanför if satsen")
print("----------------------------------------------------")

balance = float(input("Ange ett numeriskt värde och verifiera om talet är större än 0: "))      # float med decimaler
zero_value = 0
result = balance > zero_value
print("Värde är: " , bool(result))

if balance > 500:
    print("Du är rik")
elif balance > zero_value:
    print("Grattis värdet är större än 0")
else :
    print("Värdet är mindre än 0")
print("----------------------------------------------")

balance = float(input("Ange ett numeriskt värde och verifiera om talet är större än 0: "))      # float med decimaler
zero_value = 0
result = balance > zero_value
print("Värde är: " , bool(result))

if balance > 500:
    print("Du är rik")
elif balance > zero_value:
    print("Grattis värdet är större än 0")
else :
    print("Värdet är mindre än 0")
if balance < 10 or balance < 600:
    print("Du har inte satt in så mycket pengar på kontot denna gång")

print("----------------------------------------------")


