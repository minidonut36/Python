"""
Models hands and analyzes cards

:reflection: Imported files called deck and card for the modularity.
Used named constants like MAX_HANDS because it is convenient to change their values throughout the code.
Used helper functions like d.draw(deck) for the modularity.
Defined functions called hands_extend and card_remove for the modularity and information hiding.
Defined functions starts with "is_..." for the modularity.
Used helper functions like get_suit(hands, i) for the modularity and information hiding.
"""

import deck as d
import card as c

MAX_HANDS = 5
ATTEMPTS = 10000

def create_hands(deck):
    """
    Creates a list for pocker hands with 5 cards
    :return: a list for poker hands
    """
    hands = []

    for hand in range (MAX_HANDS):
        hands.append(d.draw(deck))

    return hands

def hands_extend(current_hands, given_hands):
    """
    Extends current hands with given hands

    :param current_hands: a list for current hands
    :param given_hands: a list for given hands
    :return: a list for extended hands
    """
    return current_hands.extend(given_hands)

def card_remove(hands, card_order):
    """
    Removes the card with the card order from hands

    :param hands: a list for hands
    :param card_order: an integer for card number
    :return: a list for modified hands
    """
    return hands.remove(hands[card_order])

def is_flush(hands):
    """
    Checks whether hands are flush

    :param hands: a list for hands
    :return: True if all cards have the same shape
    """
    for i in range(1, MAX_HANDS):
        if c.get_suit(hands, i) != c.get_suit(hands, i - 1):
            return False

    return True

def is_two_pair(hands):
    """
    Checks whether hands are two pair

    :param current_hands: a list for hands
    :return: True if hands have 2 pairs of the same number or character
    """
    current_hands = []
    hands_extend(current_hands, hands)

    total_pair = 0
    i = 1

    while len(current_hands) > i:
        if c.get_num_char(current_hands, 0) == c.get_num_char(current_hands, i):
            total_pair += 1

            card_remove(current_hands, i)
            card_remove(current_hands, 0)

            i = 1

        else:
            i += 1

        if i == len(current_hands):
            card_remove(current_hands, 0)

            i = 1

    if total_pair == 2:
        return True

    return False

def is_pair(hands):
    """
    Checks whether hands are two pair

    :param current_hands: a list for hands
    :return: True if hands have a pairs of the same number or character
    """
    current_hands = []
    hands_extend(current_hands, hands)

    total_pair = 0
    i = 1

    while len(current_hands) > i:
        if c.get_num_char(current_hands, 0) == c.get_num_char(current_hands, i):
            total_pair += 1

            card_remove(current_hands, i)
            card_remove(current_hands, 0)

            i = 1

        else:
            i += 1

        if i == len(current_hands):
            card_remove(current_hands, 0)

            i = 1

    if total_pair == 1:
        return True

    return False

def confirm_result(hands):
    """
    Confirms the actual result of hands

    :param hands: a list for hands
    :return:
    """
    if is_flush(hands):
        print(hands, " is flush")

    elif is_two_pair(hands):
        print(hands, " is two pair")

    elif is_pair(hands):
        print(hands, " is pair")

    else:
        print(hands, "is high card")

if __name__ == "__main__":
    deck = d.create_standard()

    for i in range (10):
        hands = create_hands(deck)

        confirm_result(hands)