from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .serializers import SupportChatSerializers
from .models import SupportChat
from rest_framework.generics import CreateAPIView, ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated


class SupportChatCreateView(CreateAPIView):
    queryset = SupportChat.objects.all()
    serializer_class = SupportChatSerializers
    permission_classes = [IsAuthenticated, ]


class SupportChatListView(ListAPIView):
    queryset = SupportChat.objects.all()
    serializer_class = SupportChatSerializers
    permission_classes = [IsAuthenticated, ]