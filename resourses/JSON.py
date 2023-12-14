import json # Библиотека для чтения json файла
import os # Библиотека для работы с файлами

# Объявляем функцию myjson
def myjson():
    # Запрашиваем директорию с файлом
    in_directory = input("Введите путь к директории, где находится файл:  ")
    # Проверяем, существовует ли директория
    if not os.path.exists(in_directory):
        print("Вы ошиблись, указанная директория не существует.")
        return

    # Запрашиваем имя файла
    in_filename = input("Введите имя файла, не забудьте указать его формат (.json): ")
    in_filepath = os.path.join(in_directory, in_filename)

    # Проверяем, существовует ли файл
    if not os.path.exists(in_filepath):
        print("Вы ошиблись, указанный файл не обнаружен.")
        return

    # Открытие и чтение файла
    with open(in_filepath, 'r', encoding='utf-8') as file:
        data = json.load(file) # Записываем считанный файл в переменную data

    # Извлекаем информацию из переменных "alert" и "count"
    vulnerabilities = [] # Объявляем список
    for site in data.get("site", []): # Указываем, что существует словарь site
        for alert in site.get("alerts", []): # Словарь alerts
            # Считываем переменные "alert" и "count" из словаря "alert"
            if "alert" in alert and "count" in alert:
                alert_text = alert["alert"] # Запоминаем текст alert
                count_value = alert["count"] # Запоминаем цифру count
                # Добавляем в список данные в заданном формате
                vulnerabilities.append({"name": alert_text, "count": int(count_value)})

    # Создание нового файла .json с обработанными данными
    out_filename = "result.json"
    out_filepath = os.path.join(in_directory, out_filename)

    # Записываем данные в файл в формате json, указываем кол-во пробелов 4 и выведем текст в читабельном виде
    with open(out_filepath, 'w', encoding='utf-8') as out_file:
        json.dump({"vulnerabilities": vulnerabilities}, out_file, indent=4, ensure_ascii=False)

    print(f"Данные успешно обработаны и записаны в файл: {out_filename}")

