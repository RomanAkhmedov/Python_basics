# Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма
# (прибыль - выручка больше издержек, или убыток - издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). Далее запросите
# численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
revenue = int(input('Введите значение выручки: '))
costs = int(input('Введите значение издержек: '))
if revenue > costs:
    print(f'Фирма работает с положительным финансовым результатом, размер прибыли: {revenue - costs}')
    print(f'При этом размер рентабельности: {round((revenue-costs)/revenue*100, 2)} %')
    staff_number = int(input('Введите численность сотрудников фирмы: '))
    print(f'Прибыль фирмы в расчете на одного сотрудника: {round((revenue - costs)/staff_number, 2)}')
elif revenue < costs:
    print(f'Фирма работает с отрицательным финансовым результатом, размер убытков: {costs - revenue}')
else:
    print(f'Фирма работает с нулевым финансовым результатом, без убытков и прибыли')
