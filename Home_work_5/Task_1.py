'''Task 1,  student is Vsevolod Dolgikh

1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
 Об окончании ввода данных свидетельствует пустая строка.
'''

file_name = input('Write the name of file: ')    # Предложим пользователю назвать файл


file = open(file_name, 'w')                      # Создаем и открываем данный файл



while True:
    text = input('Ener the text that you want: ') # Сщздаем цикл с возможностью писать столько сколько нужно
    if text == '':
        break
    file.write(text + '\n')
file.close()