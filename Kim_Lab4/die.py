"""
Models a die

:author: Chris Hegang Kim
:note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.
"""

import random

MINIMUM_VAL = 1
TWICE = 2
DEFAULT_SIDE = 6

class Die:

    def __init__(self, side_num = DEFAULT_SIDE):
        """
        Constructor

        :param side_num: the number of sides the die has
        """
        self.__side_num = side_num
        self.__current_val = MINIMUM_VAL

    def roll(self):
        """
        Rolls the die and reassigns the current value instance variable

        :return:
        """
        self.__current_val = (random.randint(MINIMUM_VAL, self.__side_num))

    def get_value(self):
        """
        Gets the value currently showing on the die

        :return: the value currently showing on the die
        """
        return self.__current_val

    def is_twice(self, other_die):
        """
        Checks whether one of the dice shows a value that is exactly twice the value of the other

        :param other_die: a Die object for the other die for comparison
        :return: True if the value of other die is two times larger than the value of current die itself
        """
        if self.get_value() == other_die.get_value() * TWICE:
            return True

        else:
            return False

    def __str__(self):
        """
        Converts to the human understandable string

        :return: a human understandable string for the current value of the die
        """
        return str(self.__current_val)