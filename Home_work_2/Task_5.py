list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
Answer = 'yes'
while Answer == 'yes':
    k = int(input('please type  your estimate '))
    dex = list.index(k)
    list.insert(dex,k)
    Answer = input('do you wonna again  yes or no ')

print(list)
