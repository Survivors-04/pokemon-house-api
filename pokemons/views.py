from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response, status, APIView
from pokemons.models import PokemonUser, Pokemons
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view


from pokemons.serializers import PokemonSerializer, PokemonUserSerializer
from users.models import User


class PokemonListCreateView(ListCreateAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemons.objects.all()

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)

        if is_many:
            serializer = PokemonSerializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = PokemonSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PokemonDetailView(RetrieveAPIView):
    serializer_class = PokemonSerializer
    queryset = Pokemons.objects.all()


class PokemonUserListCreateView(APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        pokemons = PokemonUser.objects.filter(user=user)

        serializer = PokemonUserSerializer(pokemons, many=True)

        return Response(serializer.data)

    def post(self, request, user_id):
        user = get_object_or_404(User, id=user_id)

        is_many = isinstance(request.data, list)

        if is_many:
            serializer = PokemonUserSerializer(data=request.data, many=True)

            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        serializer = PokemonUserSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user=user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PokemonUserDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = PokemonUserSerializer
    queryset = PokemonUser.objects.all()


@api_view(["GET"])
def pokemon_users_on_marketplace(request):
    pokemon_users = PokemonUser.objects.filter(on_marketplace=True)

    serializer = PokemonUserSerializer(pokemon_users, many=True)

    return Response(serializer.data)


class MarketplaceUpdateDestroy(APIView):
    def put(self, request, pokemon_id):
        pokemon_user = PokemonUser.objects.get(id=pokemon_id)

        pokemon_user.on_marketplace = True
        pokemon_user.save()

        serializer = PokemonUserSerializer(pokemon_user)

        return Response(serializer.data)

    def delete(self, request, pokemon_id):
        pokemon_user = PokemonUser.objects.get(id=pokemon_id)

        pokemon_user.on_marketplace = False
        pokemon_user.save()

        serializer = PokemonUserSerializer(pokemon_user)

        return Response(serializer.data)
