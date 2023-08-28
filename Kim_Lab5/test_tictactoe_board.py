"""
:author: Chris Hegang Kim
:note: I affirm that I have carried out the attached academic endeavors with full academic honesty,
in accordance with the Union College Honor Code and the course syllabus.
"""

from tictactoe_board import *
from testing import *


def test_get_winner():
    start_tests("Tests for tictactoe_board.get_winner()")
    test_get_winner_horiz_X()
    test_get_winner_vertical_X()
    test_get_winner_diagonal_X_L()
    test_get_winner_diagonal_X_R()
    test_get_winner_incomplete_board()
    test_get_winner_empty()
    finish_tests()

"""
Individual unit tests start here
"""

def test_get_winner_horiz_X():
    a_board = Tictactoe_board(['XXX',
                               'OOX',
                               'XOO'])
    assert_equals(str(a_board) + "Three Xs in a row horizontally",
                  'X',
                  a_board.get_winner())


def test_get_winner_vertical_X():
    a_board = Tictactoe_board(['XXO',
                               'XOX',
                               'XOO'])
    assert_equals(str(a_board) + "Three Xs in a row vertically",
                  'X',
                  a_board.get_winner())


def test_get_winner_diagonal_X_L():
    a_board = Tictactoe_board(['XOO',
                               'XXO',
                               'XOX'])
    assert_equals(str(a_board) + "Three Xs in a row in the left diagonal",
                  'X',
                  a_board.get_winner())


def test_get_winner_diagonal_X_R():
    a_board = Tictactoe_board(['XOX',
                               'XXO',
                               'XOO'])
    assert_equals(str(a_board) + "Three Xs in a row in the right diagonal",
                  'X',
                  a_board.get_winner())


def test_get_winner_incomplete_board():
    a_board = Tictactoe_board(['XXX',
                               'OOX',
                               'XOO'])
    a_board.clear_cell(0, 0)
    assert_equals(str(a_board) + "Incomplete board, no winner yet",
                  None,
                  a_board.get_winner())


def test_get_winner_empty():
    a_board = Tictactoe_board(None)
    assert_equals(str(a_board) + "Empty board, no winner yet",
                  None,
                  a_board.get_winner())


if __name__ == "__main__":
    test_get_winner()
