
second_in_our = 3600
second_in_minute = 60
user = int(input('Please, write any number :'))
ours = (user // second_in_our)
minute = (user % second_in_our) // second_in_minute
second = (user % second_in_our) % second_in_minute
print(f"{ours}:{minute}: {second}")
#git

