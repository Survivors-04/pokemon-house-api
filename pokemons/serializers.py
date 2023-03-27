from rest_framework.serializers import ModelSerializer
from pokemons.models import PokemonBooster, Pokemons


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemons

        fields = "__all__"


class PokemonBoosterSerializer(ModelSerializer):
    class Meta:
        model = PokemonBooster
        fields = "__all__"
