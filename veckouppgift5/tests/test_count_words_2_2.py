from veckouppgift5.count_words_2_2 import count_words

#Normal användning
#Mellanslagshantering
#Specialtecken
#Siffror
#Kantfall
#Robusthet mot oregelbunden spacing

# AK1 – Normala meningar
def test_normal_count_words ():
    assert count_words("Godmorgon OS") == 2
    assert count_words("En kall lördag morgon") == 4

# AK2 Test 1 ord
def test_single_word():
    assert count_words("Lördag") == 1
    assert count_words("Hej") == 1

# AK3 – Tom sträng
def test_empty_count_words ():
    assert count_words("") == 0

# AK4 – Ledande och avslutande mellanslag
def test_begin_end_space_count_words ():
    assert count_words(" Godmorgon OS ") == 2
    assert count_words(" En kall lördag morgon    ") == 4

# AK5 – Flera mellanslag mellan ord
def test_multiple_spaces_between_words():
    assert count_words("En  kall   lördag    morgon") == 4
    assert count_words("Godmorgon  OS") == 2

# AK6 – Specialtecken
def test_special_char_count_words ():
    assert count_words("Godmorgon OS !") == 3
    assert count_words("En kall lördag morgon ?") == 5

# AK7 – Endast mellanslag
def test_only_spaces():
    assert count_words("   ") == 0



