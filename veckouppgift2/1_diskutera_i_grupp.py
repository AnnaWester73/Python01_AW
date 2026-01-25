# The purpose of the code is to calculate whether the user gets a discount on the value. If the user gets a discount, what discount?
# The code from the beginning had an error that made it unexecutable on the last line where you mixed string and number
# If and elif was in the wrong order where the lowest discount was first
# Improvement was made to  clarify  when discount = 0
# Improvement with variabel for discounts

is_member = False
level2 = 300
level1 = 100

discount_zero = 0
discount_30 = 30
discount_10 = 10

price = float(input("Välkommen, köp något dyrt: "))

discount = discount_zero                                                # Clarify when discount is 0 if price is under 100 to use later on in the code

if price >= level2:
    print("Grattis! Du har avancerat till nivå 2 och får 30% rabatt. ")
    discount = discount_zero + discount_30

elif price > level1:
    print("Grattis Du har avancerat till nivå 1 och får 10% rabatt.")
    discount = discount_zero + discount_10

else:
    print("Du får inga rabatter för ditt köp! Priset är: " +str(price))

if discount > 0:
    final_price = price * (100 - discount) /100
    print("Efter rabatter blir priset...." + str(final_price))
