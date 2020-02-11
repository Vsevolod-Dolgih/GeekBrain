seasons = {
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'autumn',
    10: 'autumn',
    11: 'autumn',
    12: 'winter'
}
key = int(input('could you choice the number of mounth '))
print(seasons.get(key,'do not have any inform about it'))

list_of_seasons = ['zzzz', 'winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
                   'autumn', 'autumn', 'winter']
key_2 = int(input('could you choice the number of mounth '))
print(list_of_seasons[key_2])