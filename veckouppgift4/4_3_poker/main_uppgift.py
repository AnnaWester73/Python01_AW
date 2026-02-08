from hand import draw_hand
from flush import straight_flush
from fyrtal import fyrtal
from house  import house
from suits import suit
from straight import stege
from tretal import  tretal
from twopair import two_pair
from onepair import one_pair
from pokerhand_results import print_poker_result



SUIT_ICONS = {
    "Spader": "♠",
    "Hjärter": "♥",
    "Ruter": "♦",
    "Klöver": "♣"
}


def pretty_icon(colour):
    return SUIT_ICONS.get(colour, colour)

def print_hand(cards):
    print("Du fick kort:")
    for i, (colour, value) in enumerate(cards, start=1):
        print(f"{i}. {pretty_icon(colour)} {value}")

# Funktion som för att skriva ut vilken pokerhand pokerhand_results.py
# hämtar funktioner från alla olika varianter
def main():
    hand = draw_hand()
    print_hand(hand)

    is_straight_flush = straight_flush(hand)
    is_fyrtal = fyrtal(hand)
    is_house = house(hand)
    is_suit = suit(hand)
    is_stege = stege(hand)
    is_tretal = tretal(hand)
    is_two_pair = two_pair(hand)
    is_one_pair = one_pair(hand)

    print_poker_result(is_straight_flush, is_fyrtal, is_house, is_suit, is_stege, is_tretal, is_two_pair, is_one_pair)

if __name__ == "__main__":
    main()
