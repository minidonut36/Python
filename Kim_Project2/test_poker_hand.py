from testing import *
from poker_hand import *

def __test_poker_hand():
    start_tests("Starts testing poker_hand module")
    __test_compare_to()
    finish_tests()

def __test_compare_to():
    __flush_v_two_pair()
    __flush_v_flush_high_card1()
    __flush_v_flush_high_card2()
    __flush_v_flush_high_card3()
    __flush_v_flush_high_card4()
    __flush_v_flush_high_card5()
    __flush_v_flush_tie()

    __two_pair_v_pair()
    __two_pair_v_two_pair_high_card1()
    __two_pair_v_two_pair_high_card2()
    __two_pair_v_two_pair_high_card3()
    __two_pair_v_two_pair_tie()

    __pair_v_high_card()
    __pair_v_pair_high_card1()
    __pair_v_pair_high_card2()
    __pair_v_pair_high_card3()
    __pair_v_pair_high_card4()
    __pair_v_pair_tie()

    __high_card_v_high_card1()
    __high_card_v_high_card2()
    __high_card_v_high_card3()
    __high_card_v_high_card4()
    __high_card_v_high_card5()
    __high_card_v_high_card_tie()

def __flush_v_two_pair():
    hand = PokerHand([Card(14, "H"), Card(14, "H"), Card(8, "H"), Card(7, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(8, "C"), Card(9, "H")])
    msg = "Starts testing flush vs two pair"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __flush_v_flush_high_card1():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H"), Card(9, "H")])
    msg = "Starts testing flush vs flush (first high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __flush_v_flush_high_card2():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H"), Card(9, "H")])
    msg = "Starts testing flush vs flush (second high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __flush_v_flush_high_card3():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(11, "H"), Card(10, "H"), Card(9, "H")])
    msg = "Starts testing flush vs flush (third high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __flush_v_flush_high_card4():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(10, "H"), Card(9, "H")])
    msg = "Starts testing flush vs flush (fourth high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __flush_v_flush_high_card5():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(9, "H")])
    msg = "Starts testing flush vs flush (fifth high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __flush_v_flush_tie():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    msg = "Starts testing flush vs flush (tie)"
    expected = 0
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)


def __two_pair_v_pair():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(8, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(9, "C"), Card(10, "H")])
    msg = "Starts testing two pair vs pair"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)


def __two_pair_v_two_pair_high_card1():
    hand = PokerHand([Card(14, "H"), Card(14, "H"), Card(8, "H"), Card(8, "H"), Card(9, "H")])
    other_hand = PokerHand([Card(13, "H"), Card(13, "H"), Card(11, "H"), Card(11, "H"), Card(9, "H")])
    msg = "Starts testing two pair vs two pair (first high pair card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)


def __two_pair_v_two_pair_high_card2():
    hand = PokerHand([Card(14, "H"), Card(14, "H"), Card(8, "H"), Card(8, "H"), Card(9, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "H"), Card(7, "H"), Card(7, "H"), Card(9, "H")])
    msg = "Starts testing two pair vs two pair (second high pair card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)


def __two_pair_v_two_pair_high_card3():
    hand = PokerHand([Card(14, "H"), Card(14, "H"), Card(8, "H"), Card(8, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "H"), Card(8, "H"), Card(8, "H"), Card(9, "H")])
    msg = "Starts testing two pair vs two pair (third high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)


def __two_pair_v_two_pair_tie():
    hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "H"), Card(12, "H"), Card(11, "H"), Card(10, "H")])
    msg = "Starts testing two pair vs two pair (tie)"
    expected = 0
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __pair_v_high_card():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(9, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(8, "S"), Card(9, "C"), Card(10, "H")])
    msg = "Starts testing pair vs high card"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __pair_v_pair_high_card1():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(9, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(13, "H"), Card(13, "D"), Card(8, "S"), Card(9, "C"), Card(10, "H")])
    msg = "Starts testing pair vs pair (first high pair card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __pair_v_pair_high_card2():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(9, "C"), Card(11, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(9, "C"), Card(10, "H")])
    msg = "Starts testing pair vs pair (second high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __pair_v_pair_high_card3():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(10, "C"), Card(11, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(9, "C"), Card(11, "H")])
    msg = "Starts testing pair vs pair (third high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __pair_v_pair_high_card4():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(9, "S"), Card(10, "C"), Card(11, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(8, "S"), Card(10, "C"), Card(11, "H")])
    msg = "Starts testing pair vs pair (fourth high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __pair_v_pair_tie():
    hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(9, "S"), Card(10, "C"), Card(11, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(14, "D"), Card(9, "S"), Card(10, "C"), Card(11, "H")])
    msg = "Starts testing pair vs pair (tie)"
    expected = 0
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)


def __high_card_v_high_card1():
    hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(13, "H"), Card(12, "D"), Card(11, "S"), Card(10, "C"), Card(9, "H")])
    msg = "Starts testing high card vs high card (first high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __high_card_v_high_card2():
    hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(12, "D"), Card(11, "S"), Card(10, "C"), Card(9, "H")])
    msg = "Starts testing high card vs high card (second high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __high_card_v_high_card3():
    hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(11, "S"), Card(10, "C"), Card(9, "H")])
    msg = "Starts testing high card vs high card (third high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __high_card_v_high_card4():
    hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(10, "C"), Card(9, "H")])
    msg = "Starts testing high card vs high card (fourth high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __high_card_v_high_card5():
    hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(9, "H")])
    msg = "Starts testing high card vs high card (fifth high card)"
    expected = 1
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

def __high_card_v_high_card_tie():
    hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    other_hand = PokerHand([Card(14, "H"), Card(13, "D"), Card(12, "S"), Card(11, "C"), Card(10, "H")])
    msg = "Starts testing high card vs high card (tie)"
    expected = 0
    actual = hand.compare_to(other_hand)

    assert_equals(msg, expected, actual)

if __name__ == "__main__":
    __test_poker_hand()