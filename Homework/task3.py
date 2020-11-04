def my_func(arg1, arg2, arg3):
    some_list = [arg1, arg2, arg3]
    for item in range((len(some_list) - 1)):
        if some_list[item] < some_list[item + 1]:
            some_list[item], some_list[item + 1] = some_list[item + 1], some_list[item]

    return print(some_list[0] + some_list[1])


my_func(0, 1, 7)
