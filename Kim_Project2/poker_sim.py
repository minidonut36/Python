"""
A simple pocker game

:author: Chris Hegang Kim
:note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.
"""

from poker_hand import *

CONTINUE = True
TWO_MAX_HAND = 10

def main():
    deck = Deck()
    continue_game = CONTINUE
    total_point = 0

    while continue_game and deck.size() > TWO_MAX_HAND:
        myhand = PokerHand(deck.list_o_cards())
        other_hand = PokerHand(deck.list_o_cards())
        result = myhand.get_result(other_hand)

        print("my hand: ", myhand)
        print("other hand: ", other_hand)

        player_input = input("Who is the winner? (Type my hand, other hand, or tie)")

        if player_input == result:
            total_point += 1

        else:
           continue_game = not CONTINUE

    print("Game is over, and your total point is ", total_point)

if __name__ == "__main__":
    main()