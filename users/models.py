from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):

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

    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",
        blank=True,
        verbose_name="Группы",
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",
        blank=True,
        verbose_name="Права пользователя",
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
