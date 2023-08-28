"""
Models a 5-card hand of cards
"""

import copy
from deck import *

TIE = 0
MAX_HAND = 5
FIRST_CARD = 0
LAST_CARD = 1
FLUSH = 4
TWO_PAIR = 3
PAIR = 2
HIGH_CARD = 1

class PokerHand:

    def __init__(self, list_o_cards):
        """
        Constructor

        :param list_o_cards: a list of Card objects
        """
        self.__hand = copy.deepcopy(list_o_cards)

    def __add_card(self, card):
        """
        Adds the card to the hand

        :param card: a Card object
        :return: the PokerHand object with the additional card
        """
        return self.__hand.append(card)

    def __get_ith_card(self, index):
        """
        Returns the card at the given index

        :param index: an integer greater or equal to 0
        :return: a Card object at the given index
        """
        return self.__hand[index]

    def __str__(self):
        """
        Returns the readable version of the hand

        :return: a string for the readable version of the hand
        """
        return_string = ""

        for card in self.__hand:
           return_string += str(card) + "\n"

        return return_string

    def compare_to(self, other_hand):
        """
        Determines which of two poker hands is worth more. Returns an int
        which is either positive, negative, or zero depending on the comparison.

        :param self: The first hand to compare
        :param other_hand: The second hand to compare
        :return: a negative number if self is worth LESS than other_hand,
        zero if they are worth the SAME (a tie), and a positive number if
        self is worth MORE than other_hand
        """
        hand_point = self.__get_point()
        other_point = other_hand.__get_point()

        result = hand_point - other_point

        if result == TIE:
            if hand_point == FLUSH or hand_point == HIGH_CARD:
                self.__get_rank_list()
                other_hand.__get_rank_list()

                for i in range (MAX_HAND):
                    result = self.__get_ith_rank(i) - other_hand.__get_ith_rank(i)

                    if result != TIE:
                        return result

            elif hand_point == TWO_PAIR or hand_point == PAIR:

                for i in range (self.__rank_list_size()):
                    result = self.__get_ith_rank(i) - other_hand.__get_ith_rank(i)

                    if result != TIE:
                        return result

        return result

    def __get_point(self):
        """
        Gets the point of the hand

        :return: an integer for the score of the hand
        """
        if self.__is_flush():
            hand_score = FLUSH

        elif self.__is_two_pair():
            hand_score = TWO_PAIR

        elif self.__is_pair():
            hand_score = PAIR

        else:
            hand_score = HIGH_CARD

        return hand_score

    def __get_rank_list(self):
        """
        Gets the list with ranks in the descending order

        :return:
        """
        rank_list = []

        for card in self.__hand:
            rank_list.append(card.get_rank())

        rank_list.sort(reverse = True)

        self.__rank_list = rank_list

    def __get_ith_rank(self, index):
        """
        Returns the rank at the given index
        :param index: an integer for the index of the rank
        :return: an integer at the given index
        """
        return self.__rank_list[index]

    def __rank_list_size(self):
        """
        Returns the size of the rank list

        :return: an integer for the size of the rank list
        """
        return len(self.__rank_list)

    def __copy(self):
        """
        Stores a copy of the original value

        :param original: a value for the copy
        :return: a copied value with the new reference
        """
        return copy.deepcopy(self)

    def __size(self):
        """
        Returns the number of cards left in the hand

        :return: an integer for cards left in the hand
        """
        return len(self.__hand)

    def __remove_ith_card(self, index):
        """
        Removes the card with the given index

        :param index: an integer for the index of the card
        :return: a PokerHand object without the removed card
        """
        return self.__hand.remove(self.__hand[index])

    def __is_flush(self):
        """
        Checks whether the hand is flush

        :return: True if all cards have the same suit
        """
        for i in range (1, MAX_HAND):
            if self.__get_ith_card(i).get_suit() != self.__get_ith_card(i - 1).get_suit():
                return False

        return True

    def __is_two_pair(self):
        """
        Checks whether the hand is two pair

        :return: True if the hand has 2 pairs of the same rank
        """
        current_hand = self.__copy()

        i = 1
        total_pair = 0
        pair_rank = []
        other_rank = []

        while current_hand.__size() > i:
            if current_hand.__get_ith_card(FIRST_CARD).get_rank() == current_hand.__get_ith_card(i).get_rank():
                total_pair += 1

                pair_rank.append(current_hand.__get_ith_card(FIRST_CARD).get_rank())

                current_hand.__remove_ith_card(i)
                current_hand.__remove_ith_card(FIRST_CARD)

                i = 1

            else:
                i += 1

            if current_hand.__size() == i:
                other_rank.append(current_hand.__get_ith_card(FIRST_CARD).get_rank())

                current_hand.__remove_ith_card(FIRST_CARD)

                i = 1

            if current_hand.__size() == LAST_CARD:
                other_rank.append(current_hand.__get_ith_card(FIRST_CARD).get_rank())

                current_hand.__remove_ith_card(FIRST_CARD)

        if total_pair == 2:
            pair_rank.sort(reverse = True)
            other_rank.sort(reverse = True)

            pair_rank.extend(other_rank)

            self.__rank_list = pair_rank

            return True

        return False

    def __is_pair(self):
        """
        Checks whether the hand is a pair

        :return: True if the hand has a pair of the same rank
        """
        current_hand = self.__copy()

        i = 1
        total_pair = 0
        pair_rank = []
        other_rank = []

        while current_hand.__size() > i:
            if current_hand.__get_ith_card(FIRST_CARD).get_rank() == current_hand.__get_ith_card(i).get_rank():
                total_pair += 1

                pair_rank.append(current_hand.__get_ith_card(FIRST_CARD).get_rank())

                current_hand.__remove_ith_card(i)
                current_hand.__remove_ith_card(FIRST_CARD)

                i = 1

            else:
                i += 1

            if current_hand.__size() == i:
                other_rank.append(current_hand.__get_ith_card(FIRST_CARD).get_rank())

                current_hand.__remove_ith_card(FIRST_CARD)

                i = 1

            if current_hand.__size() == LAST_CARD:
                other_rank.append(current_hand.__get_ith_card(FIRST_CARD).get_rank())

                current_hand.__remove_ith_card(FIRST_CARD)

        if total_pair == 1:
            pair_rank.sort(reverse = True)
            other_rank.sort(reverse = True)

            pair_rank.extend(other_rank)

            self.__rank_list = pair_rank

            return True

        return False

    def get_result(self, other_hand):
        """
        Gets the result according to the given value

        :return: a string according to the given value
        """
        result = self.compare_to(other_hand)

        if result > 0:
            return "my hand"

        elif result < 0:
            return "other hand"

        else:
            return "tie"

def __confirm_result():
    deck = Deck()
    myhand = PokerHand(deck.list_o_cards())
    other_hand = PokerHand(deck.list_o_cards())
    result = myhand.get_result(other_hand)

    print("my hand: ", myhand)
    print("other hand: ", other_hand)
    print("result: ", result, " won.")

if __name__ == "__main__":
    __confirm_result()