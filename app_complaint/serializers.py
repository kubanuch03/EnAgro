from rest_framework import serializers
from .models import Complaint
from app_products.serializers import ProductSerializer


class ComplaintSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=False, allow_null=True)

    class Meta:
        model = Complaint
        fields = "__all__"
