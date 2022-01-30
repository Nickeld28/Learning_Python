"""
НЕЧЕТНЫЕ И ЧЕТНЫЕ
Напишите программу, которая получает из первого аргумента командной строки строку вида "aAbBcCdDeEfFgG".
Далее программа должна преобразовать исходные данные в строку вида "abcdefgABCDEFG" и вывести результат.
То есть сперва нужно поставить символы, которые стоят на нечетных позициях, а затем на четных.

Пример использования:
> python program.py aAbBcCdDeEfFgG
> abcdefgABCDEFG
"""

import sys

string = sys.argv[1]
print(string[::2] + string[1::2])
