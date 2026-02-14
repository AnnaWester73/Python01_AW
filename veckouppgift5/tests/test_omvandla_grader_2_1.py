from veckouppgift5.omvandla_grader_2_1 import c_to_f

# Uppgict 1a
def test_c_to_f_normal_temperature ():

    # Normala grader plus och minus
    assert c_to_f(0) == 32                              #Fryspunkt
    assert c_to_f(100) == 212                           #Kokpunkt
    assert c_to_f(22) == 71.6                           #Inomhus temperatur
    assert c_to_f(-10) == 14                            #Utonhus temperatur

def test_c_to_f_total_temperature ():
    # Gränsvärde i funktion
    assert c_to_f(-273.15) == -459.66999999999996       # Gränsvärde i funktion

#Uppgift 1b
def test_c_to_f_equivalence():

    # Giltiga värden (degree >= -273.15)
    # Normala grader plus och minus
    assert c_to_f(0) == 32                              #Fryspunkt
    assert c_to_f(100) == 212                           #Kokpunkt
    assert c_to_f(22) == 71.6                           #Inomhus temperatur
    assert c_to_f(-10) == 14                            #Utonhus temperatur

    # Ogiltiga temperaturer (degree < -273.15)
    assert c_to_f(-273.16) is None

# Uppgift 1c
def test_c_to_f_invalid_temperature ():
    assert c_to_f(-300) is None













