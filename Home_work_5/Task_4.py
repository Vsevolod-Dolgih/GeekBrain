'''Task 4,  student is Vsevolod Dolgikh

4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение
и считывающую построчно данные. При этом английские числительные
должны заменяться на русские. Новый блок строк
должен записываться в новый текстовый файл.
'''
replace = {'один': 'one', 'два': 'two', 'три': 'three', 'четыре': 'four',}

A = open('task_4.txt','r')
B = open('tag.txt','w')

for line in A:
    for key, value in replace.items():
        line = line.replace(key, value)
        B.write(line)
B.close()
A.close()