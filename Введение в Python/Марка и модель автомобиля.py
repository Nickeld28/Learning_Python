"""
Напишите программу, которая получает из аргументов командной строки два аргумента:
марку и модель автомобиля, а после выводит на экран фразу "Автомобиль: <марка> <модель>".

Пример использования в командной строке Windows:
> python auto.py Honda Accord
> Автомобиль: Honda Accord
"""

import sys

mark = sys.argv[1]
model = sys.argv[2]
print("Автомобиль:", mark, model)
