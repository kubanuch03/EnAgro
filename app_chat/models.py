from django.db import models
from app_clients.models import Client


class Chat(models.Model):
    participants = models.ManyToManyField(Client, related_name='chats')
    owner = models.OneToOneField(Client, on_delete=models.CASCADE, related_name='owned_chat', unique=True)

    def __str__(self):
        return f"Chat {self.id}"


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(Client, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} - {self.timestamp}'