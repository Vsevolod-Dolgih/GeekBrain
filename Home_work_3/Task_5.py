'''Home work 3, task 5. Student is Vsevolod Dolgikh'''
'''
Программа запрашивает у пользователя строку чисел,
 разделенных пробелом. При нажатии Enter должна выводиться
  сумма чисел. Пользователь может продолжить ввод чисел,
  разделенных пробелом и снова нажать Enter. Сумма вновь
  введенных чисел будет добавляться к уже подсчитанной сумме.
   Но если вместо числа вводится специальный символ, выполнение
    программы завершается. Если специальный символ введен после
    нескольких чисел, то вначале нужно добавить сумму этих чисел к
    полученной ранее сумме и после этого завершить программу.
    '''
def string_numbers():
    count = 0
    while True:
        numbers = input('Write line of numbers or & if you want to exit: ').split()
        for i in numbers:
            try:
                if i == '&':
                    print(f'the amount is {count}. ')
                    return
                else:
                    count += int(i)
            except ValueError:
                print('Text a number or &')
        print(f'the amount is {count}')

string_numbers()
