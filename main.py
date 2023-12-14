import resourses, random

print("В данном проекте выполнено 2 домашних задания.\n"
      "1 задание: Реализована функция method.\n"
      "2 задание: Брутфорс.\n")

print("1 задание решено 2-я способами.\n"
        "1 — Ответ получается, как указан в задании.\n"
        "2 — Реализована функция random и ответ будет уникальный каждый раз.\n"
        "Введите число 1, или 2: ")
nomer = int(input())
if nomer > 2:
    print("Вы не правильно ввели число.")
elif nomer == 1:
    # Функция для получения ответа [1,2,4,5,6]
    resourses.Method(True, False, True, True, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False, False, False, False, False, False, False, False, False, False, False,
        False, False, False, False)
else:
    # Генерация случайных значений True и False
    random_conditions = [random.choice([True, False]) for _ in range(40)]
    # Выполнение функции с генерированными значения True & False
    resourses.Method(*random_conditions)