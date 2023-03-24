from django.shortcuts import get_object_or_404, render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from pokemons.models import Pokemons
from pokemons.serializers import PokemonSerializer
from users.models import User

from users.serializers import UserSerializer


class UserListCreateView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserPokemonsView(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        
        pokemons = Pokemons.objects.filter(user=user)
        
        serializer = PokemonSerializer(pokemons, many=True)
        
        return Response(serializer.data)
