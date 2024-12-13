from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com")
        self.habit = Habit.objects.create(
            owner=self.user,
            start_time="2024-12-05 07:00",
            action="Test",
            rhythm="every day",
        )
        self.public_habit = Habit.objects.create(
            owner=self.user,
            start_time="2024-12-05 07:00",
            action="Public Habit",
            rhythm="every day",
            is_published=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        data = {
            "start_time": "2024-12-06 10:00",
            "action": "Test",
            "rhythm": "every day",
        }
        response = self.client.post("/habits/", data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 3)

    def test_public_habit_list(self):
        """Тестирование списка публичных привычек"""
        response = self.client.get("/habits/public/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["action"], "Public Habit")

    def test_habit_access_unauthenticated(self):
        """Проверка доступа для неаутентифицированного пользователя"""
        self.client.logout()
        response = self.client.get(f"/habits/{self.habit.pk}/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_habit_create_with_related_habit_and_reward(self):
        related_habit = Habit.objects.create(
            owner=self.user,
            start_time="2024-12-05 07:00",
            action="related_habit",
            rhythm="every day",
            lead_time=1,
            is_pleasant=True,
        )
        data = {
            "start_time": "2024-12-06 10:00",
            "action": "Test",
            "rhythm": "every day",
            "lead_time": 1,
            "related_habit": related_habit.pk,
            "reward": "chocolate"
        }
        response = self.client.post("/habits/", data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn(
            "Нельзя использовать одновременно связанную привычку и вознаграждение",
            str(response.json())
        )

    def test_habit_delete(self):
        """Тестирование удаления привычки"""
        url = reverse("habits:habit-detail", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 1)
