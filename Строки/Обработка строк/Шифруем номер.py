# ШИФРУЕМ НОМЕР
# Напишите программу, которая принимает первым аргументом командной строки телефонный номер,
# а затем шифрует его и выводит результат.
#
# Программа использует простой шифр, заменяя цифры номера на буквы или сочетания букв:
#
# 0 — a
# 1 — (пробел)
# 2 — b
# 3 — e
# 4 — l
# 5 — mu
# 6 — n
# 7 — o
# 8 — lee
# 9 — f
# Обратите внимание, что номер телефона заканчивается точкой, которую шифровать не надо.
#
# Пример использования:
# > python program.py 89514568156.
# > leefmu lmunlee mun.

import sys
phone = sys.argv[1]
phone = phone. \
    replace("0", "a"). \
    replace("1", " "). \
    replace("2", "b"). \
    replace("3", "e"). \
    replace("4", "l"). \
    replace("5", "mu"). \
    replace("6", "n"). \
    replace("7", "o"). \
    replace("8", "lee"). \
    replace("9", "f")

print(phone)
