"""
Analyzes a card

:reflection: Defined functions called get_suit and get_num_char for information hiding.
"""

def get_suit(hands, card_order):
    """
    Gets the card suit with the card order from hands

    :param hands: a list for hands
    :param card_order: an integer for the index of specific card
    :return: a string for the card suit
    """
    return hands[card_order][len(hands[card_order]) - 1]

def get_num_char(hands, card_order):
    """
    Gets the card number or character with the card order from hands

    :param hands: a list for hands
    :param card_order: an integer for the index of specific card
    :return: a string for the card number or character
    """
    return hands[card_order][0: len(hands[card_order]) - 1]

if __name__ == "__main__":
    print("expected suit: C, actual suit: ", get_suit(["AC", "2D", "3H", "4S", "5S"], 0))
    print("expected number: A, actual number: ", get_num_char(["AC", "2D", "3H", "4S", "5S"], 0))