'''
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
'''
import sys
from math import sqrt

# print(sys.version, sys.platform)
# 3.8.10 (default, May 19 2021, 13:12:32) [MSC v.1916 32 bit (Intel)] win32


def show_size(x, level=0):
    ''' Добавил в функцию сложение всех затрат памяти
        и возврат общей суммы затраченной памяти '''
    size_par = sys.getsizeof(x)
    print('\t' * level, f'type={type(x)}, size={size_par}, object={x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                size_par = size_par + sys.getsizeof(key)
                show_size(value, level + 1)
                size_par = size_par + sys.getsizeof(value)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)
                size_par = size_par + sys.getsizeof(item)
    return size_par
#
#
# from random import sample
#
# list_num = sample(range(1, 11), 10)
# print(list_num)
#
# @profile
# def calculate_between_min_max(array):
#     min_num = array[0]
#     max_num = array[len(array) - 1]
#     index_min = 0
#     index_max = 0
#
#     for i, item in enumerate(array):
#         if min_num > item:
#             min_num = item
#             index_min = i
#         if max_num < item:
#             max_num = item
#             index_max = i
#     if index_min > index_max:
#         index_min, index_max = index_max, index_min
#
#     new_list = array[index_min + 1:index_max]
#
#     sum = 0
#     for i in new_list:
#         sum += i
#
#     # return f'Сумма между максимальными минимальным числом в списке {array} = {sum}'
#     return locals()
#     if __name__ == '__main__':
#         calculate_between_min_max()
#
# show_size(calculate_between_min_max(list_num))


def erathosphen_sieve(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i * 2
            while j < n:
                sieve[j] = 0
                j += i
    result = [i for i in sieve if i != 0]
    return result

#  type=<class 'list'>, size=128, object=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=5
# 	 type=<class 'int'>, size=14, object=7
# 	 type=<class 'int'>, size=14, object=11
# 	 type=<class 'int'>, size=14, object=13
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=29
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=37
# 	 type=<class 'int'>, size=14, object=41
# 	 type=<class 'int'>, size=14, object=43
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=59
# 	 type=<class 'int'>, size=14, object=61
# 	 type=<class 'int'>, size=14, object=67
# 	 type=<class 'int'>, size=14, object=71
# 	 type=<class 'int'>, size=14, object=73
# 	 type=<class 'int'>, size=14, object=79
# 	 type=<class 'int'>, size=14, object=83
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=97
# 478


def prime(n):
    lst = [2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


#  type=<class 'list'>, size=132, object=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=5
# 	 type=<class 'int'>, size=14, object=7
# 	 type=<class 'int'>, size=14, object=11
# 	 type=<class 'int'>, size=14, object=13
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=29
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=37
# 	 type=<class 'int'>, size=14, object=41
# 	 type=<class 'int'>, size=14, object=43
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=59
# 	 type=<class 'int'>, size=14, object=61
# 	 type=<class 'int'>, size=14, object=67
# 	 type=<class 'int'>, size=14, object=71
# 	 type=<class 'int'>, size=14, object=73
# 	 type=<class 'int'>, size=14, object=79
# 	 type=<class 'int'>, size=14, object=83
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=97
# 482


def prime1(n):
    lst=[2]
    for i in range(3, n+1, 2):
        if (i > 10) and (i%10==5):
            continue
        for j in lst:
            if j > int((sqrt(i)) + 1):
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst

#  type=<class 'list'>, size=132, object=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=5
# 	 type=<class 'int'>, size=14, object=7
# 	 type=<class 'int'>, size=14, object=11
# 	 type=<class 'int'>, size=14, object=13
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=29
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=37
# 	 type=<class 'int'>, size=14, object=41
# 	 type=<class 'int'>, size=14, object=43
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=59
# 	 type=<class 'int'>, size=14, object=61
# 	 type=<class 'int'>, size=14, object=67
# 	 type=<class 'int'>, size=14, object=71
# 	 type=<class 'int'>, size=14, object=73
# 	 type=<class 'int'>, size=14, object=79
# 	 type=<class 'int'>, size=14, object=83
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=97
# 482

# print(show_size(erathosphen_sieve(100)))
# print(show_size(prime(100)))
# print(show_size(prime1(100)))

'''Для сравнения сделаю функцию заранее неоптимальную по затратам памяти из-за использования множеств'''

def set_prime_100(n):
    prime_set = (2,	3,	5,	7,	11,	13,	17,	19,	23,	29,	31,	37,41,43,47,53,	59,	61,	67,	71,	73,	79,	83,	89,97)
    return_set = set()
    for el in prime_set:
        if n > el:
            return_set.add(el)
        else:
            break
    return return_set

# print(show_size(set_prime_100(100)))
#  type=<class 'set'>, size=1132, object={2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=5
# 	 type=<class 'int'>, size=14, object=7
# 	 type=<class 'int'>, size=14, object=11
# 	 type=<class 'int'>, size=14, object=13
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=29
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=37
# 	 type=<class 'int'>, size=14, object=41
# 	 type=<class 'int'>, size=14, object=43
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=59
# 	 type=<class 'int'>, size=14, object=61
# 	 type=<class 'int'>, size=14, object=67
# 	 type=<class 'int'>, size=14, object=71
# 	 type=<class 'int'>, size=14, object=73
# 	 type=<class 'int'>, size=14, object=79
# 	 type=<class 'int'>, size=14, object=83
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=97
# 1482

# из-за того, что словарь занимает много места в памяти на малых величанах сильно проигрывает в памяти (478) против (1482)
# увеличим множество до 1000
def set_prime_1000(n):

    prime_set_1000=(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101,
                103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
                211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
                331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443,
                449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577,
                587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839,
                853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983,
                991, 997)
    return_set = set()
    for el in prime_set_1000:
        if n > el:
            return_set.add(el)
        else:
            break
    return return_set

print(show_size(set_prime_1000(1000)))
# print(show_size(erathosphen_sieve(1000)))

#  type=<class 'set'>, size=4204, object={2, 3, 5, 7, 521, 11, 523, 13, 17, 19, 23, 541, 29, 31, 547, 37, 41, 43, 557,
#  47, 563, 53, 569, 59, 571, 61, 577, 67, 71, 73, 587, 79, 593, 83, 599, 89, 601, 607, 97, 101, 613, 103, 617, 107,
#  619, 109, 113, 631, 127, 641, 131, 643, 647, 137, 139, 653, 659, 149, 661, 151, 157, 673, 163, 677, 167, 683, 173,
#  179, 691, 181, 701, 191, 193, 197, 709, 199, 719, 211, 727, 733, 223, 227, 739, 229, 743, 233, 239, 751, 241, 757,
#  761, 251, 257, 769, 773, 263, 269, 271, 787, 277, 281, 283, 797, 293, 809, 811, 307, 821, 311, 823, 313, 827, 317,
#  829, 839, 331, 337, 853, 857, 347, 859, 349, 863, 353, 359, 877, 367, 881, 883, 373, 887, 379, 383, 389, 907, 397,
#  911, 401, 919, 409, 929, 419, 421, 937, 941, 431, 433, 947, 439, 953, 443, 449, 967, 457, 971, 461, 463, 977, 467,
#  983, 479, 991, 997, 487, 491, 499, 503, 509}
# 	 type=<class 'int'>, size=14, object=2
# 	 type=<class 'int'>, size=14, object=3
# 	 type=<class 'int'>, size=14, object=5
# 	 type=<class 'int'>, size=14, object=7
# 	 type=<class 'int'>, size=14, object=521
# 	 type=<class 'int'>, size=14, object=11
# 	 type=<class 'int'>, size=14, object=523
# 	 type=<class 'int'>, size=14, object=13
# 	 type=<class 'int'>, size=14, object=17
# 	 type=<class 'int'>, size=14, object=19
# 	 type=<class 'int'>, size=14, object=23
# 	 type=<class 'int'>, size=14, object=541
# 	 type=<class 'int'>, size=14, object=29
# 	 type=<class 'int'>, size=14, object=31
# 	 type=<class 'int'>, size=14, object=547
# 	 type=<class 'int'>, size=14, object=37
# 	 type=<class 'int'>, size=14, object=41
# 	 type=<class 'int'>, size=14, object=43
# 	 type=<class 'int'>, size=14, object=557
# 	 type=<class 'int'>, size=14, object=47
# 	 type=<class 'int'>, size=14, object=563
# 	 type=<class 'int'>, size=14, object=53
# 	 type=<class 'int'>, size=14, object=569
# 	 type=<class 'int'>, size=14, object=59
# 	 type=<class 'int'>, size=14, object=571
# 	 type=<class 'int'>, size=14, object=61
# 	 type=<class 'int'>, size=14, object=577
# 	 type=<class 'int'>, size=14, object=67
# 	 type=<class 'int'>, size=14, object=71
# 	 type=<class 'int'>, size=14, object=73
# 	 type=<class 'int'>, size=14, object=587
# 	 type=<class 'int'>, size=14, object=79
# 	 type=<class 'int'>, size=14, object=593
# 	 type=<class 'int'>, size=14, object=83
# 	 type=<class 'int'>, size=14, object=599
# 	 type=<class 'int'>, size=14, object=89
# 	 type=<class 'int'>, size=14, object=601
# 	 type=<class 'int'>, size=14, object=607
# 	 type=<class 'int'>, size=14, object=97
# 	 type=<class 'int'>, size=14, object=101
# 	 type=<class 'int'>, size=14, object=613
# 	 type=<class 'int'>, size=14, object=103
# 	 type=<class 'int'>, size=14, object=617
# 	 type=<class 'int'>, size=14, object=107
# 	 type=<class 'int'>, size=14, object=619
# 	 type=<class 'int'>, size=14, object=109
# 	 type=<class 'int'>, size=14, object=113
# 	 type=<class 'int'>, size=14, object=631
# 	 type=<class 'int'>, size=14, object=127
# 	 type=<class 'int'>, size=14, object=641
# 	 type=<class 'int'>, size=14, object=131
# 	 type=<class 'int'>, size=14, object=643
# 	 type=<class 'int'>, size=14, object=647
# 	 type=<class 'int'>, size=14, object=137
# 	 type=<class 'int'>, size=14, object=139
# 	 type=<class 'int'>, size=14, object=653
# 	 type=<class 'int'>, size=14, object=659
# 	 type=<class 'int'>, size=14, object=149
# 	 type=<class 'int'>, size=14, object=661
# 	 type=<class 'int'>, size=14, object=151
# 	 type=<class 'int'>, size=14, object=157
# 	 type=<class 'int'>, size=14, object=673
# 	 type=<class 'int'>, size=14, object=163
# 	 type=<class 'int'>, size=14, object=677
# 	 type=<class 'int'>, size=14, object=167
# 	 type=<class 'int'>, size=14, object=683
# 	 type=<class 'int'>, size=14, object=173
# 	 type=<class 'int'>, size=14, object=179
# 	 type=<class 'int'>, size=14, object=691
# 	 type=<class 'int'>, size=14, object=181
# 	 type=<class 'int'>, size=14, object=701
# 	 type=<class 'int'>, size=14, object=191
# 	 type=<class 'int'>, size=14, object=193
# 	 type=<class 'int'>, size=14, object=197
# 	 type=<class 'int'>, size=14, object=709
# 	 type=<class 'int'>, size=14, object=199
# 	 type=<class 'int'>, size=14, object=719
# 	 type=<class 'int'>, size=14, object=211
# 	 type=<class 'int'>, size=14, object=727
# 	 type=<class 'int'>, size=14, object=733
# 	 type=<class 'int'>, size=14, object=223
# 	 type=<class 'int'>, size=14, object=227
# 	 type=<class 'int'>, size=14, object=739
# 	 type=<class 'int'>, size=14, object=229
# 	 type=<class 'int'>, size=14, object=743
# 	 type=<class 'int'>, size=14, object=233
# 	 type=<class 'int'>, size=14, object=239
# 	 type=<class 'int'>, size=14, object=751
# 	 type=<class 'int'>, size=14, object=241
# 	 type=<class 'int'>, size=14, object=757
# 	 type=<class 'int'>, size=14, object=761
# 	 type=<class 'int'>, size=14, object=251
# 	 type=<class 'int'>, size=14, object=257
# 	 type=<class 'int'>, size=14, object=769
# 	 type=<class 'int'>, size=14, object=773
# 	 type=<class 'int'>, size=14, object=263
# 	 type=<class 'int'>, size=14, object=269
# 	 type=<class 'int'>, size=14, object=271
# 	 type=<class 'int'>, size=14, object=787
# 	 type=<class 'int'>, size=14, object=277
# 	 type=<class 'int'>, size=14, object=281
# 	 type=<class 'int'>, size=14, object=283
# 	 type=<class 'int'>, size=14, object=797
# 	 type=<class 'int'>, size=14, object=293
# 	 type=<class 'int'>, size=14, object=809
# 	 type=<class 'int'>, size=14, object=811
# 	 type=<class 'int'>, size=14, object=307
# 	 type=<class 'int'>, size=14, object=821
# 	 type=<class 'int'>, size=14, object=311
# 	 type=<class 'int'>, size=14, object=823
# 	 type=<class 'int'>, size=14, object=313
# 	 type=<class 'int'>, size=14, object=827
# 	 type=<class 'int'>, size=14, object=317
# 	 type=<class 'int'>, size=14, object=829
# 	 type=<class 'int'>, size=14, object=839
# 	 type=<class 'int'>, size=14, object=331
# 	 type=<class 'int'>, size=14, object=337
# 	 type=<class 'int'>, size=14, object=853
# 	 type=<class 'int'>, size=14, object=857
# 	 type=<class 'int'>, size=14, object=347
# 	 type=<class 'int'>, size=14, object=859
# 	 type=<class 'int'>, size=14, object=349
# 	 type=<class 'int'>, size=14, object=863
# 	 type=<class 'int'>, size=14, object=353
# 	 type=<class 'int'>, size=14, object=359
# 	 type=<class 'int'>, size=14, object=877
# 	 type=<class 'int'>, size=14, object=367
# 	 type=<class 'int'>, size=14, object=881
# 	 type=<class 'int'>, size=14, object=883
# 	 type=<class 'int'>, size=14, object=373
# 	 type=<class 'int'>, size=14, object=887
# 	 type=<class 'int'>, size=14, object=379
# 	 type=<class 'int'>, size=14, object=383
# 	 type=<class 'int'>, size=14, object=389
# 	 type=<class 'int'>, size=14, object=907
# 	 type=<class 'int'>, size=14, object=397
# 	 type=<class 'int'>, size=14, object=911
# 	 type=<class 'int'>, size=14, object=401
# 	 type=<class 'int'>, size=14, object=919
# 	 type=<class 'int'>, size=14, object=409
# 	 type=<class 'int'>, size=14, object=929
# 	 type=<class 'int'>, size=14, object=419
# 	 type=<class 'int'>, size=14, object=421
# 	 type=<class 'int'>, size=14, object=937
# 	 type=<class 'int'>, size=14, object=941
# 	 type=<class 'int'>, size=14, object=431
# 	 type=<class 'int'>, size=14, object=433
# 	 type=<class 'int'>, size=14, object=947
# 	 type=<class 'int'>, size=14, object=439
# 	 type=<class 'int'>, size=14, object=953
# 	 type=<class 'int'>, size=14, object=443
# 	 type=<class 'int'>, size=14, object=449
# 	 type=<class 'int'>, size=14, object=967
# 	 type=<class 'int'>, size=14, object=457
# 	 type=<class 'int'>, size=14, object=971
# 	 type=<class 'int'>, size=14, object=461
# 	 type=<class 'int'>, size=14, object=463
# 	 type=<class 'int'>, size=14, object=977
# 	 type=<class 'int'>, size=14, object=467
# 	 type=<class 'int'>, size=14, object=983
# 	 type=<class 'int'>, size=14, object=479
# 	 type=<class 'int'>, size=14, object=991
# 	 type=<class 'int'>, size=14, object=997
# 	 type=<class 'int'>, size=14, object=487
# 	 type=<class 'int'>, size=14, object=491
# 	 type=<class 'int'>, size=14, object=499
# 	 type=<class 'int'>, size=14, object=503
# 	 type=<class 'int'>, size=14, object=509
# 6556

#  на бОльших данных разница уже не так сильна (6556) против 3076


