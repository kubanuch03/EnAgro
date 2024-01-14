from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "podcategory",
            "name",
            "image",
            "description",
            "price",
        )
        read_only_fields = (
            "id",
            "slug",
            "user",
            "created",
            "updated",
        )  # Поля, которые можно только читать
