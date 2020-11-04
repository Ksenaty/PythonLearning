def division(arg1, arg2):
    try:
        return print(arg1 / arg2)
    except ZeroDivisionError:
        return print(0)


division(float(input('Введите числитель>>>')), float(input('Введите знаменатель>>>')))
