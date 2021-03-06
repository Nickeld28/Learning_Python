"""
Напишите программу, которая принимает первым аргументом командной строки слово, а после выводит его в рамке.
Обратите внимание, что в примере использования справа и слева от слова стоят пробелы.

Пример использования в командной строке Windows:
> python program.py Programming
> +-------------+
> | Programming |
> +-------------+
"""

import sys

word = sys.argv[1]
print("+", "-" * (len(word) + 2), "+", sep="")
print("|", word, "|", sep=" ")
print("+", "-" * (len(word) + 2), "+", sep="")
