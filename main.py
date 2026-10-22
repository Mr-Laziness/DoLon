import logging

from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

from config import TOKEN
from handlers import (
    start,
    help_command,
    stats,
    add,
    echo,
    error_handler,
)

logging.basicConfig(
    format="%(asctime)s — %(name)s — %(levelname)s — %(message)s",
    level=logging.INFO,
)

logging.getLogger("httpx").setLevel(logging.WARNING)


def main() -> None:
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("stats", stats))
    app.add_handler(CommandHandler("add", add))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.add_error_handler(error_handler)

    print("✅ Бот запущен.")
    print("📱 Открой Telegram и отправь своему боту команду /start")
    print("🛑 Чтобы остановить бота, нажми Ctrl + C в терминале.")

    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()