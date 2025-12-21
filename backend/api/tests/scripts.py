"""
This file contains scripts to quickly test the PokerHandInterface as functionality
is being built. It serves for debugging purposes.
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

from backend.api.tests.fixtures import create_hand_royal_flush
from backend.api.interface import PokerHandInterface


def get_cards(
    royal_flush: bool = True
) -> list:
    """
    Returns five poker hand cards that can be used to test the PokerHandInterface.
    """
    if royal_flush:
        return create_hand_royal_flush()

    return []


def test_is_valid():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_valid())


def test_is_flush():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_flush())


def test_is_royal_flush():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_royal_flush())


def test_get_ranking():
    cards = get_cards(royal_flush=True)
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.get_ranking())


def main():
    # test_is_valid()
    # test_is_royal_flush()
    # test_is_flush()
    # test_get_ranking()
    print("Done!")


if __name__ == "__main__":
    main()
