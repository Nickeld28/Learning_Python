"""
РАСШИФРОВЫВАЕМ НОМЕР
Используя таблицу соответствий цифр буквам из прошлого урока, напишите программу, которая первым аргументом командной строки принимает зашифрованный телефонный номер, а затем дешифрует его и выводит результат.

Шифр из прошлго урока:

0 — a
1 — (пробел)
2 — b
3 — e
4 — l
5 — mu
6 — n
7 — o
8 — lee
9 — f
Обратите внимание, что номер телефона заканчивается точкой, которую шифровать не надо.

Пример использования:
> python program.py "leefmu lmunlee mun."
> 89514568156.
"""

import sys

phone = sys.argv[1]
phone = phone. \
    replace("lee", "8"). \
    replace("a", "0"). \
    replace(" ", "1"). \
    replace("b", "2"). \
    replace("e", "3"). \
    replace("l", "4"). \
    replace("mu", "5"). \
    replace("n", "6"). \
    replace("o", "7"). \
    replace("f", "9")

print(phone)
