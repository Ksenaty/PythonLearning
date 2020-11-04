user_str = input('Введите словосочетание>>>')
user_list = user_str.split(' ')
n = 0
for i in user_list:
    n += 1
    print('{0}.  {1}'.format(n, i[0:10]))
