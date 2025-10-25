import random
values = [-3, -5, -2, -12, 0, 15, 4, 7, 2]
a = random.randint(4, 8)
b = random.randint(4, 8)
matrix = []
for i in range(a):
    row = []
    for j in range(b):
        row.append(random.choice(values))
    matrix.append(row)
print(f'Матрица {a} * {b}:\n')
for row in matrix:
    print(' '.join(map(str, row))) # преобразуем числа в строке в строки и пишем через пробелы
sum_minus = 0
for i in range(a):
    for j in range(b):
        if matrix[i][j] < 0:
            sum_minus += matrix[i][j]
if sum_minus != 0:
    print('Сумма всех отрицательных элементов:', sum_minus)
else:
    print('Отрицательных элементов нет.')