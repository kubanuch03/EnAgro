from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.core.validators import RegexValidator
from django.utils.crypto import get_random_string

from .managers import UserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True, blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=25, unique=True, null=True)
    activation_code = models.CharField(max_length=255, blank=True)
    is_verified = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to="avatar/%Y/%m/%d/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    token_auth = models.CharField(max_length=64, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    hone_number_code = models.CharField(max_length=6, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f"{self.username}"

    def create_activation_code(self):
        import uuid

        code = str(uuid.uuid4())
        self.activation_code = code

    def create_phone_number_code(self):
        code = get_random_string(6, allowed_chars="123456789")
        self.phone_number_code = code
        return code
