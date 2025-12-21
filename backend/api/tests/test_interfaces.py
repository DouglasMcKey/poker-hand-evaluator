from django.test import SimpleTestCase, TestCase, RequestFactory

from api.interface import PokerHandInterface
from api.tests.fixtures import create_hand_royal_flush


class TestAPIPokerHandInterface(SimpleTestCase):
    """
    This test case is used to test the `PokerHandInterface`.
    > pipenv run python manage.py test api.tests.test_interfaces -v 2 --failfast
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.royal_flush = create_hand_royal_flush()

    def test_is_valid(self):
        poker_hand = PokerHandInterface(self.royal_flush)
        self.assertTrue(poker_hand.is_valid())

        invalid_poker_hand = []
        poker_hand = PokerHandInterface(invalid_poker_hand, validate_hand=True)
        self.assertFalse(poker_hand.is_valid())

    # def test_royal_flush(self):
    #     poker_hand = PokerHandInterface(self.royal_flush)
    #     self.assertTrue(poker_hand.is_royal_flush())
