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
        self.total_hand_value = sum(card["value"] for card in self.poker_hand)

        # Suit ranges.
        self.all_hearts = 500
        self.all_diamonds = 1000
        self.all_clubs = 1500
        self.all_spades = 2000


    def is_valid(self):
        """
        Currently, the integration with our own Angular front-end, is designed
        in such a manner that only valid poker hands are received. So by default,
        we expect this function to return True.
        TODO: We should always validate that the cards form a valid five card poker hand.

        Returns:
             True if valid, False otherwise.
        """
        if self.validate_hand:
            if len(self.poker_hand) != 5:
                return False

        return True

    def is_royal_flush(self) -> tuple:
        """
        To be considered a royal flush, the following must be True:
            - All cards are from the same suit.
            - Hand must include:
                10 (value: 10),
                Jack (value: 11),
                Queen (value: 12),
                King (value: 13),
                Ace  (value: 14)

        Returns:
            A tuple. E.g. (True, "Hearts"), (False, "Not suited")
        """
        is_flush, suit = self.is_flush()
        if not is_flush:
            return False, suit

        high_card_values = sum((10, 11, 12, 13, 14))
        if self.total_hand_value in [
            self.all_hearts + high_card_values,
            self.all_diamonds + high_card_values,
            self.all_clubs + high_card_values,
            self.all_spades + high_card_values
        ]:
            return True, suit
        else:
            return False, suit

    def is_straight_flush(self) -> tuple:
        """
        To be considered a straight flush, the following must be True:
            - All cards are from the same suit.
            - Hand must be of the form `straight`

        Returns:
            A tuple. E.g. (True, "9 High"), (False, "9 High")
        """

        # TODO:
        #  Order cards: lowest to highest
        #  determine what qualifies to be considered a straight
        #  when qualifying -> determine the straight.

        print(self.poker_hand)
        # is_flush, suit = self.is_flush()
        # if not is_flush:
        #     return False, suit
        #
        # is_straight, high_card = self.is_straight()
        # if is_straight:
        #     return True, high_card
        # else:
        #     return False, high_card
        return True, "9 High"

    def is_flush(self) -> tuple:
        """
        To be considered a flush, the following must be True:
            - All cards are from the same suit.

        Returns:
            A tuple. E.g. (True, "Hearts"), (False, "Not suited")
        """
        if self.all_hearts < self.total_hand_value < self.all_diamonds:
            return True, "Hearts"
        elif self.all_diamonds < self.total_hand_value < self.all_clubs:
            return True, "Diamonds"
        elif self.all_clubs < self.total_hand_value < self.all_spades:
            return True, "Clubs"
        elif self.all_spades < self.total_hand_value:
            return True, "Spades"
        else:
            return False, "Not Suited"

    def get_ranking(self) -> str:
        """
        Determines the poker hand ranking based on the poker hand.

        Returns:
             A string representing the poker hand ranking.
        """
        is_royal_flush, suit = self.is_royal_flush()
        if is_royal_flush:
            return f"Royal Flush ({suit})"

        return "POKER RANKING IN PROGRESS"
