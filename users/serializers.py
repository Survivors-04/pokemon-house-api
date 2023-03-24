from rest_framework.serializers import ModelSerializer
from pokemons import serializers

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User

        fields = "__all__"
        read_only_fields = ["id", "is_superuser"]
