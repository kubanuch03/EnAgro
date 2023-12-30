from django.db import models
from app_clients.models import Client

# from app_products.models import Product


class Complaint(models.Model):
    COMPLAINT_CHOICES = [
        ("Запрещенный товар", "Запрещенный товар"),
        ("Спам", "Спам"),
        ("Дубликат", "Дубликат"),
        ("Неверная категория", "Неверная категория"),
        ("Мошенничество", "Мошенничество"),
        ("Другая причина", "Другая причина"),
    ]
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="complaint")
    status = models.CharField(max_length=20, choices=COMPLAINT_CHOICES, default="Спам")
    # product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='complaints', null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{str(self.user)}"

    class Meta:
        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["-created_at"]),
        ]
