from django.contrib import admin
from django.urls import path
from .views import ChatCreateView, ChatListView, MessageCreateView, MessageListView, MessageDetailView, ChatDetailView, MessageByChat



urlpatterns = [
    path("create/chat/", ChatCreateView.as_view(), name="create_chat"),
    path("list/chat/", ChatListView.as_view(), name="list_chat"),
    path('detail/chat/<int:id>/', ChatDetailView.as_view(), name='detail_chat'),
    path("create/message/", MessageCreateView.as_view(), name="create_message"),
    path("list/message/", MessageListView.as_view(), name="List_message"),
    path('detail/message/<int:id>/', MessageDetailView.as_view(), name='detail_message'),
    path("message/by/chat/<int:chat_id>/", MessageByChat.as_view(),name='MessageByChat')
]
