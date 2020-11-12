file = open('task2.txt', 'r')
content = file.readlines()
print(file.read())
print('Количество строк в тексте: {}'.format(len(content)))
for idx, el in enumerate(content, 1):
    words_number = len(el.split(' '))
    print(f"В строке {idx} количество слов: {words_number}")

file.close()
