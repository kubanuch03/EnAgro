from django.urls import path
from .views import SupportChatListView, SupportChatCreateView

app_name = "SupportChar"

urlpatterns = [
    path("create/support/chat/", SupportChatCreateView.as_view(), name='Create_support_chat'),
    path("list/support/chat/", SupportChatListView.as_view(), name='list_support_chat'),


]