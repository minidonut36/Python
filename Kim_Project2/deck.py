"""
Models a deck of cards
"""

from card import *
import random

RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
SUITS = ["H", "D", "S", "C"]
EMPTY = 0
TOP_CARD = 0
MAX_HAND = 5

class Deck:

    def __init__(self):
        """
        Constructor
        """
        self.__deck = []

        for rank in RANKS:
            for suit in SUITS:
                self.__deck.append(Card(rank, suit))

        self.__shuffle()

    def __shuffle(self):
        """
        Shuffles the deck

        :return: a list for the shuffled deck
        """
        return random.shuffle(self.__deck)

    def __deal(self):
        """
        Deals and returns a single card by removing the top card of the deck

        :return: a Card object which is the top card of the deck
        """
        if self.size() == EMPTY:
            return None

        else:
            return self.__deck.pop(TOP_CARD)

    def size(self):
        """
        Returns the number of cards left in the deck

        :return: an integer for cards left in the deck
        """
        return len(self.__deck)

    def __str__(self):
        """
        Returns the readable version of the deck

        :return: a string for the readable version of the deck
        """
        return_string = ""

        for card in self.__deck:
            return_string += str(card) + "\n"

        return return_string

    def list_o_cards(self):
        """
        Creates a list of Card objects

        :return: a list of Card objects
        """
        list_o_cards = []

        for i in range(MAX_HAND):
            list_o_cards.append(self.__deal())

        return list_o_cards

def __confirm_result():
    deck = Deck()

    print(deck)

if __name__ == "__main__":
    __confirm_result()