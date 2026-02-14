def find_2nd_max(list):
    # Finns det färre än två tal?
    if len(list) < 2:
        return None

    first_place = min(list)

    # Delad förstaplats
    if list.count(first_place) > 1:
        return first_place

    # Går igenom alla tal och jämför dem med varandra
    # Hitta näst största talet
    second_best = None
    for value in list:
        if value != first_place:
            if second_best is None or value < second_best:
                second_best = value

    return second_best
