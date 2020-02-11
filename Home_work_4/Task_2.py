'''Task 2,  student is Vsevolod Dolgikh

Представлен список чисел. Необходимо вывести элементы
 исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
'''
#Список с случайными значениями
from random import randint
list = [12,2,1,5,32,2,45,6,6,5,77]
list_1 = [ randint(0,100)for i in range(50)]

# Долгий вариант решения
list_2 =[]
a = [int(i) for i in list_1 ]
print(a)
for i in range(1, len(a)):
    if a[i] > a[i - 1]:
        list_2.append(a[i])
print(list_2)

list_3 = [i for i in list_2]
print(list_3)


# быстрый вариант
list_4 = [i > i for i in list_1]


""" Пока решал данное задание часто встречался с данными ошибками, я до конца не смог понять как их избежать
#TypeError: 'int' object is not subscriptable
#int' object is not callable
"""













