'''Home work 3, task 4. Student is Vsevolod Dolgikh'''
'''
Программа принимает действительное положительное число x
 и целое отрицательное число y. Необходимо выполнить
  возведение числа x в степень y. Задание необходимо реализовать
   в виде функции my_func(x, y). При решении задания необходимо
    обойтись без встроенной функции возведения числа в степень.
    '''

def exponention(x, y):
    for i in range (y):
        x *= x
        return 1 / x


print(exponention(4,2))


