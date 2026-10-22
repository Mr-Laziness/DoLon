from telegram import Update
from telegram.ext import ContextTypes

user_trainings = {}


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
    user_id = update.effective_user.id
    trainings = user_trainings.get(user_id, [])

    if not trainings:
        await update.message.reply_text(
            "📊 У тебя пока нет записанных тренировок.\n"
            "Добавь первую: /add 30"
        )
        return

    total_count = sum(trainings)

    await update.message.reply_text(
        f"📊 Твоя статистика:\n\n"
        f"Тренировок записано: {len(trainings)}\n"
        f"Всего повторений: {total_count}"
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

    user_id = update.effective_user.id

    if user_id not in user_trainings:
        user_trainings[user_id] = []

    user_trainings[user_id].append(count)

    await update.message.reply_text(
        f"Тренировка добавлена: {count} повторений.\n"
        f"Всего в памяти: {len(user_trainings[user_id])} шт."
    )


async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("ОШИБКА:")
    print(context.error)