
print("-------------------")
print("uppgift 1a")
def foo(t):
    print("test")

foo("hej")
# funktionen foo tar emot värdet hej och sätter det i lokal variabel t
# Men variabel t används inte i funktionen
# Utan print skriver ut en sträng test och det är det som skrivs ut

print("-------------------")
print("uppgift 1b")

def fun1(x, y):
    return x * y

print(3, 5)
# Finns inga värden till de lokala variablerna x och y
# beräkning görs inte
# Skriver bara ut 3 5


print("-------------------")
print("uppgift 1c")

def fun1(x, y):
    return x * y

print(fun1(3, 5))

# Här tar jag med funktionen i print där jag skickar med värden
# för x och y. Då kommer funktionen i bruk
# 3*5=15
# skriver ut 15

print("-------------------")
print("uppgift 1d")

def fun2(i):
    return 5 * i

x = 2
y = 3
a = fun2(fun2(x) + fun2(y))
print(a)
# Första steget är i=2 från x variabel går in i funktion 5*2=10
# Andra steget är i=3 från y variabel går in i funktion 5*3=15
# tredje steget är 10+15=25. Då blir i=25
# fjärde steget är i=25 går in i funktionen 5*25=125
# a variabeln blir 125 och skrivs ut

print("-------------------")
print("uppgift 1e")

a = 5
def fun3(a):
    a += 1
a += 2
print(a)

# funktion körs inte då funktionen saknar en return av värdet
# utskriften kommer bara göra 5+2=7
# 7 skrivs ut

print("-------------------")
print("uppgift 1e som blir 8 ")

a = 5
def fun3(a):
    return a + 1
a = fun3(a)
a += 2
print(a)
# funktionen fun3 skickar in värde 5 och skickar med ett nytt värde tillbaka
# första steget 5+1=6 och a kommer ut med värde 6 från funktionen fun3
# näste steg 6+2=8 och 8 skrivs ut

print("-------------------")
print("uppgift 1f")

def foo(i):
    return 2*i*i

def goo(x, y):
    return foo(y)

a = goo(foo, 3)
print(a)
# Första steget är att en funktion med namn foo och finns beräkning som returnerar ett tal
# Andra steget är att det skapas en funktion med namn goo
# Där man skickar där funktionen är x och värdet y
# x(y) innebär att funktion x med argument y
# funktion goo anropas genom a = goo(foo, 3)
# x för värdet foo där ett värde ska returneras
# y får värde 3
# samma sak som return foo(3)
# funktion foo körs med beräkning 2*3*3=18
# Anser att goo funktionen bara förvirrar

print("-------------------")
print("uppgift 1f mera logisk")

def goo(x, y):
    return x(y)

def foo(i):
    return 2*i*i

def bar(i):
    return i + 10

print(goo(foo, 3))  # 2*3*3=18
print(goo(bar, 3))  # 3+10=13

# utan goo måste du skriva:
# print(foo(3))
# print(bar(3))
# Vilket funkar — men blir snabbt rörigt i större program.

print("-------------------")
print("uppgift 1g")

def is_number(x):
    if isinstance(x, int):
        return True
    elif isinstance(x, float):
        return True
    return False

print(is_number(5.5))
print(is_number(42))

# steg 1 skickar in 5.5. if blir false då det inte är en int
# går vidare till elif där 5.5 är en float och returnerar True
# Skriver ut True
# steg 2 skickar in 42. if är True. Returnerar True
# skriver ut True

print("-------------------")
print("uppgift 1g med förbättring")

def is_number(x):
    if isinstance(x, (int, float)):
        return True
    return False

print(is_number(5.5))
print(is_number(42))
print(is_number("sträng"))

print("-------------------")
print("uppgift 1h")


def average_words(strings):
    found = []
    for item in strings:
        if 4 < len(item) < 8:
            found.append(item)
    return found

average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"])

# har en funktion average_words
# skapar en tom lista som heter found
# gör en loop om ordets längd är mellan 5-7 tecken
# Lägger till orden i listan found
# returnerar orden "how's going coding"

print("-------------------")
print("uppgift 1i")
# Lista ut vad som är funktionens syfte, baserad på namn och sammanhang.

# Lista ut vad som ska vara det förväntade resultatet
# för de tre testlistorna.

# Rätta felen, så funktionen gör det den ska.

def find_min(numbers):
    counter = 0
    for item in numbers:
        if item < counter:
            counter = item
    print(f"The smallest item is: {counter}")
    return counter

find_min([10, 3, -4, -11])  # -11
find_min([])                # 0
find_min([100])             # 0

print("-------------------")
print("uppgift 1i förbättring av uppgift")

def find_min(numbers):
    if numbers:
        smallest = numbers[0]
        for item in numbers:
            if item < smallest:
                smallest = item
        print(f"The smallest item is: {smallest}")

        return smallest
    else:
        print("List is empty")
        return None

find_min([10, 3, -4, -11])  # -11
find_min([])                # 0
find_min([100])             # 0



