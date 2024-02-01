from rest_framework import serializers
from app_products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    podcategory = serializers.SerializerMethodField()

    def get_category(self, obj):
        return obj.category.name if obj.category.name else None
    
    def get_podcategory(self, obj):
        return obj.podcategory.name if obj.podcategory.name else None

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
            "image1",
            "image2",
            "image3",
            "image4"

        )
        # read_only_fields = (
        #     "id",
        #     "slug",
        #     "user",
        #     "created",
        #     "updated",
        #     "rating",
        # )  # Поля, которые можно только читать

