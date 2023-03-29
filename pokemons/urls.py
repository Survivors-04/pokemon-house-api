from .views import (
    PokemonListCreateView,
    PokemonDetailView,
    PokemonBoosterListCreateAPIView,
    PokemonUserDetailView,
    get_booster,
    PokemonUserListCreateView,
    pokemon_users_on_marketplace,
    MarketplaceUpdateDestroy,
)
from django.urls import path


urlpatterns = [
    path("pokemons/", PokemonListCreateView.as_view()),
    path("pokemons/<uuid:pk>/", PokemonDetailView.as_view()),
    path("boosters/", PokemonBoosterListCreateAPIView.as_view()),
    path("boosters/<uuid:booster_id>/", get_booster),
    path("pokemons/users/<uuid:user_id>/", PokemonUserListCreateView.as_view()),
    path("pokemons/<uuid:pk>/users/", PokemonUserDetailView.as_view()),
    path("marketplace/", pokemon_users_on_marketplace),
    path("marketplace/pokemons/<uuid:pokemon_id>", MarketplaceUpdateDestroy.as_view())
]
