def int_func(some_word: str):
    str1 = ''
    some_word = some_word.split(" ")
    for item in some_word:
        str1 += item.title() + " "

    return print(str1)


int_func(some_word=input('Введите строку>>>'))
