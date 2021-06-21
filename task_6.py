'''
6. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
составленного из этих отрезков. Если такой треугольник существует, то определить, является ли он разносторонним,
равнобедренным или равносторонним.
'''
a, b, c = input('Введите длины трех отрезков: ').split()
a = int(a)
b = int(b)
c = int(c)
if a + b < c or a + c < b or b + c < a:
    print('Треуголника не существует.')
elif a == b == c:
    print('Треугольник равносторонний.')
elif a == b or a == c or b == c:
    print('Треугольник равнобедренный')
else:
    print('Треугольник разносторонний.')