# Uppgift 5 version 1 Skriv en funktion som ritar en kvadrat. Längden på sidan ska vara en parameter till funktionen.

# Hastighet finns 0-10
# 0 – snabbast möjligt, ritar direkt utan animation
# 1 – mycket långsam
# 2 – långsam
# 3 – ganska långsam
# 4 – långsam till medel
# 5 – medelhastighet
# 6 – normal hastighet (standard)
# 7 – ganska snabb
# 8 – snabb
# 9 – mycket snabb
# 10 – snabbast

import turtle

lines = 4
t = turtle.Turtle()
t.speed(1)

def rectangle ():

    for line in range(lines):
        t.forward(100)
        t.right(90)

rectangle ()

# Har kvar fönstret som ritas ut
turtle.done()
