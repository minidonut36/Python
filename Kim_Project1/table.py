"""
Computes a table

:reflection: Imported files called deck and hands for the modularity.
Used named constant like ATTEMPTS because it is convenient to change its value throughout the code.
Defined functions called first_row and get_result for the modularity.
Defined a function called get_percentage and get_content for the modularity and information hiding.
Used helper functions like d.create_standard() for the modularity.
"""

import deck as d
import hands as h

ATTEMPTS = 10000

def first_row():
    """
    Outputs the first row of the table

    :return:
    """
    print('{} {:>7} {:^7} {:>9} {:^7} {:>9} {:^7} {:>11} {:^7}'.format('# of hands', 'pairs', '%', '2 pairs', '%',
                                                                          'flushes', '%', 'high card', '%'))
def get_percentage(number, total_attempt):
    """
    Gets percentage with the given number and total attempt

    :param number: an integer for the division
    :param total_attempt: an integer for the division
    :return: an integer converted into a percentage
    """
    return number / total_attempt * 100

def get_result(total_attempt):
    """
    Gets each total number of flush, two pair, pair, and high card and computes each percentage

    :return: a list of total numbers and percentages
    """
    total_flush = 0
    total_two_pair = 0
    total_pair = 0
    total_high_card = 0

    deck = d.create_standard()
    d.random.shuffle(deck)

    for i in range(total_attempt):
        if d.cards_remaining(deck) < 5:
            deck = d.create_standard()
            d.shuffle(deck)

        hands = h.create_hands(deck)

        if h.is_flush(hands):
            total_flush += 1

        elif h.is_two_pair(hands):
            total_two_pair += 1

        elif h.is_pair(hands):
            total_pair += 1

        else:
            total_high_card += 1

    return [total_attempt, total_pair, get_percentage(total_pair, total_attempt), total_two_pair,
            get_percentage(total_two_pair, total_attempt), total_flush, get_percentage(total_flush, total_attempt),
            total_high_card, get_percentage(total_high_card, total_attempt)]

def get_content(total_result, content_order):
    """
    Gets content from the given total result

    :param total_result: a list of total numbers and percentages
    :param content_order: an integer for the index of specific content
    :return: an integer or float for the specific content
    """
    return total_result[content_order]

def output_table(total_result):
    """
    Outputs the table with total numbers and percentages

    :param total_list: a list of total numbers
    :return:
    """
    print('{:>10,} {:>7} {: 06.2f} {:>10} {: 06.2f} {:>10} {: 06.2f} {:>12} {: 06.2f}'.
          format(get_content(total_result, 0), get_content(total_result, 1), get_content(total_result, 2),
                 get_content(total_result, 3), get_content(total_result, 4), get_content(total_result, 5),
                 get_content(total_result, 6), get_content(total_result, 7), get_content(total_result, 8)))

if __name__ == "__main__":
    first_row()
    output_table(get_result(ATTEMPTS))