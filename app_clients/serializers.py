from decouple import config

from django.contrib.auth.hashers import make_password
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_decode

from rest_framework import serializers

from app_users.send_sms import send_activation_sms
from .models import Client
from django.contrib.auth import get_user_model


User = get_user_model()

from djoser.serializers import serializers


class ConfirmEmailSerializer(serializers.Serializer):
    token = serializers.CharField()


class ClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(write_only=False, required=False)
    full_name = serializers.CharField(required=True)

    class Meta:
        model = Client
        fields = (
            "id",
            "email",
            "username",
            "full_name",
            "phone_number",
            "password",
            "password2",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Пароль не совпадает, попробуйте еще раз"}
            )
        return attrs

    def create(self, validated_data):
        client = Client.objects.create_client(
            email=validated_data["email"],
            username=validated_data.get("username", ""),
            phone_number=validated_data.get("phone_number", ""),
            full_name=validated_data.get("full_name", ""),
            password=validated_data["password"],
            token_auth=get_random_string(64),
        )

        current_site = get_current_site(self.context["request"])
        domain = current_site.domain
        protocol = "https" if self.context["request"].is_secure() else "http"
        confirmation_link = reverse(
            "clients:confirm_email", kwargs={"token": client.token_auth}
        )

        subject = "Подтверждение почты"
        message = (
            f"Подтвердите почту по ссылке: \n\n{protocol}://{domain}{confirmation_link}"
        )
        from_email = config("EMAIL_HOST_USER")
        to_email = validated_data["email"]
        send_mail(subject, message, from_email, [to_email], fail_silently=False)
        make_password(validated_data["password"])

        return client

    # def create_by_phone(self, validated_data):
    #     user = Client.objects.create_user(**validated_data)
    #     send_activation_sms(user.phone_number, user.activation_code)
    #     return user

    # def create_by_phone(self, validated_data):
    #     user = Client.objects.create_user(**validated_data)
    #     send_activation_sms(user.phone_number, user.activation_code)
    #     return user


class LoginClientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Client
        fields = ("email", "password")


class ResetPasswordConfirmSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, data):
        uidb64 = self.context.get("uidb64")
        token = self.context.get("token")

        if not uidb64 or not token:
            raise serializers.ValidationError(
                {
                    "error": "Отсутствуют необходимые параметры в ссылке для сброса пароля"
                }
            )

        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Client, pk=uid)

        if not default_token_generator.check_token(user, token):
            raise serializers.ValidationError(
                {"error": "Недействительная ссылка для сброса пароля"}
            )

        password = data.get("password")
        password2 = data.get("password2")

        if password != password2:
            raise serializers.ValidationError({"error": "Пароли не совпадают"})

        return data

    def save(self):
        uidb64 = self.context.get("uidb64")
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(Client, pk=uid)

        password = self.validated_data["password"]
        user.set_password(password)
        user.save()


class ClientProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "username", "email", "full_name", "avatar")


class RegisterPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = (
            "id",
            "email",
            "username",
            "full_name",
            "phone_number",
            "password",
            "password2",
        )

    def create(self, validated_data):
        user = Client.objects.create_user(**validated_data)
        send_activation_sms(user.phone_number, user.activation_code)
        return user

    def save(self, **kwargs):
        user = super().save(**kwargs)
        return user


class ActivationSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)

    def validate(self, attrs):
        self.code = attrs["code"]
        return attrs

    def save(self, **kwargs):
        try:
            user = User.objects.get(activation_code=self.code)
            user.is_active = True
            user.activation_code = ""
            user.save()
        except:
            self.fail("неверный код")
        fields = ("id", "username", "email", "full_name", "avatar")


class ConfirmEmailSerializer(serializers.Serializer):
    key = serializers.CharField()


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
