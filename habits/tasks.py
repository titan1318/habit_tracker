from celery import shared_task
from django.utils.timezone import now
from .models import Habit

@shared_task
def send_habit_reminders():
    habits = Habit.objects.filter(start_time__lte=now(), is_published=True)
    for habit in habits:
        print(f"Напоминание для привычки: {habit.action}")
