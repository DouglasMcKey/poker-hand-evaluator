from django.urls import path

from api import views

urlpatterns = [
    path("evaluate-power-hand/", views.evaluate_poker_hand, name="evaluate_poker_hand")
]
