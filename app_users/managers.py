from django.contrib.auth.models import (
    BaseUserManager,
)
from .send_sms import send_activation_sms


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        if not email:
            return ValueError("Email должен быть обьзателльно передан")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **kwargs)
        user.create_activation_code()
        phone_number = kwargs.get("phone_number")
        if phone_number:
            user.create_phone_number_code()
        else:
            user.create_activation_code()
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

    def create_client(self, phone_number, password, **kwargs):
        user = self.model(phone_number=phone_number, **kwargs)
        user.create_activation_code()
        user.create_phone_number_code()
        user.set_password(password)
        user.save()

        # Отправка SMS-подтверждения
        send_activation_sms(phone_number, user.phone_number_code)
        return user
