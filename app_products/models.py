from datetime import datetime

from django.db import models
from app_clients.models import Client

from app_category.models import Category, PodCategory
from .manager import ConfirmedCommentManager



class Product(models.Model):
    RATING = (
        (1, '⭐️'),
        (2, '⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️'),
        (5, '⭐️⭐️⭐️⭐️⭐️'),
    )
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    podcategory = models.ForeignKey(PodCategory, related_name="pod_products", on_delete=models.CASCADE)
    user = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    image1 = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True, null=True)
    image2 = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True, null=True)
    image3 = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True, null=True)
    image4 = models.ImageField(upload_to="products/%Y/%m/%d/", blank=True, null=True)

    description = models.TextField()
    price = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    location = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.IntegerField(choices=RATING)

    class Meta: 
        ordering = ["title"]

        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["title"]),
            models.Index(fields=["-created"]),
        ]
        ordering = ["title"]

        indexes = [
            models.Index(fields=["id"]),
            models.Index(fields=["title"]),
            models.Index(fields=["-created"]),
        ]

    def __str__(self):
        return self.title
    
