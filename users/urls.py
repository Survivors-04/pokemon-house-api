from . import views
from django.urls import path


urlpatterns = [
    path("", views.UserListCreateView.as_view()),
    path("<uuid:pk>/", views.UserDetailView.as_view()),
    path("<uuid:user_id>/pokemons", views.UserPokemonsView.as_view()),
]
