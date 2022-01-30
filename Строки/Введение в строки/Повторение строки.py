"""
ПОВТОРЕНИЕ СТРОКИ
Напишите программу repeat.py, которая получает из первого аргумента командной строки слово, а из второго число N,
а после повторяет полученное слово N раз.

Пример использования:
> python repeat.py AA 5
> AAAAAAAAAA
"""

import sys

word = sys.argv[1]
num = sys.argv[2]

print(word * int(num))
