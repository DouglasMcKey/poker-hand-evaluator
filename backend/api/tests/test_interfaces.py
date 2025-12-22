from django.test import SimpleTestCase

from api.interface import PokerHandInterface
from api.tests.fixtures import (
    create_hand_royal_flush, create_hand_straight_flush, create_hand_four_of_a_kind,
    create_hand_full_house, create_hand_flush, create_hand_straight
)


class TestAPIPokerHandInterface(SimpleTestCase):
    """
    This is used to unit test the `PokerHandInterface`.

    > pipenv run python manage.py test api.tests.test_interfaces -v 2 --failfast
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.royal_flush_hand = create_hand_royal_flush()
        cls.straight_flush = create_hand_straight_flush()
        cls.four_of_a_kind = create_hand_four_of_a_kind()
        cls.full_house = create_hand_full_house()
        cls.flush = create_hand_flush()
        cls.straight = create_hand_straight()

    def test_is_valid(self):
        poker_hand = PokerHandInterface(self.royal_flush_hand)
        self.assertTrue(poker_hand.is_valid())

        invalid_hand = []
        poker_hand = PokerHandInterface(invalid_hand)
        self.assertFalse(poker_hand.is_valid())

    def test_royal_flush(self):
        poker_hand = PokerHandInterface(self.royal_flush_hand)
        is_royal_flush = poker_hand.is_royal_flush()
        self.assertTrue(is_royal_flush)

    def test_straight_flush(self):
        poker_hand = PokerHandInterface(self.straight_flush)
        is_straight_flush = poker_hand.is_straight_flush()
        self.assertTrue(is_straight_flush)

    def test_four_of_a_kind(self):
        poker_hand = PokerHandInterface(self.four_of_a_kind)
        is_four_of_a_kind = poker_hand.is_four_of_a_kind()
        self.assertTrue(is_four_of_a_kind)

    def test_full_house(self):
        poker_hand = PokerHandInterface(self.full_house)
        is_full_house = poker_hand.is_full_house()
        self.assertTrue(is_full_house)

    def test_straight(self):
        poker_hand = PokerHandInterface(self.straight)
        is_straight = poker_hand.is_straight()
        self.assertTrue(is_straight)
