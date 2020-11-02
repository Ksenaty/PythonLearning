month = int(input('Введите месяц(число)>>>'))
list_winter = [12, 1, 2]
list_spring = [3, 4, 5]
list_summer = [6, 7, 8]
list_autumn = [9, 10, 11]
if month in list_winter:
    print('Вы ввели месяц из зимы')
if month in list_spring:
    print('Вы ввели месяц из весны')
if month in list_summer:
    print('Вы ввели месяц из лета')
if month in list_autumn:
    print('Вы ввели месяц из осени')
