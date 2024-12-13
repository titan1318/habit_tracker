from django.test import TestCase
from django.utils.timezone import now
from .models import Habit
from .tasks import send_habit_reminders


class HabitTasksTests(TestCase):
    def setUp(self):
        self.habit = Habit.objects.create(
            owner=None,
            action="Drink water",
            start_time=now(),
            is_published=True
        )

    def test_send_habit_reminders(self):
        send_habit_reminders()
        self.assertTrue(True)
