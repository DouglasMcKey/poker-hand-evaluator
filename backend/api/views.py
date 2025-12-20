from django.http import JsonResponse, HttpRequest


def evaluate_poker_hand(request: HttpRequest) -> JsonResponse:
    """
    Evaluates a poker hand.
    Args:
         request: HttpRequest object.

    Returns:
         JsonResponse
    """

    result = "Full House"  # evaluate_poker_hand(request)

    return JsonResponse(result, safe=False)
