# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы. Реализовать вывод
# данных о пользователе одной строкой.


def user_information(name, surname, birth_year, city, e_mail, telephone):
    """
    Выводит данные (согласно параметрам) о пользователе одной строкой

    Именованные параметры:
    name -- имя пользователя,
    surname -- фамилия пользователя,
    birth_year -- год рождения,
    city -- город проживания,
    e_mail -- адрес электронной почты,
    telephone -- телефон
    """
    print(f'Имя - {name}, Фамилия - {surname}, год рождения - {birth_year}, город проживания - {city}, '
          f'адрес электронной почты - {e_mail}, телефон - {telephone}')


user_information(name='Анатолий', surname='Сидоров', birth_year='1987', city='Волгоград', e_mail='sidoran@google.com',
                 telephone='+7(964)780-97-63')
