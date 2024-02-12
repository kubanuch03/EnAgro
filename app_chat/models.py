from django.db import models
from app_users.models import CustomUser
from app_clients.models import Client


class Chat(models.Model):
    participants = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="chats")
    owner = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="owned_chat")

    def __str__(self):
        return f"Chat {self.id}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name="messages")
    recipient = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="received_messages")
    sender = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="sent_messages")
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient} - {self.timestamp}\n{self.sender} - {self.timestamp}"
