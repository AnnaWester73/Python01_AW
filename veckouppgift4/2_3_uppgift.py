#Följande kod ska sluta loopa efter 5 varv.
# Flytta den in i en funktion och justera den enligt kommentaren.
#   end = 5
#   y = 1
#   for x in range(1, 100):
#       y *= 2
#       # avsluta loopen med en if-sats här
#   print(y)

# En funktion som heter summa med två argument: end och y
# En for-loop som går igenom talen 1 till 99
# y multipliceras med 2 i varje varv
# När x är lika med end skrivs y ut och loopen avslutas
# x=1 1*2=2, x=2 2*2=4, x=3 4*2=8, x=4 8*2=16, x=5 16*2=32
def summa(end, y):
    for x in range(1,100):
        y = y * 2
        if x == end:
            print(y)
            break

end = 5
y = 1
summa(end, y)



