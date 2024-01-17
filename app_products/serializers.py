from rest_framework import serializers
from app_products.models import Product, RatingProduct


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


class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = RatingProduct
        fields = '__all__'