# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов.


def sum_of_two_max(el_1, el_2, el_3):
    """
    Принимает три позиционных аргумента, возвращает сумму наибольших двух аргументов

    (number, number, number) -> number

    >>> sum_of_two_max(8,5,12)
    20
    """
    numb = [el_1, el_2, el_3]
    numb.remove(min(numb))
    return sum(numb)


print(sum_of_two_max(17, 9, 15))
