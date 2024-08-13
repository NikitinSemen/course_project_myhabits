import requests

from config.settings import BOT_TOKEN, TELEGRAM_URL


def send_telegram_message(message, tg_id):
    params = {"text": message, "chat_id": tg_id}
    requests.get(f"{TELEGRAM_URL}{BOT_TOKEN}/sendMessage", params=params)
