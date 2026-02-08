#Uppgift 4 version 4
# Skriv funktioner som ritar de enskilda bokstäverna i ordet "PYTHON" med turtle-modulen.
# Kombinera dem och försök få bokstäverna att ritas med samma storlek, på en rak linje.

import turtle as t

# Skapar en turtle och hastighet
pen = t.Turtle()
pen.shape("turtle")
pen.penup()             # Ingen linje
pen.color("white")
pen.speed(1)

# Skapar en röd skärm
screen = t.Screen()
screen.bgcolor("red")

# Skapar en lista med bokstäver

letters = ["P", "Y", "T", "H", "O", "N"]

# start position vart bokstäverna ska skrivas ut på skärmen i mitten
# Start-x ≈ −(antal_bokstäver × avstånd) / 2
# x är vågrätt och y är lodrätt
x = -30
y = 0

for letter in letters:
    pen.goto(x, y)
    pen.write(letter)
    x = x + 10

pen.hideturtle()        # Göm pennan
t.mainloop()