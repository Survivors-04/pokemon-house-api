from .views import PokemonListCreateView, PokemonDetailView, PokemonBoosterListCreateAPIView, get_booster
from django.urls import path


urlpatterns = [
    path("", PokemonListCreateView.as_view()),
    path("<uuid:pk>/", PokemonDetailView.as_view()),
    path("boosters/", PokemonBoosterListCreateAPIView.as_view()),
    path("boosters/<uuid:booster_id>/", get_booster),
]
