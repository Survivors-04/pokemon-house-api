from rest_framework.serializers import ModelSerializer
from pokemons.models import  PokemonUser, Pokemons


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemons

        fields = "__all__"


class PokemonUserSerializer(ModelSerializer):
    class Meta:
        model = PokemonUser

        fields = "__all__"

        read_only_fields = ["user"]
