''' Task 1,  student is Vsevolod Dolgikh

Реализовать скрипт, в котором должна быть предусмотрена
 функция расчета заработной платы сотрудника. В расчете
 необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
 Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами
 .'''

def wage():
    #Функция принимает будет считать зарплату для каждого сотрудника
    Name_employee = input('Enter the name of your employe: ')
    hourly_rate = float(input('Enter the hourly rate of his work : '))
    worked_out = float(input('Enter how many ours worked out: '))
    bonus = float(input('Enter the bonus of that employe : '))
    salary = (hourly_rate * worked_out) + bonus
    return  print(Name_employee , salary)

wage()

