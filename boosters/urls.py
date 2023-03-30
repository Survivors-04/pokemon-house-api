from .views import BoosterListCreateAPIView, get_booster
from django.urls import path


urlpatterns = [
    path("boosters/", BoosterListCreateAPIView.as_view()),
    path("boosters/<uuid:booster_id>/", get_booster),
]
