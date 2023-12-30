
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'category', 'user', 'name', 'slug', 'image', 'description', 'price', 'available', 'created', 'updated')
        read_only_fields = ('id', 'slug', 'user', 'created', 'updated')  # Поля, которые можно только читать


