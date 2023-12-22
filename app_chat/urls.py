from django.contrib import admin
from django.urls import path
from .views import ChatCreateView, ChatListView, MessageCreateView, MessageListView

app_name = "chat"

urlpatterns = [
    path("create/chat/", ChatCreateView.as_view(), name="create_chat"),
    path("list/chat/", ChatListView.as_view(), name="list_chat"),
    path("create/message/", MessageCreateView.as_view(), name="create_message"),
    path("list/message/", MessageListView.as_view(), name="List_message"),
]