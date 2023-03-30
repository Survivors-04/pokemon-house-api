import random
from decimal import Decimal
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView
from boosters.models import Booster
from boosters.serializers import BoosterSerializer
from pokemons.models import Pokemons


class BoosterListCreateAPIView(ListCreateAPIView):
    queryset = Booster.objects.all()
    serializer_class = BoosterSerializer


def get_booster(request, booster_id):
    booster = get_object_or_404(Booster, pk=booster_id)

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
