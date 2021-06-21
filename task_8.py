'''
8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
'''
a, b, c = map(int, input('Введите три разных числа: ').split())
middle = c
if a < c < b or b < c < a:
    print(f'Среднее число = {middle}')
elif a < b < c or c < b < a:
    middle = b
    print(f'Среднее число = {middle}')
else:
    middle = a
    print(f'Среднее число = {middle}')
