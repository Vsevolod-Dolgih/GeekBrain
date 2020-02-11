num = int(input('Would you kind to write any number :'))

# Way number one

# found = []
# while num != 0:
#     f = num % 10
#     found.append(f)
#     num = num // 10
# print(max(found))

# Way number two
maximum = 0
while num > 0:
    last_digit = num % 10
    if last_digit > maximum:
        maximum = last_digit
    num = num // 10
print(maximum)
print(num)
#git

