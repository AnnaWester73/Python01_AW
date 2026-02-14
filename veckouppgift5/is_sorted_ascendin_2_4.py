#Uppgift 4b
# Den returnerar True för tom lista.
# Den returnerar True för lista med ett element.
# Den returnerar True för korrekt sorterad lista.
# Den returnerar False för osorterad lista.
# Den accepterar lika värden som giltig sortering.
# Den kastar TypeError om indata inte är en lista.
# Indata-listan ändras inte under körning.

def is_sorted_ascending(numbers):

    if type(numbers) != list:
        raise TypeError("Input must be a list")

    # Gå igenom listan och jämför varje element med nästa
    for i in range(len(numbers) - 1):       # Returnerar true om listan är tom eller bara 1 värde. Loopen körs inte
        if numbers[i] > numbers[i + 1]:
            return False

    # Om inget fel hittades är listan sorterad
    return True
