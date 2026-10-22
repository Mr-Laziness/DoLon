import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "Токен не найден.\n"
        "Проверь GitHub Settings → Codespaces → Secrets.\n"
        "Имя секрета должно быть: TELEGRAM_BOT_TOKEN"
    )