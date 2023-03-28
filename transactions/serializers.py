from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields ="__all__"
        read_only_fields = [
            "id",
            "seller_id",
        ]
    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)
    