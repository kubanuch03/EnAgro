from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    location = serializers.CharField(source='location', read_only=True)
    rating = serializers.DecimalField(max_digits=3, decimal_places=2, source='rating', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'category', 'podcategory', 'user', 'name', 'slug', 'image', 'description', 'price', 'location', 'rating', 'available', 'created', 'updated')
        read_only_fields = ('id', 'slug', 'user', 'created', 'updated')

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        include_location_rating = self.context.get('include_location_rating', False)
        if not include_location_rating:
            representation.pop('location', None)
            representation.pop('rating', None)

        return representation

