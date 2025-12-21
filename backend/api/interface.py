import json


class PokerHandInterface():
    """
    This class is responsible for evaluating a five card poker hand and produce
    a poker hand ranking.
    """
    def __init__(self, poker_hand: list[dict], validate_hand: bool = False):
        self.poker_hand = poker_hand
        self.validate_hand = validate_hand

        print(json.dumps(self.poker_hand, indent=4))

    def is_valid(self):
        """
        Should an API be exposed, then hand validation will be required.
        Currently, the integration with our own Angular front-end, is designed
        in such a manner that only valid poker hands are received. So by default,
        we expect this function to return True.
        * This may change as we progress with this class.

        Returns:
             True if valid, False otherwise.
        """
        if self.validate_hand:
            return False

        return True


    def get_ranking(self) -> str:
        """
        Determines the poker hand ranking based on the poker hand.

        Returns:
             A string representing the poker hand ranking.
        """
        return "POKER RANKING IN PROGRESS"
