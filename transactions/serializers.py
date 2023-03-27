from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ["id, buyed_id", "seller_id"]
        read_only_fields = [
            "id",
            "seller",
        ]
    def create(self, validated_data):
        return Transaction.objects.create(**validated_data)
    