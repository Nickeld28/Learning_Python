# ФАМИЛИЯ ИМЯ ОТЧЕСТВО
# Напишите программу, которая принимает три аргумента командной строки: фамилию, имя и отчество, а затем выводит их в правильной форме: первая буква заглавная, остальные строчные.
#
# Пример использования:
# > python program.py иванов иван иванович
# > Иванов Иван Иванович
# Подсказка:
# Воспользуйтесь методом capitalize.

import sys

first_name = sys.argv[1]
last_name = sys.argv[2]
third_name = sys.argv[3]

print(first_name.capitalize(), last_name.capitalize(), third_name.capitalize(), sep=" ")
