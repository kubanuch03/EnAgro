from django.db import models
from app_users.models import CustomUser
from app_clients.models import Client


class SupportChat(models.Model):
    recipient = models.OneToOneField(
        CustomUser, related_name="received_chats", on_delete=models.PROTECT
    )
    sender = models.ForeignKey(
        Client, related_name="sent_chats", on_delete=models.CASCADE
    )
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
