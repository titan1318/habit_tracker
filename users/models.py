from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
        help_text="Введите ваш email",
    )

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Введите ваше имя",
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Введите вашу фамилию",
        blank=True,
        null=True,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
