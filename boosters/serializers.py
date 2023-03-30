from rest_framework.serializers import ModelSerializer
from boosters.models import Booster


class BoosterSerializer(ModelSerializer):
    class Meta:
        model = Booster
        fields = "__all__"
