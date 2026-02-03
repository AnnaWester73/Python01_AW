# Gör en funktion som kan skriva ut innehållet i en lista lite snyggare.
# Först ska funktionen tala om ifall listan är tom,
# eller hur många element den har.
# Sedan ska funktionen skriva ut elementen i en punktlista. Exempel:
# pretty_print(["a", "b", 3.14])
# Listan har 3 element:
# 1. a
# 2. b
# 3. 3.14

def pretty_print(value):

    if len(value) == 0:
        print("Listan är tom!")
        return
    else:
        print("Listan är inte tom! Den har",(len(value)), "element")

    print("Skriver även ut en punktlista")
    for y, x in enumerate(value, start=1):
        print(f"{y}. {x}")


todo_list=["a", "b", 3.14]
pretty_print(todo_list)
