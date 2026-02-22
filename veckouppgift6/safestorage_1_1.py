""" Uppgift 1_1"""

class SafeStorage:
    __data = None

    def get(self):
        return self.__data

    def put(self, data):
        self.__data = data

safe = SafeStorage()
safe.put("Anakonda")
x = safe.get()
safe.put("Boaorm")
y = safe.get()
print(x, y)

# Jag tror att det kommer skrivas ut Anakonda Boaorm. Där x = Anakonda och y = Boaorm
# Ett privat attribut skapas = data
# En metod som sparar värdet i put funktionen
# En metod som hämtar värdet i get funktionen>
# För att använda klassen och skiva ut lägger jag till nedan kod.

""" Uppgift 1_2a"""

class Animal:
    def make_noise(self):
        print("Detta djur har vi inget ljud för.")


class Dog(Animal):
    def make_noise(self):
        print("Voff!")                              # ändrat print


class Cat(Animal):
    def make_noise(self):                           # felstavning av self
        super().make_noise()
        print("Mjau!")

class Rooster(Animal):                              # ny subclass för Rooster
    pass

def sound_off(animals):
    for animal in animals:                          # for loop som tar hand om listan som anropas
        animal.make_noise()


# Följande fel har identifierats
# - subclass dog ligger print fel.
# - self är felstavat i subclass cat
# - finns ingen class som heter Rooster så skapar upp en som ärver Animal.
# - Ändra funktionen sound_off så att den hanterar en lista

# Jag tror att det kommer skrivas ut "Detta djur har vi inget ljud för. Mjau! Voff! Detta djur har vi inget ljud för."
# Feltolkat då python gör en radbrytning efter varje anrop.
# En basklass och tre subclasser
# super() anropar basclassen
# Den kör alltså basclassens funktion först och lägger sedan till sitt eget ljud.


""" Uppgift 1_2b"""

class Parrot(Animal):
    def make_noise(self):                           # felstavning av self
        print("Sing!")

c = Cat()
d = Dog()
h = Rooster()
i = Parrot()

sound_off([c, d, h, i])





