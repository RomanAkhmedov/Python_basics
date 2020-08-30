# * Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя.

# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-характеристик, например список названий товаров.

# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

# Формирование банка данных о товарах:
materials = []
goods_number = int(input('Введите количество товаров: '))
goods_characteristic = int(input('Введите кол-во характеристик товаров: '))
dict_keys = []
dict_values = []
good_info = []
for i in range(1, goods_characteristic + 1):
    dict_keys.append(input(f'Введите {i}-й параметр: '))
for i in range(1, goods_number + 1):
    dict_values.clear()
    good_info.clear()
    for j in range(0, goods_characteristic):
        dict_values.append(input(f'Введите значение параметра "{dict_keys[j]}" для {i}-го товара: '))
    good_info.append(i)
    good_info.append(dict(zip(dict_keys, dict_values)))
    materials.append(tuple(good_info))
print('Список товаров: ')
for idx, el in enumerate(materials, 1):
    print(f'{idx}-й - {el}')

# Аналитика:
values_analysis = []
goods_analysis = {}
for i in range(goods_characteristic):
    for j in range(goods_number):
        values_analysis.append(materials[j][1].get(dict_keys[i]))
    dictionary = {dict_keys[i]: values_analysis}
    goods_analysis.update(dictionary)
    values_analysis = []
    dictionary.clear()
print(f'Аналитика товаров: {goods_analysis}')
