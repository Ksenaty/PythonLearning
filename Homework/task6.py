product_catalog_tmp = []
product_catalog = []
i = 1
while True:
    list_prod = input('Введите название товара>>>')
    list_price = int(input('Введите цену товара>>>'))
    list_amount = int(input('Введите количество товара>>>'))
    list_unit = input('Введите единицу товара>>>')
    dictionary = dict(название=list_prod,
                      цена=list_price,
                      количество=list_amount,
                      единица=list_unit)
    product_catalog_tmp.append(i)
    product_catalog_tmp.append(dictionary)
    product_catalog.append(product_catalog_tmp)
    i += 1
    answer = input(('Желаете добавить еще товар?(да/нет)'))
    if answer != 'да':
        break
tmp = 0
product_catalog = tuple(product_catalog_tmp)
while tmp < (len(product_catalog) - 1):
    print(product_catalog[tmp:(tmp + 2)])
    tmp += 2
