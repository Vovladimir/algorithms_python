'''
3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы
'''
import random

m = 5
array = [random.randint(0, 100) for i in range(2 * m + 1)]
print(array)


# для проверки встроенными функциями

def sort_median(array):
    array.sort()
    print(array)
    return array[len(array) // 2]


print(sort_median(array))



