def numbers(content):
    num_list = []
    num = ' '
    sum = 0
    for char in content:
        index = content.index(":")
        subject = content[:index]
        if char.isdigit():
            num = num + char
        else:
            if num != ' ':
                num_list.append(int(num))
                num = ' '
    for itm in num_list:
        sum += itm
        return subject, sum


file = open('task6.1.txt', 'r', encoding='utf-8')
content = file.readlines()
some_list = []
for itm in content:
    a, b = numbers(itm)
    some_list.append(a)
    some_list.append(b)
final_dict = {some_list[i]: some_list[i + 1] for i in range(0, len(some_list), 2)}
print(final_dict)
file.close()

