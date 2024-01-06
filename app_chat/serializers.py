from rest_framework import serializers
from app_users.models import CustomUser
from .models import Chat, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ["chat", "sender", "content"]


class ChatSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = ["id", "participants", "messages"]


class CreateMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ChatCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ["participants", "owner"]
