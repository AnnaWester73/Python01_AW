# Veckouppgift 5
#Skriv ner vad du tror kommer skrivas ut. Skriv sedan in koden i din IDE,
# exakt som den står, och kör den. Fick du samma resultat som du trodde? Om inte, varför?
# Uppgift 1 version 1
# Vilka ekvivalensklasser har uttrycken?


print("Uppgift 1a")
# Påstående x > 100 har två klasser
# x ≤ 100 ger False
# x > 100 ger True
# Exempel nedan skickar True tillbaka där 200 är större än 100

x = 200
print(x > 100)


print("Uppgift 1b")
# Påstående y == 42 har två ekvivalenta klasser
# y=42 ger True
# y != från 42 ger False
# Exempel nedan skickar True där y är lika med 42

y = 42
print(y == 42)

print("Uppgift 1c")
# Påstående len(text) >= 5 har två ekvivalenta klasser
# Längd mindre än 5 ger False
# Längden >= än 5 ger True
# Exempel nedan skickar False där längden på "text" är mindre än 5.

text = "text"
print(len(text) >= 5)

print("Uppgift 1d")
# Påståendet x == true har två ekvivalenta klasser
# z lika med True ger True
# z är False ger False
# Exempel skickar tillbaka True

z = True
print(z == True)

print("Uppgift 1e")
# Påståendet 8 < v < 16 har tre ekvivalenta klasser
# v mindre eller lika med ger False
# v större än 6 men mindre än 16 ger True
# v större eller lika med 16 ger False
# Exempel skickar tillbaka True

v = 10
print(8 < v < 16)

print("Uppgift 1f")
# Påståendet w == 32 or w == 64 or w == 128 har fyra ekvivalenta klasser
# w är lika med 32 ger True
# w är lika med 64 ger True
# w är lika med 128 ger True
# w är något annat ger False
# Exempel skickar tillbaka True

w = 32
print(w == 32 or w == 64 or w == 128)

print("Uppgift 1g")
# Påstående if x < 5: … elif x < 10: … elif x < 15: … else för att kontrollera villkor mellan olika intervaller

x = 10
if x < 5:
    print("x < 5")
elif x < 10:
    print("5 ≤ x < 10")
elif x < 15:
    print("10 ≤ x < 15")
else:
    print("x ≥ 15")






