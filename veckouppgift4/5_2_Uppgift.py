# Skriv en funktion som flyttar pennan ett lämpligt avstånd till höger, utan att rita.
# Tanken är att du ska kunna kombinera den med kvadratfunktionen,
# för att rita flera kvadrater. Exempel:

import turtle

# Variabler för hur många linger för att skapa en kvadrat,
# hur pennan ska flyttas och hur många kvadrater som ska skrivas ut

lines = 4
move = 200
qty = 3
t = turtle.Turtle()
t.speed(1)

def rectangle():
    for line in range(lines):
        t.forward(100)
        t.right(90)

#rectangle() Behövs inte då jag kallar på den i function draw_many

def move_next():
    t.penup()
    t.forward(move)
    t.pendown()

# move_next() Behövs inte då jag kallar på den i function draw_many

def draw_many ():
    for i in range(qty):
        rectangle()
        move_next()

t.penup()
t.goto(-200,200)
t.pendown()

draw_many()

# Har kvar fönstret som ritas ut
turtle.done()