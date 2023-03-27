from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField

from users.models import User


class UserSerializer(ModelSerializer):
    pokemons = PrimaryKeyRelatedField(many=True, read_only=True)

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
        instance.username = validated_data.get("username", instance.username)
        instance.gold = validated_data.get("gold", instance.gold)
        instance.dateRoll = validated_data.get("dateRoll", instance.dateRoll)
        password = validated_data.get("password", None)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
