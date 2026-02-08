# Möjlig vidareutveckling:
# bygg ett spel som frågar användaren om man vill ta ett nytt kort eller stanna.
# (slumpa ett tal) Gör så att datorn kan simulera en motståndare.
# Målet är att vinna över datorn.


import random

def random_card():
    card = random.randint(1, 13)
    return card

user_sum = 0
computer_sum = 0

while True:
    new_card = input("Vill du ha ett kort j/n: ")
    if new_card == "n":
        break
    else:
        card = random_card()
        user_sum += card
    print("Du drog:", card)
    print("Summa:", user_sum)

    if user_sum >= 21:
        print("Du gick över 21! Du har förlorat")
        break

if user_sum <= 21:
    while computer_sum < 21:    # Bra odds för mig ändra om du vill till 17
        card = random_card()
        computer_sum += card
        print("Datorn drog:", card)
    print("Datorns summa:", computer_sum)

if user_sum > 21:
    print("Datorn vinner.")
elif computer_sum > 21:
    print("Du vinner!")
elif user_sum > computer_sum:
    print("Du vinner!")
elif user_sum < computer_sum:
    print("Datorn vinner.")
else:
    print("Oavgjort!")










