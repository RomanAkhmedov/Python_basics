# Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами
# 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка
# элементов необходимо использовать функцию input().
number_of_elements = int(input('Введите кол-во элементов списка: '))
user_list = []
for i in range(number_of_elements):
    element = int(input(f'Введите значение {i + 1}-го элемента: '))
    user_list.append(element)
print(f'Исходный список: {user_list}')
for i in range(0, len(user_list), 2):
    if i == len(user_list) - 1:
        if len(user_list) % 2 != 0:
            break
    user_list[i], user_list[i + 1] = user_list[i + 1], user_list[i]
print(f'Измененный список: {user_list}')
