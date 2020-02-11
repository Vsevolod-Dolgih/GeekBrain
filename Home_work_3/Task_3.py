'''Home work 3, task 3. Student is Vsevolod Dolgikh'''
'''
Реализовать функцию my_func(), которая
 принимает три позиционных аргумента, и
 возвращает сумму наибольших двух аргументов.
 '''

def my_func(a, b, c):
    list = [a, b, c]
    list.remove(min(a, b, c))
    return sum(list)

def result():
    print(my_func(a = int(input('write first number')),
                  b = int(input('write second number ')),
                  c = int(input('write third number'))))

result()