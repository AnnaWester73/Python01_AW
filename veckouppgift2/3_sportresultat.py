# Tottenham spelar mot Liverpool i Champions League. Skriv ett program som frågar användaren hur många mål respektive lag gjorde, och talar om vilket lag som vann.

print("Version 1")
tottenham_goals = int(input("Hur många mål gjorde Tottenham mot Liverpool: "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool mot Tottenham: "))

if tottenham_goals > liverpool_goals:
    print("Tottenham vann!")

elif liverpool_goals > tottenham_goals:
    print("Liverpool vann!")

print("------------------------------------------------------------------------------------")

print("Version 2")

tottenham_goals = int(input("Hur många mål gjorde Tottenham mot Liverpool: "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool mot Tottenham: "))

if tottenham_goals > liverpool_goals:
    print("Tottenham vann!")

elif liverpool_goals > tottenham_goals:
    print("Liverpool vann!")

else:
    print("Matchen blev oavgjord")

print("------------------------------------------------------------------------------------")

print("Version 3a")

tottenham_goals = int(input("Hur många mål gjorde Tottenham mot Liverpool: "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool mot Tottenham: "))

diff_goals_tottenham = tottenham_goals - liverpool_goals
diff_goals_liverpool = liverpool_goals - tottenham_goals

if tottenham_goals > liverpool_goals:
    print(f"Tottenham vann med {diff_goals_tottenham} mål!" )

elif liverpool_goals > tottenham_goals:
    print(f"Liverpool vann med {diff_goals_liverpool} mål!")

else:
    print("Matchen blev oavgjord")

print("Version 3b")


tottenham_goals = int(input("Hur många mål gjorde Tottenham mot Liverpool: "))
liverpool_goals = int(input("Hur många mål gjorde Liverpool mot Tottenham: "))

diff_goals = abs(tottenham_goals - liverpool_goals)                                 # Använt abs i uträkning så att man inte tar hänsym till negativt värde

if tottenham_goals > liverpool_goals:                                               # Om Tottenham vinner
    print(f"Tottenham vann med {diff_goals} mål!" )

elif liverpool_goals > tottenham_goals:
    print(f"Liverpool vann med {diff_goals} mål!")                                  # Om Liverpool vinner

else:
    print("Matchen blev oavgjord")                                                  # Oavett ovan blir matchen oavgjord då man förutsätter att matchen blev lika. Tar inte hänsyn till walk over