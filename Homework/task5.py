def summary(user_str):
    some_list = user_str.split(" ")
    some_list = [int(item) for item in some_list]
    print(sum(some_list))
    while True:
        user_str = input('Введите числа через пробел(Для прекращения введите любую букву в конце числа)>>>')
        check_list = user_str.split(" ")
        try:
            check_list = [int(item) for item in check_list]
            for item in check_list:
                some_list.append(item)
            print(sum(some_list))
        except ValueError:
            check_list.pop(-1)
            for item in check_list:
                some_list.append(item)
            print(sum(some_list))
            break

    return


summary(input("Введите числа через пробел>>>"))
