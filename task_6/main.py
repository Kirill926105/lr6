import random # импортируем модуль для случайных чисел

# Создаём список из 20 кортежей по 4 случайных числа от -10 до 10
values = [tuple(random.randint(-10, 10) for _ in range(4)) for _ in range(20)]
print("Список из 20 кортежей по 4 числа:", values)

# Находим все уникальные комбинации (не учитывая порядок)
unique_combinations = set(tuple(sorted(t)) for t in values)
unique_combinations = list(unique_combinations)
print("\nУникальные комбинации:", unique_combinations)

# Пользователь вводит целое число
user_value = int(input("\nВведите целое число для проверки суммы пар: "))

# Вычисляем количество пар кортежей, чья сумма элементов меньше заданного числа
pair_count = 0 # счетчик пар
n = len(values) # количество кортежей в списке

for i in range(n): # перебираем пары кортежей и проверяем условие выполнения счетчика
    for j in range(i + 1, n):  # чтобы не считать одну и ту же пару дважды
        sum1 = sum(values[i])
        sum2 = sum(values[j])
        if sum1 + sum2 < user_value:
            pair_count += 1

print("\nКоличество пар кортежей, чья сумма меньше", user_value, ":", pair_count) # выводим результат