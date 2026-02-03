# Lägg till en parameter "count", som avgör hur många ekon som ska skapas.
# Exempel:
# eko("hej", 3) → skriver ut "hejhejhej"

# Skickar in två argument till funktionen eco.
# Där argumentet word är sträng och med argument quantity
# anger hur många gånger strängen ska upprepas/skriva ut)

def eco(word, quantity):
    print(word * quantity)

eco("hej", 3)
