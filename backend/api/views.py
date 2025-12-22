import json

from django.contrib.auth.decorators import login_not_required
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponse
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt

from api.interface import PokerHandInterface


@login_not_required
def index(
    request: HttpRequest,
    template_name: str = "index.html"
) -> TemplateResponse:
    """
    This is the index page of the backend.
    """
    return TemplateResponse(request, template_name)


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

        poker_hand = PokerHandInterface(received_cards)
        if not poker_hand.is_valid():
            response.update({
                "status": "error",
                "message": "Invalid poker hand"
            })

        else:
            result = poker_hand.get_ranking()
            response.update({
                "status": "success",
                "message": result
            })
            status_code = HttpResponse().status_code

    return JsonResponse(response, safe=False, status=status_code)
