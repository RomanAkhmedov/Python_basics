# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и другие арифметические операции.
user_number = int(input('Введите целое положительное число: '))
max_digit = user_number % 10
while user_number > 0:
    if user_number % 10 > max_digit:
        max_digit = user_number % 10
    user_number //= 10
print(f'Наибольшая цифра в числе: {max_digit}')
