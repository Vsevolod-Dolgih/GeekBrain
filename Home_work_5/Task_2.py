'''Task 2,  student is Vsevolod Dolgikh

2. Создать текстовый файл (не программно),
сохранить в нем несколько строк, выполнить подсчет
количества строк, количества слов в каждой строке.
'''

# Переменные для подсчета строк, слов и букв.
lines = 0
words = 0
letters = 0


for line in open('task.txt', 'r'):
    lines += 1
# Определим  количество символов в строке
    letters += len(line)
# Флаг, сигнализирующий нахождение за пределами слова.
    pos = 'out'
# Цикл перебора строки по символам.
    for letter in line:
        # Если очередной символ не пробел, а флаг в значении "вне слова",
        # то значит начинается новое слово.
        if letter != ' ' and pos == 'out':
            # Поэтому надо увеличить счетчик слов на 1,
            words += 1
            # а флаг поменять на значение "внутри слова".
            pos = 'in'
        # Если очередной символ пробел,
        elif letter == ' ':
            # то следует установить флаг в значение "вне слова".
            pos = 'out'

# Вывод количеств строк, слов и символов на экран.
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)

