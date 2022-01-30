"""
В прошлом задании мы выводили расширение файла, а теперь давайте печатать его имя.

Напишите программу, которая первым аргументом командной строки принимает имя файла вместе с расширением,
а после выводит только его имя. Для удобства будем считать, что все расширения состоят из трех символов.

Пример использования в командной строке Windows:
> python program.py my_car.png
> my_car
"""

import sys

file_name = sys.argv[1]
print(file_name[:-4])
