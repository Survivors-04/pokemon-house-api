from rest_framework.serializers import ModelSerializer
from pokemons.models import Pokemons


class PokemonSerializer(ModelSerializer):
    class Meta:
        model = Pokemons

        fields = "__all__"

    
