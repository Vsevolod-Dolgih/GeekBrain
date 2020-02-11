list_origin = [ 123,'duck', 2.34, True, 0, bin(8), 'Gaga', oct(22), hex(3), ['yes,no'], False, None]
count = 0
for i in range (len(list_origin) // 2):
    list_origin[count],list_origin[count+1] = list_origin[count+1], list_origin[count]
    count+=2

print(list_origin)





