def create_hand_royal_flush() -> tuple:
    """
    Creates and returns a five card poker hand.

    Returns:
         list[dict]
    """
    return [
        {"id": 13, "value": 114, "face_value": "Ace", "suite": "Hearts"},
        {"id": 12, "value": 113, "face_value": "King", "suite": "Hearts"},
        {"id": 11, "value": 112, "face_value": "Queen", "suite": "Hearts"},
        {"id": 10, "value": 111, "face_value": "Jack", "suite": "Hearts"},
        {"id": 9, "value": 110, "face_value": 10, "suite": "Hearts"}
    ], "Hearts"
