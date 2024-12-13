from django.db import models
from django.core.exceptions import ValidationError
from users.models import User


class Habit(models.Model):
    RHYTHM_CHOICES = [
        ("every day", "каждый день"),
        ("every other day", "через день"),
        ("every three days", "раз в 3 дня"),
        ("every four days", "раз в 4 дня"),
        ("every five days", "раз в 5 дней"),
        ("every six days", "раз в 6 дней"),
        ("every week", "раз в неделю")
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Владелец",
    )
    place = models.CharField(
        max_length=100,
        verbose_name="Место выполнения привычки",
        help_text="Укажите место выполнения привычки",
        blank=True,
        null=True,
    )
    start_time = models.DateTimeField(
        verbose_name="Время начала выполнения привычки",
        help_text="Выберите дату и время начала привычки",
        blank=True,
        null=True,
    )
    action = models.CharField(
        max_length=300,
        verbose_name="Действие привычки",
        help_text="Опишите действие вашей привычки",
    )
    is_pleasant = models.BooleanField(
        default=False,
        verbose_name="Признак приятной привычки",
        help_text="Привычка является приятной",
    )
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        help_text="Выберите связанную приятную привычку",
        blank=True,
        null=True,
    )
    rhythm = models.CharField(
        max_length=16,
        choices=RHYTHM_CHOICES,
        verbose_name="Периодичность выполнения",
        help_text="Выберите периодичность выполнения привычки",
        default="every day",
    )
    reward = models.CharField(
        max_length=300,
        verbose_name="Вознаграждение",
        help_text="Укажите вознаграждение",
        blank=True,
        null=True,
    )
    lead_time = models.IntegerField(
        default=1,
        verbose_name="Время выполнения",
        help_text="Укажите предположительное время выполнения привычки в минутах",
    )
    is_published = models.BooleanField(
        default=False,
        verbose_name="Общий доступ",
        help_text="Опубликовать для общего доступа",
    )

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError("Нельзя одновременно указать вознаграждение и связанную привычку.")

        if self.lead_time > 2:
            raise ValidationError("Время выполнения привычки не должно превышать 120 секунд.")

        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной.")

        if self.is_pleasant and (self.reward or self.related_habit):
            raise ValidationError("Приятная привычка не может иметь вознаграждение или связанную привычку.")

    def __str__(self):
        return self.action
