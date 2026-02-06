# Bygg om koden så att den ingår i en funktion,
# som ritar en komplett cirkel. Använd parametrar i stället för värdena 7, 40 och 30.

import turtle

t = turtle.Turtle()
t.speed(1)

# Variabler hur t ska flyttas. move_1 flyttar framåt och
step = 7
move_1 = 40
angle = 30

def draw_circle (x, y, z):
    # ger heltal
    circle = 360 // z

    for every_move in range (circle):
        t.forward (y / x)
        t.right(z)

draw_circle(step, move_1, angle)

turtle.done()