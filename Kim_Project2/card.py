"""
Models a single card
"""

JACK = 11
QUEEN = 12
KING = 13
ACE = 14
HEARTS = "H"
DIAMONDS = "D"
SPADES = "S"

class Card:

    def __init__(self, rank, suit):
        """
        Constructor

        :param rank: an integer for the rank of the card
        :param suit: a string for the suit of the card
        """
        self.__card = {"rank": rank, "suit": suit}

    def get_rank(self):
        """
        Gets the rank of the card

        :return: an integer for the rank of the card
        """
        return self.__card["rank"]

    def get_suit(self):
        """
        Gets the suit of the card

        :return: an integer for the suit of the card
        """
        return self.__card["suit"]

    def __str__(self):
        """
        Returns the readable version of the card

        :return: a string for the readable version of the card
        """
        rank = self.get_rank()
        suit = self.get_suit()

        if rank == JACK:
            rank_string = "Jack"

        elif rank == QUEEN:
            rank_string = "Queen"

        elif rank == KING:
            rank_string = "King"

        elif rank == ACE:
            rank_string = "Ace"

        else:
            rank_string = str(rank)

        if suit == HEARTS:
            suit_string = "Hearts"

        elif suit == DIAMONDS:
            suit_string = "Diamonds"

        elif suit == SPADES:
            suit_string = "Spades"

        else:
            suit_string = "Clubs"

        return rank_string + " of " + suit_string

def __confirm_result():
    card = Card(11, "C")

    print(card)

if __name__ == "__main__":
    __confirm_result()