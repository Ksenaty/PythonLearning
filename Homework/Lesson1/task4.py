user_number = int(input('Введите число>>>'))
max_number = 0
while user_number > 0:
    comparing_number = user_number % 10
    if max_number < comparing_number:
        max_number = comparing_number
        user_number //= 10
    else:
        user_number //= 10
    comparing_number = user_number % 10
print(max_number)
