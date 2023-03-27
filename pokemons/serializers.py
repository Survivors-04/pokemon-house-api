from pyexpat import model
from rest_framework.serializers import ModelSerializer, HiddenField, CurrentUserDefault
from pokemons.models import PokemonBooster, PokemonUser, Pokemons


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemons

        fields = "__all__"


class PokemonBoosterSerializer(ModelSerializer):
    class Meta:
        model = PokemonBooster
        fields = "__all__"


class PokemonUserSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = PokemonUser
        fields = "__all__"
