'''Home work 3, task 2. Student is Vsevolod Dolgikh'''
'''
Реализовать функцию, принимающую несколько параметров,
 описывающих данные пользователя: имя, фамилия, год рождения,
  город проживания, email, телефон. Функция должна принимать 
  параметры как именованные аргументы. Реализовать вывод данных 
  о пользователе одной строкой.
  '''
def show_result(**kwargs:str) -> list:
    return list(kwargs.values())

def user_data():
    print(show_result(name = input('what is yoyre name? '),
                    ser_name = input('what is youre ser name? '),
                    birtday = input('when do you have day of birthday? '),
                    phone = input('what is your phone number'),
                    email = input('text your email: ')))

user_data()