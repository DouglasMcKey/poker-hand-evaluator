class PokerHandInterface():
    """
    This class is responsible for evaluating a five card poker hand and produce
    a poker hand ranking.
    """
    def __init__(self, poker_hand: list[dict]):
        """
        Args:
            poker_hand: list of five cards, each card must have the following key, value pairs:
                {
                    "value": 114,
                    "face_value": 14,
                    "display": "Ace",
                    "suit": "Hearts"
                },
        """
        self.cards = poker_hand

        # Suit ranges.
        self.all_hearts = 500
        self.all_diamonds = 1000
        self.all_clubs = 1500
        self.all_spades = 2000

        # Processing variables.
        self.high_card = None  # Will hold the highest card "display" value.
        self.low_card = None  # Will hold the lowest card `face_value`
        self.hand_suit = None  # Will hold the suit name, when applicable. e.g. "Hearts".
        self.card_face_values = None  # Will hold a list of card face values.

    def is_valid(self):
        """
        Currently, the integration with our own Angular front-end, is designed
        in such a manner that only valid poker hands are received. So by default,
        we expect this function to return True.
        TODO: Besides hand size, this method can be extended with additional
              validation, like ensuring cards are unique to one deck.

        Returns:
             True if valid, False otherwise.
        """
        # Simple validation on hand size.
        if len(self.cards) != 5:
            return False

        return True

    def sort_hand(self):
        """
        Sorts the poker hand in ascending order.

        Returns:
            list of the sorted poker hand.
        """
        self.cards.sort(key=lambda slot: slot["face_value"])

    def set_high_and_low_cards(self):
        """
        Sets the high card and low card face value.
        """
        self.sort_hand()
        self.high_card = self.cards[-1]
        self.low_card = self.cards[0]

    def set_card_face_values(self):
        """
        Sets the `card_face_values` variable to a list of the poker hand card face values.
        """
        self.sort_hand()
        self.card_face_values = [
            self.cards[0]["face_value"],
            self.cards[1]["face_value"],
            self.cards[2]["face_value"],
            self.cards[3]["face_value"],
            self.cards[4]["face_value"]
        ]

    def get_total_value(self) -> int:
        """
        Returns the total `value` of the poker hand. This value is important
        in determining a suited hand.

        Returns:
            int: The total `value` of the poker hand.
        """
        return sum(card["value"] for card in self.cards)

    def is_royal_flush(self) -> bool:
        """
        To be considered a royal flush, the following must be True:
            - All cards are from the same suit.
            - Hand must include the following high cards:
                10 (value: 10),
                Jack (value: 11),
                Queen (value: 12),
                King (value: 13),
                Ace (value: 14)

        Returns:
            True if the hand is a royal flush, False otherwise.
        """
        is_flush = self.is_flush()
        if not is_flush:
            return False

        high_card_values = sum((10, 11, 12, 13, 14))
        total_hand_value = self.get_total_value()
        if total_hand_value in [
            self.all_hearts + high_card_values,
            self.all_diamonds + high_card_values,
            self.all_clubs + high_card_values,
            self.all_spades + high_card_values
        ]:
            return True
        else:
            return False

    def is_straight_flush(self) -> bool:
        """
        To be considered a straight flush, the following must be True:
            - All cards are from the same suit.
            - Hand must be of the form `straight`

        Returns:
            True if the hand is a straight flush, False otherwise.
        """
        is_flush = self.is_flush()
        if not is_flush:
            return False

        is_straight = self.is_straight()
        if not is_straight:
            return False

        return True

    def is_four_of_a_kind(self) -> bool:
        """
        To be considered a four of a kind, the following must be True:
            - Four of the cards must be of the same face_value.

        Returns:
            True if hand is a four of a kind, False otherwise.
        """
        self.set_card_face_values()
        face_values_set = set(self.card_face_values)
        if len(face_values_set) > 2:
            return False

        for face_value in face_values_set:
            count = self.card_face_values.count(face_value)
            if count == 4:
                return True

        return False

    def is_full_house(self) -> bool:
        """
        To be considered a full house, the following must be True:
            - Three of the cards must be of the same face_value.
            - The remaining two cards must be of the same face_value.

        Returns:
            True if hand is a full house, False otherwise.
        """
        self.set_card_face_values()
        face_values_set = set(self.card_face_values)
        if len(face_values_set) > 2:
            return False
        else:
            has_3 = False
            has_2 = False
            for face_value in face_values_set:
                count = self.card_face_values.count(face_value)
                if count == 3:
                    has_3 = True
                elif count == 2:
                    has_2 = True

            if has_3 and has_2:
                return True

        return False

    def is_flush(self) -> bool:
        """
        To be considered a flush, the following must be True:
            - All cards are from the same suit.

        Returns:
            True if the hand is a flush, False otherwise.
        """
        total_hand_value = self.get_total_value()
        suit_range = 100

        if total_hand_value in range(self.all_hearts, self.all_hearts + suit_range):
            self.hand_suit = "Hearts"
            return True
        elif total_hand_value in range(self.all_diamonds, self.all_diamonds + suit_range):
            self.hand_suit = "Diamonds"
            return True
        elif total_hand_value in range(self.all_clubs, self.all_clubs + suit_range):
            self.hand_suit = "Clubs"
            return True
        elif total_hand_value > self.all_spades:
            self.hand_suit = "Spades"
            return True
        else:
            return False

    def is_straight(self) -> bool:
        """
        To be considered a straight, the following must be True:
            - All cards are in a sequential order.

        Returns:
            True if the hand is a straight, False otherwise.
        """
        self.sort_hand()
        self.set_high_and_low_cards()
        self.set_card_face_values()

        # You can not have a straight if the lowest card is greater than 10.
        if self.low_card["face_value"] > 10:
            return False

        if self.low_card["face_value"] != 2:
            sequential_face_values = list(range(
                min(self.card_face_values),
                max(self.card_face_values) + 1
            ))
            return self.card_face_values == sequential_face_values

        elif self.low_card["face_value"] == 2 and self.high_card["face_value"] == 14:
            # Remove the last item (It is an ace).
            self.card_face_values.pop(-1)
            sequential_face_values = list(range(
                min(self.card_face_values),
                max(self.card_face_values) + 1
            ))

            result = self.card_face_values == sequential_face_values
            if result:
                self.high_card = self.cards[-2]
                return result

        return False

    def get_ranking(self) -> str:
        """
        Determines the poker hand ranking based on the five card poker hand.

        Returns:
             A string representing the poker hand ranking.
        """
        if self.is_valid():
            is_royal_flush = self.is_royal_flush()
            if is_royal_flush:
                return f"Royal Flush ({self.hand_suit})"

            is_straight_flush = self.is_straight_flush()
            if is_straight_flush:
                return f"Straight Flush - {self.high_card['display']} High ({self.hand_suit})"

            is_four_of_a_kind = self.is_four_of_a_kind()
            if is_four_of_a_kind:
                # TODO: Include the card display that made the 4 of a kind.
                return f"Four of a Kind"

            is_full_house = self.is_full_house()
            if is_full_house:
                # TODO: Include the card display that made up the full house.
                return f"Full House"

            is_flush = self.is_flush()
            if is_flush:
                return f"Flush - {self.high_card['display']} High ({self.hand_suit})"

            is_straight = self.is_straight()
            if is_straight:
                return f"Straight - {self.high_card['display']} High"

            # TODO: is_three_of_a_kind
            # TODO: is_two_pair
            # TODO: is_one_pair
            # TODO: else return high_card
            return "This hand rank is not developed yet."

        return "Invalid Poker Hand."
