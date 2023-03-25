from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from .views import UserListCreateView, UserDetailView, UserPokemonsView


urlpatterns = [
    path("", UserListCreateView.as_view()),
    path("<uuid:pk>/", UserDetailView.as_view()),
    path("<uuid:user_id>/pokemons", UserPokemonsView.as_view()),
    path("login", jwt_views.TokenObtainPairView.as_view()),
]
