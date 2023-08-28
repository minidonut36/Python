"""
Models a deck

:reflection: Used named constants like MAX_NUMBER because it is convenient to change their values throughout the code.
Used string for cards like "2C" (two clover) because it is easy to compare their numbers, characters, or suits
if their lengths and index are similar.
Defined functions called shuffle, draw, and card_remaining for the modularity.
"""

import random

MAX_NUMBER = 10
SUITS = ["C", "D", "H", "S"]
CHARACTERS = ["A", "J", "Q", "K"]

def create_number():
    """
    Creates a deck of number cards

    :return: a list for a deck of number cards
    """
    number_deck = []

    for i in range (2, MAX_NUMBER + 1):
        for j in SUITS:
            number_deck.append(str(i) + j)

    return number_deck

def create_standard():
    """
    Creates a standard deck of 52 cards

    :return: a list for a deck of cards
    """
    standard_deck = create_number()

    for i in CHARACTERS:
        for j in SUITS:
            standard_deck.append(i + j)

    return standard_deck

def shuffle(deck):
    """
    Shuffles the deck

    :param deck: a list for a deck of cards
    :return: a list for a shuffled deck of cards
    """
    return random.shuffle(deck)

def draw(deck):
    """
    Draw a card from the standard deck

    :param deck: a list for a deck of cards
    :return: a string drawn randomly
    """
    return deck.pop(random.randrange(0, len(deck)))

def cards_remaining(deck):
    """
    Returns a number of cards left in the deck

    :param deck: a list for a deck of cards
    :return: an integer for cards left
    """
    return len(deck)

if __name__ == "__main__":
    deck = create_standard()

    print("deck: ", deck)
    print("card: ", draw(deck))
    print("cards remaining: ", cards_remaining(deck))