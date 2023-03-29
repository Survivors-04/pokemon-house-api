import random
import jwt
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response, Request, status, APIView
from pokemons.models import PokemonBooster, PokemonUser, Pokemons
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view


from pokemons.serializers import PokemonBoosterSerializer, PokemonSerializer, PokemonUserSerializer
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


class PokemonBoosterListCreateAPIView(ListCreateAPIView):
    queryset = PokemonBooster.objects.all()
    serializer_class = PokemonBoosterSerializer


def get_booster(request, booster_id):
    booster = get_object_or_404(PokemonBooster, pk=booster_id)

    # normalizar as probabilidades para que a soma seja igual a 1
    total_probability = (
        booster.common_probability + booster.rare_probability + booster.epic_probability + booster.legendary_probability
    )
    common_probability = Decimal(booster.common_probability) / Decimal(total_probability)
    rare_probability = Decimal(booster.rare_probability) / Decimal(total_probability)
    epic_probability = Decimal(booster.epic_probability) / Decimal(total_probability)
    legendary_probability = Decimal(booster.legendary_probability) / Decimal(total_probability)

    pokemons = []
    for i in range(6):
        # gerar um número aleatório entre 0 e 1
        random_number = random.random()

        # escolher a raridade do pokemon baseado no número aleatório gerado
        if random_number < common_probability:
            rarity = "C"
        elif random_number < common_probability + rare_probability:
            rarity = "R"
        elif random_number < common_probability + rare_probability + epic_probability:
            rarity = "E"
        else:
            rarity = "L"

        # escolher um pokemon aleatório da raridade escolhida
        pokemon = get_random_pokemon(rarity)

        pokemons.append(
            {
                "name": pokemon.name,
                "rarity": pokemon.rarity,
                "pokedex": pokemon.pokedex,
                "type_1": pokemon.type_1,
                "type_2": pokemon.type_2,
            }
        )

    return JsonResponse(pokemons, safe=False)


def get_random_pokemon(rarity):
    count = Pokemons.objects.filter(rarity=rarity).count()
    if count == 0:
        return f"No {rarity} Pokemons available"

    pokemon = Pokemons.objects.filter(rarity=rarity).order_by("?").first()
    return pokemon


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
