# 6 Lös felen i koden.
# def increase(x):
#    return x   # funktionen avslutas här
#    x += 1     # denna rad körs aldrig
# print(increase(1))

# lösningen är att x måste ökas innan return,
# eftersom return avslutar funktionen direkt

def increase(x):
    x += 1
    return x

print(increase(1))
