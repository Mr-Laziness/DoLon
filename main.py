import os

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not TOKEN:
    raise ValueError(
        "Токен не найден. Проверь secret TELEGRAM_BOT_TOKEN "
        "в настройках GitHub Codespaces."
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_name = update.effective_user.first_name

    await update.message.reply_text(
        f"Привет, {user_name}! Я Football Progress Bot.\n\n"
        "Напиши /help, чтобы увидеть команды."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Команды:\n"
        "/start — начать\n"
        "/help — помощь\n"
        "/stats — показать статистику"
    )


async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Тренировок пока нет.\n"
        "Позже я научусь сохранять их в базу данных."
    )


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text

    await update.message.reply_text(
        f"Ты написал: {text}"
    )


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("Бот запущен. Открой Telegram и напиши ему /start.")
    app.run_polling()


if __name__ == "__main__":
    main()