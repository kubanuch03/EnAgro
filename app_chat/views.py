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

    # def perform_create(self, serializer):
    #     participants = self.request.data.getlist('participants', [])
    #
    #     if len(participants) < 2:
    #         return Response({'error': 'Для чата необходимо как минимум два участника.'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     try:
    #         chat = serializer.save()
    #
    #         user = self.request.user
    #
    #         chat.participants.set(participants)
    #
    #         chat.owner = user
    #         chat.save()
    #
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class MessageCreateView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        message = serializer.save()
        user_email = message.sender.email
        notification.delay(user_email)
        return Response({'message': 'Новые Уведомления'}, status=201)

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
