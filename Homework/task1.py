def user_text():
    some_list = []
    while True:
        user_input = input("Введите строку (для выхода нажмите enter) >>>")
        if user_input == "":
            break
        some_list.append(user_input + "\n")
    return some_list


file = open("task1.txt", "w")
file.writelines(user_text())
file.close()
