import random # импортируем модуль для случайных чисел

# Создаём список из 25 случайных чисел от -50 до 50
numbers = [random.randint(-50, 50) for _ in range(25)]
print("Заполненный список:", numbers)

# Создаём счётчики
count_plus = 0   # положительные
count_minus = 0  # отрицательные
count_zero = 0   # нули

# Считаем все категории
for num in numbers:
    if num > 0:
        count_plus += 1
    elif num < 0:
        count_minus += 1
    else:
        count_zero += 1

total = len(numbers)  # общее количество чисел

# Выводим результаты с процентами (просто, без f-строк)
percent_plus = count_plus / total * 100
percent_minus = count_minus / total * 100
percent_zero = count_zero / total * 100

print("\nПоложительные числа:", count_plus, "шт.,", round(percent_plus, 2), "% от списка") # выводим результаты
print("Отрицательные числа:", count_minus, "шт.,", round(percent_minus, 2), "% от списка")
print("Нули:", count_zero, "шт.,", round(percent_zero, 2), "% от списка")

# Находим максимум и минимум
print("\nСамое большое число:", max(numbers))
print("Самое маленькое число:", min(numbers))