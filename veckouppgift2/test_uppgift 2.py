level1 = 100
level2 = 300

discount_zero = 0
discount_10 = 10
discount_50 = 50

price = float(input("Välkommen, köp något dyrt: "))

discount = discount_zero

if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 50% rabatt.")
    discount = discount_50

elif price >= level1:
    print("Grattis! Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount_10

else:
    print("Du får inga rabatter!")

final_price = price * (100 - discount) / 100

print(f"Efter rabatter blir priset {final_price}")