variable_sec = int(input('Введите время в секундах>>>'))
print('Вы ввели {}'.format(variable_sec))
variable_minutes = 0
variable_hours = 0
while variable_sec > 59.99:
    variable_minutes += 1
    variable_sec -= 60
    while variable_minutes > 59.99:
        variable_hours += 1
        variable_minutes -= 60

print('Время >>> {0:0>2d}:{1:0>2d}:{2:0>2d}'.format(variable_hours, variable_minutes, variable_sec))
