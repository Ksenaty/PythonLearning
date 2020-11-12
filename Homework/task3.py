import time


file = open('task3.txt', 'r')
content = file.readlines()
file.close()
data = [line.split(' ') for line in content]
data_workers = [el.rstrip() for el, i in data]
data_salary = [i.rstrip() for el, i in data]
for i in range(len(data_workers)):
    print("Сотрудник {0} имеет оклад {1}".format(data_workers[i], data_salary[i]))

print()
s = 0
for i in range(len(data_workers)):
    s += int(data_salary[i])
    if int(data_salary[i]) < 20000:
        print("Сотрудник {0} имеет оклад {1}".format(data_workers[i], data_salary[i]))

s = s / len(data_workers)
print()
print(f'Средняя зарплата сотрудников: {s}')

