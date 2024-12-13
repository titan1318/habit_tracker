from unittest.mock import patch
from django.test import TestCase
from .services import send_telegram_message


class TelegramServiceTests(TestCase):

    @patch("requests.post")
    def test_send_telegram_message(self, mock_post):
        """Тест отправки сообщения в Telegram"""
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {"ok": True}

        response = send_telegram_message("Test message")
        self.assertTrue(response["ok"])
        mock_post.assert_called_once()
