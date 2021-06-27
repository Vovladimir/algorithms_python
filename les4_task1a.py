''' Выбрана задача 1 из 3 урока

В диапазоне натуральных чисел от 2 до n определить,

cколько из них кратны каждому из чисел в диапазоне от 2 до 9'''

import cProfile
import timeit


def multiple_count(n):
    summary_dict = dict()

    for div in range(2, 10):
        summary_dict[div] = 0

        for num in range(2, n + 1):

            if num % div == 0:
                summary_dict[div] += 1

    return summary_dict

# "les4_task1a.multiple_count(99)"
# {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
# 1000 loops, best of 5: 69.2 usec per loop

# "les4_task1a.multiple_count(999)"
# {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
# 1000 loops, best of 5: 675 usec per loop

# "les4_task1a.multiple_count(9999)"
# {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
# 1000 loops, best of 5: 7.01 msec per loop

# cProfile.run('multiple_count(99)')
# 1    0.000    0.000    0.000    0.000 les4_task1a.py:10(multiple_count)

# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.





def multiple_count1(n):
    summary_dict = {}

    for i in range(2, 10):
        summary_dict[i] = n // i

    return summary_dict

# python -m timeit -n 1000 -s "import les4_task1a" "les4_task1a.multiple_count1(99)"
# {2: 49, 3: 33, 4: 24, 5: 19, 6: 16, 7: 14, 8: 12, 9: 11}
# 1000 loops, best of 5: 1.06 usec per loop

# -m timeit -n 1000 -s "import les4_task1a" "les4_task1a.multiple_count1(999)"
# 1000 loops, best of 5: 1.16 usec per loop

# -m timeit -n 1000 -s "import les4_task1a" "les4_task1a.multiple_count1(9999)"
# 1000 loops, best of 5: 1.21 usec per loop

# cProfile.run('multiple_count1(9999)')
# 1    0.000    0.000    0.000    0.000 les4_task1a.py:45(multiple_count1)

# Алгоритм работает приблизительно за O(1). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивалось незначительно. При увеличении количества входных элементов в 1000 раз время
#  увеличилось всего на 14%

def multiple_count2(n):
    summary_dict = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

    for num in range(2, n + 1):

        if num % 2 == 0:
            summary_dict[2] += 1

        if num % 3 == 0:
            summary_dict[3] += 1

        if num % 4 == 0:
            summary_dict[4] += 1

        if num % 5 == 0:
            summary_dict[5] += 1

        if num % 6 == 0:
            summary_dict[6] += 1

        if num % 7 == 0:
            summary_dict[7] += 1

        if num % 8 == 0:
            summary_dict[8] += 1

        if num % 9 == 0:
            summary_dict[9] += 1

    return summary_dict
# -m timeit -n 1000 -s "import les4_task1a" "les4_task1a.multiple_count2(99)"
# 1000 loops, best of 5: 53.6 usec per loop

# -m timeit -n 1000 -s "import les4_task1a" "les4_task1a.multiple_count2(999)"
# 1000 loops, best of 5: 581 usec per loop

# -m timeit -n 1000 -s "import les4_task1a" "les4_task1a.multiple_count2(9999)"
# 1000 loops, best of 5: 6.02 msec per loop

# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.


# ВЫВОД:
# Алгоритм, использованный в функции multiple_count1(), является самым оптимальным и быстрым.
# Так как он выполняется практически за константное время, несильно завися от размера входных данных.
