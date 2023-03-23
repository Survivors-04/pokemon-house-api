from . import views
from django.urls import path


urlpatterns = [
    path("", views.PokemonListCreateView.as_view()),
    path("<str:pk>/", views.PokemonDetailView.as_view()),
]
