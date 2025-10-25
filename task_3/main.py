kolvo_lines = int(input('Введите количество строк: '))
if kolvo_lines > 0:
    lines = []
    for i in range(kolvo_lines):
        line = input(f'Строка {i + 1}: ')
        lines.append(line)
    text = ' '.join(lines)
    words = text.split()
    uniq_words = set(words)
    print(f'Количество различных слов: {len(uniq_words)}')
else:
    print('Строк должно быть больше 0.')