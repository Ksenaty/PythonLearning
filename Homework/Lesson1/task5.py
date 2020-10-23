gain = int(input('Введите значение выручки>>>'))
costs = int(input('Введите значение издержек>>>'))
if gain > costs:
    rentability = gain / costs
    print('Поздравляю! Вы закрылись с прибылью. Рентабельность: {0:.1%}'.format(rentability))
    workers = int(input('Введите численность сотрудников>>>'))
    income = (gain - costs) / workers
    print('Прибыль на одного сотрудника равна: {0}'.format(income))
else:
    loss = gain - costs
    print('Ничего хорошего, вы закрылись с убытком {0}'.format(loss))
