# Просим пользователя ввести строку для поиска
search = input("Введите строку для поиска: ")

# Открываем файл text.txt для чтения
with open("text.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # читаем все строки в список

# Создаем пустой список для найденных строк
found_lines = []

# Проверяем каждую строку из файла
for line in lines:
    if search.lower() in line.lower():  # ищем без учета регистра
        found_lines.append(line.strip())  # добавляем строку без пробелов и \n, если строка подходит

# Проверяем, есть ли найденные строки
if len(found_lines) == 0: # если их нет, выводим результат
    print("Совпадений не найдено.") 
else: # иначе выводим их
    print("\nНайденные строки:")
    for line in found_lines:
        print(line)

    print("\nКоличество найденных строк:", len(found_lines)) # выводим результат

    # Сортируем найденные строки по длине(от короткой к длинной)
    found_lines.sort(key=len)

    print("\nСтроки, отсортированные по длине:") # выводим результат
    for line in found_lines:
        print(line)