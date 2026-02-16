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

letter_height = 100
letter_width = 50
space = 20

# Funktioner för varje bokstav

def write_p():
    pen.pendown()
    pen.left(90)
    pen.forward(letter_height)
    pen.right(90)
    pen.forward(letter_width)
    pen.right(90)
    pen.forward(letter_height // 2)
    pen.right(90)
    pen.forward(letter_width)
    pen.left(90)
    pen.forward(letter_height // 2)
    pen.penup()
    pen.setheading(0)


def write_y():
    pen.penup()

    # upp till mötespunkten (lite högre för smalare form)
    pen.setheading(90)
    pen.forward(letter_height * 0.6)

    pen.pendown()

    # vänster arm (mer uppåt än tidigare)
    pen.setheading(110)
    pen.forward(letter_height * 0.40)

    # tillbaka till mötespunkten
    pen.backward(letter_height * 0.40)

    # höger arm
    pen.setheading(70)
    pen.forward(letter_height * 0.40)

    # tillbaka till mötespunkten
    pen.backward(letter_height * 0.40)

    # stam ner till baslinjen
    pen.setheading(270)
    pen.forward(letter_height * 0.6)

    pen.penup()
    pen.setheading(0)

def write_t():
    pen.pendown()

    pen.left(90)
    pen.forward(letter_height)

    pen.right(90)
    pen.backward(letter_width / 2)
    pen.forward(letter_width)

    pen.backward(letter_width / 2)
    pen.right(90)
    pen.forward(letter_height)

    pen.penup()
    pen.setheading(0)

def write_h():
    pen.pendown()
    pen.left(90)
    pen.forward(letter_height)
    pen.backward(letter_height / 2)

    pen.right(90)
    pen.forward(letter_width)

    pen.left(90)
    pen.forward(letter_height / 2)
    pen.backward(letter_height)

    pen.penup()
    pen.setheading(0)

def write_o():
    pen.penup()

    # flytta till O:s nederkant
    pen.setheading(90)
    pen.forward(letter_height)

    pen.setheading(0)
    pen.pendown()

    # rita cirkeln uppåt
    pen.circle(-letter_height / 2)

    pen.penup()

    # tillbaka till baslinjen
    pen.setheading(270)
    pen.forward(letter_height)

    pen.setheading(0)

def write_n():
    pen.pendown()
    pen.left(90)
    pen.forward(letter_height)

    pen.right(150)
    pen.forward(letter_height * 1.15)

    pen.left(150)
    pen.forward(letter_height)

    pen.penup()
    pen.setheading(0)

pen.goto(-250, -40)   # Startposition (vänster, rak linje)

write_p()
pen.forward(letter_width + space)

write_y()
pen.forward(letter_width + space)

write_t()
pen.forward(letter_width + space)

write_h()
pen.forward(letter_width + space)

write_o()
pen.forward(letter_width + space)

write_n()
pen.forward(letter_width + space)

pen.hideturtle()        # Göm pennan
t.mainloop()