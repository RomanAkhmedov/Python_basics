# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл
# while и другие арифметические операции.
user_number = int(input('Введите целое положительное число: '))
user_digits = []
while user_number > 0:
    user_digits.append(user_number % 10)
    user_number //= 10
print(f'Наибольшая цифра в числе: {max(user_digits)}')
