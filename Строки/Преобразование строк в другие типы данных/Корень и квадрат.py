"""
КОРЕНЬ И КВАДРАТ
Напишите программу, которая первым аргументом командной строки принимает целое число,
а после выводит квадратный корень из этого числа, само число и число возведенное в квадрат.
Все значения должны быть разделены точкой с запятой.

Пример использования:
> python program.py 81
> 9;81;6561
"""

import sys

num = int(sys.argv[1])
print(int(num ** 0.5), num, num * num, sep=";")
