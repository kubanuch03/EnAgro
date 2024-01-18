from rest_framework import serializers
from app_products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "id",
            "category",
            "podcategory",
            "title",
            "description",
            "price",
            "location",
            "rating",

        )
        read_only_fields = (
            "id",
            "slug",
            "user",
            "created",
            "updated",
            "rating",
        )  # Поля, которые можно только читать

