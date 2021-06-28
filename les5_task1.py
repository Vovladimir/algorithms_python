'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
'''
from collections import defaultdict

N = int(input('Введите количество предприятия: '))

dict_company = defaultdict(list)
for i in range(N):
    lst = input('Введите их наименования и прибыль за четыре квартала для каждого предприятия: ').split()
    for j in lst[1:]:
        dict_company[lst[0]].append(j)

sum_profit = 0
for value in dict_company.values():
    for i in value:
        sum_profit += int(i)
avg_profit = round(sum_profit / N, 2)
print(f'Cредняя годовая прибыль = {avg_profit}')

for key, value in dict_company.items():
    spam = 0
    for i in value:
        spam += int(i)
    if spam > avg_profit:
        print(f'У предприятия "{key}" годовая прибыль = {spam}, что больше средней.')
    elif spam < avg_profit:
        print(f'У предприятия "{key}" годовая прибыль = {spam}, что меньше средней.')
    else:
        print(f'У предприятия "{key}" годовая прибыль = {spam}, что равно средней.')
