"""
Напишите программу, которая принимает первым аргументом командной строки слово, а после выводит его с подчеркиванием.
В качестве символа для подчеркивания используйте минус «-».

Пример использования в командной строке Windows:
> python program.py Programming
> Programming
> -----------
"""

import sys

word = sys.argv[1]
print(word, end="\n"), print(len(word) * "-")
