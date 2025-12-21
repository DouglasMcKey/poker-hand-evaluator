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


def get_cards():
    """
    Returns five poker hand cards that can be used to test the PokerHandInterface.
    """
    poker_cards = create_hand_royal_flush()

    return poker_cards


def test_is_valid(cards):
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.is_valid())


def test_get_ranking(cards):
    poker_hand = PokerHandInterface(cards)
    print(poker_hand.get_ranking())


def main():
    cards = get_cards()

    test_is_valid(cards)
    # test_get_ranking(cards)
    print("Done!")


if __name__ == "__main__":
    main()
