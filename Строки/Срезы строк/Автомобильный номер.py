"""
Напишите программу, которая принимает первым аргументом командной строки полный автомобильный номер,
а после выводит его регистрационный номер:

Пример использования в командной строке Windows:
> python program.py c065mk78
> 065
"""

import sys

sign = sys.argv[1]
print(sign[1:4])
