import random

file = open('text5.1.txt', 'w')
for i in range(random.randint(1, 300)):
    file.write(str(random.randint(0, 9)) + ' ')



file.close()

file = open('text5.1.txt', 'r')
content = file.read()
some_list = content.split(' ')
some_list.pop(-1)
print(some_list)
new_list = [int(item) for item in some_list]
print(f'Ссума чисел: {sum(new_list)}')
file.close()


