"""
Создайте программу, которая получает из первого аргумента командной строки имя ученика,
а после выводит на экран фразу "Hello <ученик>".

Где <ученик> — это имя, которое было передано первым аргументом командной строки.

Чтобы получить в программе аргументы (параметры) командной строки, нужно добавить в её начало такой код:

import sys
name = sys.argv[1]
Тогда передаваемый аргумент (имя ученика), будет храниться в переменой name.
Подробнее как решить эту задачу вы можете посмотреть в уроке Решение задач.

Пример использования в командной строке Windows:
> python hello_user.py Nikita
> Hello Nikita
"""

import sys

name = sys.argv[1]
print("Hello,", name)
print("Hello,", input())

# > python Hello, User!.py Nikolay
# > Hello Nikolay
