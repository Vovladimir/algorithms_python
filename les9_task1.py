"""
1. Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных
подстрок в этой строке.

Примечания:
* в сумму не включаем пустую строку и строку целиком;
* без использования функций для вычисления хэша (hash(), sha1() или любой
другой из модуля hashlib задача считается не решённой.
"""

from hashlib import sha1


def substr_count(string: str):
    str_length = len(string)
    assert str_length > 0, "Строка не может быть пустой"

    is_counted = [
        string
    ]
    substrings = {}

    # формируем подстроки
    for pos in range(str_length):
        for width in range(pos + 1, str_length + 1):
            subs = string[pos:width]
            if subs not in is_counted and subs not in substrings:
                substrings[subs] = 0

    for patt in substrings:
        patt_length = len(patt)
        patt_hash = sha1(patt.encode("utf-8")).hexdigest()
        for i in range(str_length - patt_length + 1):
            subs_hash = sha1(string[i:i + patt_length].encode("utf-8")).hexdigest()
            if subs_hash == patt_hash:
                substrings[patt] += 1

    return substrings, f' Количество подстрок = {sum(x for x in substrings.values())}'


s = input("Введите строку: ")

result = substr_count(s)
print(result)