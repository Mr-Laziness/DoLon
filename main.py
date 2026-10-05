name = "Клауд"
goal = "Стать Python backend-разработчиком"

print(f"Привет, {name}!")
print(f"Моя цель: {goal}")
def training_message(trainings):
    if trainings == 0:
        return "Начни с первой тренировки."
    elif trainings < 5:
        return "Хорошее начало. Продолжай!"
    return "Ты держишь темп. Отличная работа!"


print(training_message(0))
print(training_message(3))
print(training_message(7))