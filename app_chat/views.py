from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import serializers
from .task import notification
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer, ChatCreateSerializer
from rest_framework.permissions import IsAuthenticated


class ChatListView(ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsAuthenticated, ]


class ChatCreateView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatCreateSerializer
    permission_classes = [IsAuthenticated, ]


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, ]

    def perform_create(self, serializer):
        message = serializer.save()
        user_email = message.recipient.email
        notification.delay(user_email)
        return Response({"message": "Новые Уведомления"}, status=201)

    # def perform_create(self, serializer):
    #     chat_id = self.kwargs.get('chat_id')
    #     chat = get_object_or_404(Chat, id=chat_id)
    #     sender_id = self.request.data.get('sender_id')
    #     content = self.request.data.get('content')
    #
    #     if not sender_id or not content:
    #         return Response({'error : Для отправки сообщения необходимы идентификатор отправителя и контент.'},
    #                         status=status.HTTP_400_BAD_REQUEST)
    #
    #     sender = get_object_or_404(CustomUser, id=sender_id)
    #
    #     message = serializer.save(chat=chat, sender=sender, content=content)
    #     return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)


class MessageListView(ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated, ]
