"""
A module for main file that creates the [ | ] format domino with left and right values
"""

def create(left, right):
    """
    Create a representation for a domino with the given left and right values
    :param left: an integer for the left value
    :param right: an integer for the right value
    :return: a tuple of left and right values
    """
    domino = (left, right)

    return domino

def get_left(domino):
    """
    Get the left value of a given domino
    :param domino: a tuple of left and right values
    :return: an integer for the left value
    """
    left = domino[0]

    return left

def get_right(domino):
    """
    Get the right value of a given domino
    :param domino: a tuple of left and right value
    :return: an integer for right value
    """
    right = domino[1]

    return right

def as_str(domino):
    """
    Get the [ | ] format domino with left and right values
    :param domino: a tuple of left and right values
    :return: a string with left and right values
    """
    return "[%d | %d]" % (get_left(domino), get_right(domino))