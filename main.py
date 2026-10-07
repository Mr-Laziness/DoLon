import logging
import os

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)


logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)

logging.getLogger("httpx").setLevel(logging.WARNING)


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "Токен не найден.\n"
        "Проверь GitHub Settings → Codespaces → Secrets.\n"
        "Имя секрета должно быть: TELEGRAM_BOT_TOKEN"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name

    print(f"Получена команда /start от: {user_name}")

    await update.message.reply_text(
        f"Привет, {user_name}! 👋\n\n"
        "Я Football Progress Bot.\n"
        "Я буду помогать тебе записывать и отслеживать футбольные тренировки.\n\n"
        "Напиши /help, чтобы увидеть команды."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Получена команда /help")

    await update.message.reply_text(
        "Мои команды:\n\n"
        "/start — начать работу\n"
        "/help — показать помощь\n"
        "/stats — показать статистику\n\n"
        "Также можешь отправить обычное сообщение, "
        "и я повторю его."
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Получена команда /stats")

    await update.message.reply_text(
        "📊 Твоя статистика\n\n"
        "Тренировок пока нет.\n"
        "Следующим шагом мы добавим команду для их записи."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    print(f"Получено обычное сообщение: {text}")

    await update.message.reply_text(
        f"Ты написал:\n{text}"
    )


async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args

    if not args:
        await update.message.reply_text(
            "Пожалуйста, укажи число повторений.\n"
            "Пример: /add 30"
        )
        return

    try:
        count = int(args[0])
    except ValueError:
        await update.message.reply_text(
            f"«{args[0]}» — это не число.\n"
            "Пример правильной команды: /add 30"
        )
        return

    await update.message.reply_text(
        f"Тренировка добавлена: {count} повторений"
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("ОШИБКА:")
    print(context.error)


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_error_handler(error_handler)

    print("✅ Бот запущен.")
    print("📱 Открой Telegram и отправь своему боту команду /start")
    print("🛑 Чтобы остановить бота, нажми Ctrl + C в терминале.")

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()