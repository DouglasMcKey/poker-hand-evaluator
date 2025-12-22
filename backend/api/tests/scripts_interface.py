"""
This file contains scripts to quickly test the PokerHandInterface as functionality
is being built. It serves for debugging during development.
"""
#!/usr/bin/env python
import os
import sys
import django

from pathlib import Path

BASE_DIRECTORY = Path(__file__).resolve(strict=True).parent.parent.parent

sys.path.append(f"{BASE_DIRECTORY}")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings.development")

django.setup()

from backend.api.tests.fixtures import (
    create_hand_royal_flush, sorted_hand_royal_flush, create_hand_straight_flush,
    create_hand_flush, create_hand_four_of_a_kind, create_hand_full_house,
    create_hand_straight
)
from backend.api.interface import PokerHandInterface


def get_cards(
    sorted_hand: bool = False,
    royal_flush: bool = False,
    straight_flush: bool = False,
    flush: bool = False,
    four_of_a_kind: bool = False,
    full_house: bool = False,
    straight: bool = False,
) -> list:
    """
    Returns a five poker hand cards that can be used to test the PokerHandInterface.
    """
    if sorted_hand:
        return sorted_hand_royal_flush()

    elif royal_flush:
        return create_hand_royal_flush()

    elif straight_flush:
        return create_hand_straight_flush()

    elif flush:
        return create_hand_flush()

    elif four_of_a_kind:
        return create_hand_four_of_a_kind()

    elif full_house:
        return create_hand_full_house()

    elif straight:
        return create_hand_straight()

    return []


def test_is_valid():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_valid())


def test_sort_hand():
    unsorted_hand = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(unsorted_hand)
    poker_hand.sort_hand()
    print(poker_hand.cards)


def test_set_high_and_low_cards():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    poker_hand.set_high_and_low_cards()
    print(poker_hand.low_card)
    print(poker_hand.high_card)


def test_set_card_face_values():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    poker_hand.set_card_face_values()
    print(poker_hand.card_face_values)


def test_get_total_value():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.get_total_value())


def test_is_royal_flush():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_royal_flush())
    print(poker_hand.hand_suit)
    print(poker_hand.get_ranking())


def test_is_straight_flush():
    cards = get_cards(straight_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_straight_flush())
    print(poker_hand.hand_suit)
    print(poker_hand.get_ranking())


def test_is_four_of_a_kind():
    cards = get_cards(four_of_a_kind=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_four_of_a_kind())
    print(poker_hand.get_ranking())


def test_is_full_house():
    cards = get_cards(full_house=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_full_house())
    print(poker_hand.get_ranking())


def test_is_flush():
    cards = get_cards(straight_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_flush())
    print(poker_hand.hand_suit)
    print(poker_hand.get_ranking())


def test_is_straight():
    cards = get_cards(straight=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_straight())
    print(poker_hand.get_ranking())


def main():
    # test_is_valid()
    # test_sort_hand()
    # test_set_high_and_low_cards()
    # test_set_card_face_values()
    # test_get_total_value()

    # test_is_royal_flush()
    # test_is_straight_flush()
    # test_is_four_of_a_kind()
    # test_is_full_house()
    # test_is_flush()
    # test_is_straight()
    print("Done!")


if __name__ == "__main__":
    main()
