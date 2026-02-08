

def print_poker_result(is_straight_flush, is_fyrtal, is_house, is_suit, is_stege, is_tretal, is_two_pair, is_one_pair):
    if is_straight_flush:
        print("Grattis! Du har fått: Straight flush!")

    elif is_fyrtal:
        print("Grattis! Du har fått: Fyrtal")

    elif is_house:
        print("Grattis! Du har fått: Kåk")

    elif is_suit:
        print("Grattis! Du har fått: Kåk")

    elif is_stege:
        print("Grattis! Du har fått: Stege")

    elif is_tretal:
        print("Grattis! Du har fått: Tretal")

    elif is_two_pair:
        print("Grattis! Du har fått: Två par")

    elif is_one_pair:
        print("Grattis! Du har fått: Ett par")

    else:
        print("Ledsen! Du har ingen pokerhand")
