'''
Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
'''
import cProfile

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

# -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.erathosphen_sieve(10)"
# 1000 loops, best of 5: 3.1 usec per loop

#  -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.erathosphen_sieve(100)"
# 1000 loops, best of 5: 28.6 usec per loop

# -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.erathosphen_sieve(1000)"
# 1000 loops, best of 5: 330 usec per loop

# cProfile.run('erathosphen_sieve(10000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.158    0.158   12.743   12.743 <string>:1(<module>)
#         1   10.682   10.682   12.586   12.586 les4_task2a.py:12(erathosphen_sieve)
#         1    0.901    0.901    0.901    0.901 les4_task2a.py:13(<listcomp>)
#         1    1.002    1.002    1.002    1.002 les4_task2a.py:22(<listcomp>)
#         1    0.000    0.000   12.743   12.743 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Алгоритм работает приблизительно за O(n). Т.к. при увеличении количества элементов в 10 раз на каждый запуск
#  время выполнения увеличивается приблизительно в 10 раз.



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

# python -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.prime(100)"
# 1000 loops, best of 5: 22.3 usec per loop

# -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.prime(1000)"
# 1000 loops, best of 5: 362 usec per loop

# cProfile.run('prime(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    4.340    4.340 <string>:1(<module>)
#         1    4.327    4.327    4.339    4.339 les4_task2a.py:56(prime)
#         1    0.000    0.000    4.340    4.340 {built-in method builtins.exec}
#     78497    0.013    0.000    0.013    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


from math import sqrt

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

# python -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.prime1(10)"
# 1000 loops, best of 5: 3.57 usec per loop

# python -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.prime1(100)"
# 1000 loops, best of 5: 51.6 usec per loop

# python -m timeit -n 1000 -s "import les4_task2a" "les4_task2a.prime1(1000)"
# 1000 loops, best of 5: 759 usec per loop

# cProfile.run('prime1(1000000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001   12.447   12.447 <string>:1(<module>)
#         1    8.468    8.468   12.446   12.446 les4_task2a.py:79(prime1)
#         1    0.000    0.000   12.447   12.447 {built-in method builtins.exec}
#  13251251    3.966    0.000    3.966    0.000 {built-in method math.sqrt}
#     78497    0.012    0.000    0.012    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}