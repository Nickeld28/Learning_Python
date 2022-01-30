"""
Через командную строку (или параметры PyCharm) можно передавать не один параметр, а сразу несколько.
Для этого их нужно разделить пробелом:

Пример в командной строке Windows:
> python hello_user.py Nikita Antonov

Напишите программу, которая получает из аргументов командной строки имя и фамилию ученика, а после выводит на экран фразу "Hello <имя> <фамилия>".

Пример использования в командной строке Windows:
> python hello_user.py Nikita Antonov
> Hello Nikita Antonov
"""

import sys

first_name = sys.argv[1]  # В first_name будет храниться Nikita
last_name = sys.argv[2]  # В last_name будет храниться Antonov
print("Hello", first_name, last_name)
