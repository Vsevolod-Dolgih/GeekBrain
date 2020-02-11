'''Task 4,  student is Vsevolod Dolgikh

Представлен список чисел. Определить элементы списка,
 не имеющие повторений. Сформировать итоговый массив чисел, 
 соответствующих требованию. Элементы вывести в порядке их 
 следования в исходном списке. Для выполнения задания обязательно 
 использовать генератор.
 '''

from random import randint
list_1 = [randint(0,50) for i in range(11)]
print(list_1)

list_2 = [i for i in list_1  if list_1.count(i) == 1]

for i in list_1:
    if list_1.count(i) == 1:
        pass
    else:
        list_1.remove(i)

print(list_1)

a = set(list_1)
print(a)

