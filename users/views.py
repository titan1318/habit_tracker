from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import RegisterUserSerializer, UserSerializer
from .models import User


class RegisterUserView(generics.CreateAPIView):
    """Регистрация нового пользователя"""
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer
    permission_classes = [AllowAny]


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)  # Хеширование пароля
        user.save()


class CustomTokenObtainPairView(TokenObtainPairView):
    """Получение JWT токена"""
    permission_classes = [AllowAny]


class CustomTokenRefreshView(TokenRefreshView):
    """Обновление JWT токена"""
    permission_classes = [AllowAny]
