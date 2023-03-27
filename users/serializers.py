from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from users.models import User


class UserSerializer(ModelSerializer):
    pokemons = PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data: dict) -> User:
        
        return User.objects.create_superuser(**validated_data)
        

    class Meta:
        model = User

        fields = "__all__"
        read_only_fields = ["id", "is_superuser"]
