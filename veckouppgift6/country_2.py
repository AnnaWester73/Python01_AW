


class Country:

    # Konstruktor. Skapar ett nytt Country-objekt och initierar dess instansvariabler.
    def __init__(self, name, pop, area=None):       # För de länder som inte har något värde blir det automatiskt None
        self.__name = name
        self.__population = pop
        self.__area = area
        self.__languages = []                       # Börjar med en tom lista där språk adderas i metoden add_language


    # Metod för utskrifter
    def print_info(self):
        print(f"I {self.__name} bor det {self.__population} miljoner invånare.")

        # Skriver information om area om det finns
        if self.__area is not None:
            print(f"Landets area är {self.__area} kvadratkilometer.")
        else:
            print("Areauppgift saknas.")

        # Skriver information om officiellt språk
        if self.__languages:
            print("Officiellt språk:")
            for language in self.__languages:
                print(language)
        else:
             print("Inga officiella språk registrerade.")

    def add_language(self, language):
        self.__languages.append(language)

country = {
    "se": Country("Sverige", 10.5, 450295),
    "no": Country("Norge", 5.5, 324220),
    "island": Country("Island", 3.8),
    "dk": Country("Danmark", 5.9, 43000),
}
# Hämta objektet från dictionary först.
# Adderar sedan språk för varje land
country["se"].add_language("Svenska")
#country["no"].add_language("Norska")
country["island"].add_language("Isländska")
country["dk"].add_language("Danska")
country["dk"].add_language("Engelska")


"""Skapar en funktion där användaren anger ett land som finns i
dictionary country. Input sparas i code. selected hämtar 
objektet från dictionary"""

def select_countrycode():
    print ("Ange landskod (se/dk): ")
    code = input().lower()

    selected = country.get(code)            # Hämtar objektet som är kopplat till nyckeln code i dictionary country

    if selected:
        selected.print_info()               # # Om objektet finns i dictionary anropas metoden print_info

    else:
        print("Landet finns inte i listan.")

#Anropar funktion
select_countrycode()