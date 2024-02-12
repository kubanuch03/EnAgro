from rest_framework import serializers
from app_users.models import CustomUser
from .models import Chat, Message



class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["id", "participants", "owner"]



class ChatSerializer(serializers.ModelSerializer):
    owner_username = serializers.SerializerMethodField()
    participants_username = serializers.SerializerMethodField()

    def get_owner_username(self, obj):
        return obj.owner.username if obj.owner else None

    def get_participants_username(self, obj):
        return obj.participants.username if obj.participants else None

    class Meta:
        model = Chat
        fields = ["id", "participants", "owner", "participants_username", "owner_username"]



class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "sender", "chat", "recipient", "message"]



class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["id", "sender", "chat", "recipient", "message"]

