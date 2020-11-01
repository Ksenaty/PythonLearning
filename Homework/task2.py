user_number = input('Введите любое число>>>')
some_list = [int(i) for i in user_number]
print("{1}  Размер списка: {0}".format(len(some_list), some_list))
s = len(some_list) // 2
for i in range(s):
    some_list[2*i], some_list[1 + 2*i] = some_list[1 + 2*i], some_list[2*i]
print(some_list)
