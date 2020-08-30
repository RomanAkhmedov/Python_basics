# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# Решение через list.

month = None
while month not in range(1, 13):
    month = int(input('Номер месяца в диапазоне от 1 до 12: '))
year = list(range(1, 13))
if month in year[:2] or month == year[11]:
    print('Зима')
elif month in year[2:5]:
    print('Весна')
elif month in year[5:8]:
    print('Лето')
else:
    print('Осень')
