def create_hand_royal_flush() -> tuple:
    """
    Creates and returns a five card poker hand.

    Returns:
         list[dict]
    """
    return [
        {"id": 13, "value": 114, "face_value": 14, "display": "Ace", "suit": "Hearts"},
        {"id": 12, "value": 113, "face_value": 13, "display": "King", "suit": "Hearts"},
        {"id": 11, "value": 112, "face_value": 12, "display": "Queen", "suit": "Hearts"},
        {"id": 10, "value": 111, "face_value": 11, "display": "Jack", "suit": "Hearts"},
        {"id": 9, "value": 110, "face_value": 10, "display": 10, "suit": "Hearts"}
    ], "Hearts"
