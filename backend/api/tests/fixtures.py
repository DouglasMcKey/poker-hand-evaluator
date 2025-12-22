def sorted_hand_royal_flush() -> list[dict]:
    """
    Returns a sorted five card poker hand, royal flush.

    Returns:
         list[dict]
    """
    return [
        {"id": 9, "value": 110, "face_value": 10, "display": 10, "suit": "Hearts"},
        {"id": 10, "value": 111, "face_value": 11, "display": "Jack", "suit": "Hearts"},
        {"id": 11, "value": 112, "face_value": 12, "display": "Queen", "suit": "Hearts"},
        {"id": 12, "value": 113, "face_value": 13, "display": "King", "suit": "Hearts"},
        {"id": 13, "value": 114, "face_value": 14, "display": "Ace", "suit": "Hearts"}
    ]


def create_hand_royal_flush() -> list[dict]:
    """
    Returns a five card poker hand, royal flush.

    Returns:
         list[dict]
    """
    return [
        {"id": 13, "value": 114, "face_value": 14, "display": "Ace", "suit": "Hearts"},
        {"id": 12, "value": 113, "face_value": 13, "display": "King", "suit": "Hearts"},
        {"id": 11, "value": 112, "face_value": 12, "display": "Queen", "suit": "Hearts"},
        {"id": 10, "value": 111, "face_value": 11, "display": "Jack", "suit": "Hearts"},
        {"id": 9, "value": 110, "face_value": 10, "display": 10, "suit": "Hearts"}
    ]


def create_hand_straight_flush() -> list[dict]:
    """
    Returns a five card poker hand, straight flush.

    Returns:
         list[dict]
    """
    return [
        {'id': 17, 'value': 205, 'face_value': 5, 'display': 5, 'suit': 'Diamonds'},
        {'id': 18, 'value': 206, 'face_value': 6, 'display': 6, 'suit': 'Diamonds'},
        {'id': 19, 'value': 207, 'face_value': 7, 'display': 7, 'suit': 'Diamonds'},
        {'id': 16, 'value': 204, 'face_value': 4, 'display': 4, 'suit': 'Diamonds'},
        {'id': 15, 'value': 203, 'face_value': 3, 'display': 3, 'suit': 'Diamonds'}
    ]


def create_hand_flush() -> list[dict]:
    """
    Returns a five card poker hand, flush.

    Returns:
         list[dict]
    """
    return [
        {'id': 43, 'value': 405, 'face_value': 5, 'display': 5, 'suit': 'Spades'},
        {'id': 48, 'value': 410, 'face_value': 10, 'display': 10, 'suit': 'Spades'},
        {'id': 52, 'value': 414, 'face_value': 14, 'display': 'Ace', 'suit': 'Spades'},
        {'id': 44, 'value': 406, 'face_value': 6, 'display': 6, 'suit': 'Spades'},
        {'id': 47, 'value': 409, 'face_value': 9, 'display': 9, 'suit': 'Spades'}
    ]


def create_hand_four_of_a_kind() -> list[dict]:
    """
    Returns a five card poker hand, four of a kind.

    Returns:
         list[dict]
    """
    return [
        {'id': 4, 'value': 105, 'face_value': 5, 'display': 5, 'suit': 'Hearts'},
        {'id': 17, 'value': 205, 'face_value': 5, 'display': 5, 'suit': 'Diamonds'},
        {'id': 52, 'value': 414, 'face_value': 14, 'display': 'Ace', 'suit': 'Spades'},
        {'id': 30, 'value': 305, 'face_value': 5, 'display': 5, 'suit': 'Clubs'},
        {'id': 43, 'value': 405, 'face_value': 5, 'display': 5, 'suit': 'Spades'}
    ]


def create_hand_full_house() -> list[dict]:
    """
    Returns a five card poker hand, full house.

    Returns:
         list[dict]
    """
    return [
        {'id': 9, 'value': 110, 'face_value': 10, 'display': 10, 'suit': 'Hearts'},
        {'id': 22, 'value': 210, 'face_value': 10, 'display': 10, 'suit': 'Diamonds'},
        {'id': 24, 'value': 212, 'face_value': 12, 'display': 'Queen', 'suit': 'Diamonds'},
        {'id': 50, 'value': 412, 'face_value': 12, 'display': 'Queen', 'suit': 'Spades'},
        {'id': 48, 'value': 410, 'face_value': 10, 'display': 10, 'suit': 'Spades'}
    ]


def create_hand_straight() -> list[dict]:
    """
    Returns a five card poker hand, straight.

    Returns:
         list[dict]
    """
    return [
        {'id': 6, 'value': 107, 'face_value': 7, 'display': 7, 'suit': 'Hearts'},
        {'id': 33, 'value': 308, 'face_value': 8, 'display': 8, 'suit': 'Clubs'},
        {'id': 47, 'value': 409, 'face_value': 9, 'display': 9, 'suit': 'Spades'},
        {'id': 9, 'value': 110, 'face_value': 10, 'display': 10, 'suit': 'Hearts'},
        {'id': 23, 'value': 211, 'face_value': 11, 'display': 'Jack', 'suit': 'Diamonds'}
    ]
