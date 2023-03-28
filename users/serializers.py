from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from django.contrib.auth.hashers import make_password

from users.models import User


class UserSerializer(ModelSerializer):
    pokemons = PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data: dict) -> User:
        
        return User.objects.create_superuser(**validated_data)
        

    class Meta:
        model = User

        fields = "__all__"
        read_only_fields = ["id", "is_superuser"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        password = validated_data.get("password")
        user = User(**validated_data)

        if password is not None:
            user.set_password(password)

        user.save()

        return user

    def update(self, instance, validated_data):
        password = validated_data.get("password")

        if password is not None:
            validated_data["password"] = make_password(password)

        return super().update(instance, validated_data)
