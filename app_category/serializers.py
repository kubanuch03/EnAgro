from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'img')
        read_only_fields = ('id', 'slug')  # Поля, которые можно только читать

