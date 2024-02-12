from rest_framework import generics, permissions, viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny

from django.contrib.auth import login, authenticate

from app_users.send_email import send_confirmation_email
from .models import Client
from .permissions import IsClientOrAdmin
from .serializers import (
    ClientSerializer,
    LoginClientSerializer,
    ResetPasswordConfirmSerializer,
    ClientProfileSerializer,
    ClientSerializer,
    RegisterPhoneSerializer,
    ConfirmEmailSerializer,
    PasswordResetSerializer
)
from rest_framework.generics import CreateAPIView, GenericAPIView
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


class RequestPasswordResetView(APIView):
    serializer_class = PasswordResetSerializer
    permission_classes = [AllowAny, ]

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        try:
            user = Client.objects.get(email=email)
        except Client.DoesNotExist:
            return Response(
                {"error": "Пользователь с таким email не найден"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        uid = urlsafe_base64_encode(force_str(user.pk).encode())
        token = default_token_generator.make_token(user)

        reset_url = reverse(
            "clients:reset-password-confirm", kwargs={"uidb64": uid, "token": token}
        )
        reset_url = request.build_absolute_uri(reset_url)

        subject = "Восстановление пароля"
        message = f"Для восстановления пароля перейдите по ссылке: {reset_url}"

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

        return Response(
            {"success": "Ссылка для восстановления пароля отправлена на ваш email"}
        )


class ResetPasswordConfirmView(generics.GenericAPIView):
    serializer_class = ResetPasswordConfirmSerializer
    permission_classes = [AllowAny, ]


    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(
            data=request.data,
            context={"uidb64": kwargs["uidb64"], "token": kwargs["token"]},
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        try:
            serializer.save()
            return Response({"success": "Пароль успешно изменен"})
        except:
            return Response(
                {"error": "Недействительная ссылка для сброса пароля"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class RegisterClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny, ]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        client = serializer.save()

        return Response(
            {
                "detail": "Registration successful",
                "user_id": client.id,
                "email": client.email,
                "username": client.username,
                "phone_number": client.phone_number,
                "подтвердите регистрацию, отправили код на ваш email адрес":client.email,
            },
            status=status.HTTP_201_CREATED,
        )

    def email_code(self, request):
        serializer = RegisterPhoneSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        send_confirmation_email(user.email, user.activation_code)
        if user:
            print(user, "!!!!")
            try:
                send_confirmation_email(user.email, user.activation_code)
            except:
                return Response(
                    {
                        "message": "Зарегистрировался но на почту код не отправился",
                        "data": serializer.data,
                    },
                    status=201,
                )
        return Response(serializer.data, status=201)


class LoginClientView(generics.GenericAPIView):
    serializer_class = LoginClientSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        if email and password:
            client = authenticate(username=email, password=password)
            print(f"Client: {client}")

            if client:
                login(request, client)
                refresh = RefreshToken.for_user(client)
                return Response(
                    {
                        "user_id": client.id,
                        "email": client.email,
                        "username": client.username,
                        "refresh": str(refresh),
                        "access": str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "detail": "Authentication failed. User not found or credentials are incorrect."
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
        else:
            return Response(
                {"detail": "Invalid input. Both email and password are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        
    def get(self, request, token):
        try:
            user = Client.objects.get(activation_token=token)
            user.is_active = True
            user.save()
        except Client.DoesNotExist:
            raise ({"error": "invalid-token"})


class ConfirmEmailView(generics.GenericAPIView):
    serializer_class = ConfirmEmailSerializer

    @staticmethod
    def get(request, token):
        try:
            user = Client.objects.get(token_auth=token)
            if user.is_active:
                return Response(
                    {"detail": "User is already activated"}, status=status.HTTP_200_OK
                )

            user.is_active = True
            user.save()

            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    "detail": "Email confirmation successful",
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                },
                status=status.HTTP_200_OK,
            )
        except Client.DoesNotExist:
            return Response(
                {"detail": "Invalid token"}, status=status.HTTP_404_NOT_FOUND
            )


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser, ]


class ClientUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsClientOrAdmin, ]



class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [permissions.IsAdminUser, ]
    # lookup_field = "pk"


class ClientProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = ClientProfileSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_object(self):
        return self.request.user

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class RegistrationPhoneView(CreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = RegisterPhoneSerializer
#     # def post(self, request):
#     data = request.data
#     serializer = RegisterPhoneSerializer(data=data)
#     if serializer.is_valid(raise_exception=True):
#         serializer.save()
#         return Response('good', status=201)


# class ActivationPhoneView(GenericAPIView):
#     serializer_class = ActivationSerializer

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response('Аккаунт успешно активирован', status=200)
