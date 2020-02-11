'''Task 6,  student is Vsevolod Dolgikh

Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
'''

from itertools import  count
from itertools import cycle
from random import  randint


Karl = [i for i in count(2)]

list = [randint(1, 100) for i in range (10)]

Varl = [i for i in cycle(list)]

k = 0
for item in cycle(list):
    if k > 20:
        break
    print(item)
