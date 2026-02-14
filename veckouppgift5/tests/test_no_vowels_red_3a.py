# Det behövs flera testfall för funktionen.
# Hur många vokaler finns det i (aeiouyåäö) både med små och stora bokstäver
# Finns det vokaler?
# Finns samma vokal flera gånger
# Finns det tecken som inte är bokstäver

from veckouppgift5.count_vowels_red_3a import count_vowels

def test_count_all_vowels():
    assert count_vowels("aeiouyåäö") == 9

def test_count_all_uppercase_vowels():
    assert count_vowels("AEIOUYÅÄÖ") == 9

def test_count_no_vowels():
    assert count_vowels("") == 0
    assert count_vowels ("zxc") == 0

def test_repeated_vowels():
    assert count_vowels ("aaaa") == 4
    assert count_vowels("eee") == 3

def test_vowels_and_consonants():
    assert count_vowels("pannkaka") == 3
    assert count_vowels("ödla") == 2




