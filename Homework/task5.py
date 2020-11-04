my_list = [7, 5, 3, 3, 2]
user_number = int(input("Введите число>>>"))
n = 0
while n < len(my_list):
    if user_number > my_list[n]:
        my_list.insert(n, user_number)
        print(my_list)
        break
    elif n == (len(my_list) - 1):
        my_list.append(user_number)
        print(my_list)
        break
    else:
        n += 1
