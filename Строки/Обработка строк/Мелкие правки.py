# МЕЛКИЕ ПРАВКИ
# Напишите программу, которая принимает первым аргументом командной строки телефонный номер в формате +7-111-222-33-44
# и меняет первые две черточки на пробелы.
#
# Пример использования:
# > python program.py +7-111-222-33-44
# > +7 111 222-33-44
# Подсказка:
# Используйте метод replace, его возможности чуть шире, чем мы рассмотрели в уроке.

import sys
phone = sys.argv[1]
phone = phone.replace("-", " ", 2)

print(phone)
