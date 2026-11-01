import sqlite3


def init_db():
    """Создаёт базу данных и таблицу тренировок, если их ещё нет."""
    connection = sqlite3.connect("nurelax.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trainings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            count INTEGER NOT NULL
        )
    """)

    connection.commit()
    connection.close()
    print("✅ База данных готова, таблица trainings создана.")


def add_training(user_id: int, count: int) -> None:
    """Сохраняет одну тренировку в базу."""
    connection = sqlite3.connect("nurelax.db")
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO trainings (user_id, count) VALUES (?, ?)",
        (user_id, count)
    )

    connection.commit()
    connection.close()


def get_user_trainings(user_id: int) -> list:
    """Возвращает список всех повторений для одного пользователя."""
    connection = sqlite3.connect("nurelax.db")
    cursor = connection.cursor()

    cursor.execute(
        "SELECT count FROM trainings WHERE user_id = ?",
        (user_id,)
    )

    rows = cursor.fetchall()
    connection.close()

    # fetchall() возвращает список кортежей: [(30,), (40,), ...]
    # Превращаем в обычный список чисел: [30, 40, ...]
    return [row[0] for row in rows]


if __name__ == "__main__":
    init_db()