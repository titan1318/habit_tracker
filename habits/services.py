import requests

TELEGRAM_API_URL = "https://api.telegram.org/bot{token}/sendMessage"
TELEGRAM_BOT_TOKEN = "ваш_токен_бота"
CHAT_ID = "ваш_chat_id"


def send_telegram_message(message):
    url = TELEGRAM_API_URL.format(token=TELEGRAM_BOT_TOKEN)
    data = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    return response.json()
