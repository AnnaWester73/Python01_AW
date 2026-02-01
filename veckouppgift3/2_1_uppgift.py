# tankesätt börja räkna ut par
# 1+10=11
# 2+9=11
# 3+8=11
# 4+7=11
# 5+6=11
# 6+5=11
# 7+4= 11paret finns redan blir då total 5 par
# summan blir 5*11=55

print("Uppgift 1a")

answer = 0

for counter in range(1, 11):
    answer = answer + counter
print("Summan av talen 1 till 10 är " + str(answer))

print("----------------------------------------------------------------")

# Annat tankesätt
# Räkna utan antal par 100/2= 50 par
# Summan blir 50*101=5050

print("Uppgift 1b")

answer = 0
for counter in range(1, 101):
    answer = answer + counter
print("Summan av talen 1 till 100 är " + str(answer))


print("Uppgift 1C")

# Så att i börjar med talet 1
# Ska sluta när talet är 100
# I while loopen lägg till en räknare 1 så att alla tal inkluderas och loopen kan bli false

answer   = 0
counter = 1
while counter <= 100:
    answer = answer + counter
    counter = counter + 1
print("Summan av talen 1 till 100 är: " + str(answer))

