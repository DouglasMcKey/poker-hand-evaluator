import json

from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def evaluate_poker_hand(request: HttpRequest) -> JsonResponse:
    """
    Evaluates a poker hand.
    Args:
         request: HttpRequest object.

    Returns:
         JsonResponse
    """
    # Default response detail.
    status_code = HttpResponseBadRequest().status_code
    response = {
        "status": "error",
        "message": "Bad Request"
    }

    if request.method == "POST":
        received_cards = json.loads(request.body).get("cards")
        print("received_cards:\n", received_cards)
        evaluated_poker_hand = "We are in business."  # evaluate_poker_hand(request)

        # Update the JsonResponse detail.
        response.update({
            "status": "success",
            "message": evaluated_poker_hand
        })
        status_code = HttpResponse().status_code

    return JsonResponse(response, safe=False, status=status_code)
