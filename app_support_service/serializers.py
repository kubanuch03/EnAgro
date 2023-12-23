from rest_framework import serializers
from .models import SupportChat
from app_users.models import CustomUser
from app_clients.models import Client


# class ClientSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Client
#         fields = ['username']


# class CustomSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser
#         fields = ['username']


class SupportChatSerializers(serializers.ModelSerializer):
    # recipient = CustomSerializer(read_only=True)
    # sender = serializers.StringRelatedField()

    class Meta:
        model = SupportChat
        fields = ['sender', 'recipient', 'body']
