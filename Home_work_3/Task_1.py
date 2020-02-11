'''Home work 3, task 1. Student is Vsevolod Dolgikh'''
'''
 Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть
  обработку ситуации деления на ноль.
  '''

def division(a:int, b:int) -> int:
    try:
        return a / b
    except ZeroDivisionError:
        return 'No / 0'
    except ValueError:
        return 'No value'


# Coment - this is 1 way
#a , b = int(input('a = ')), int(input('b = '))
#result = division(a , b)
#print(result)

# 2 way
user = division(int(input()), int(input()))
print(user)

