# Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor.

# Vi tar med både små och stora bokstäver för att klara båda fallen och lägger in i en lista
# Vowels är en sträng som innehåller alla tecken
# Går igenom varje sträng i letter (ett i taget)
# Varje gång den hittar en vokal räknar 1 annars 0
# Summerar alla vokaler den hittar i count

def count_vowels(letter):
    vowels = "aeiouyåäöAEIOUYÅÄÖ"
    count = 0
    for x in letter:
        if x in vowels:
            count = count + 1
    return count
