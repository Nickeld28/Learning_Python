"""
МЕНЯЕМ РЕГИСТР
Напишите программу, которая получает из первого аргумента командной строки слово,
а после заменяет в нем заглавные буквы на строчные и наоборот.

Пример использования:
> python swapcase.py Python
> pYTHON
Подсказка:
Используйте метод swapcase.
"""

import sys

name = sys.argv[1]
print(name.swapcase())
