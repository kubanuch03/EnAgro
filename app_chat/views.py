from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import serializers
from .task import notification
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, ChatCreateSerializer


class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()
        user_email = message.recipient.email
        notification.delay(user_email)
        return Response({"message": "Новые Уведомления"}, status=201)


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
