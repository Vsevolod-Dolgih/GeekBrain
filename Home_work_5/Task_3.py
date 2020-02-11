'''Task 3,  student is Vsevolod Dolgikh

3. Создать текстовый файл (не программно),
построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''


f = open('task3.txt', 'r')
file = f.readlines()
wage = []
name = []
for i in file:
    a = i.split()
    money = int(a[1])
    name = list(a[0])
    if money < 20000:
        print(f'{a[0]} has less wage then 20000')
    wage.append(money)
    name.append(name)




print(f'{sum(wage) / len(name)} this is midle of level sallary' )

f.close()
