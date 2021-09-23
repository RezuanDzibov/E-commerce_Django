from rest_framework import serializers, validators
from .models import Item


class ItemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="product.name")
    quantity = serializers.IntegerField(max_value=10, min_value=1)

    class Meta:
        model = Item
        fields = ("id", "name", "item_price", "total_price", "quantity")