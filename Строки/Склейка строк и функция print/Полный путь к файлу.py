"""
Полный путь до файлов в операционной системе WIndows начинается с имени диска, затем следуют каталоги разделенные
обратным слешем и замыкает последовательность целевой файл: C:\Catalog1\catalog2\file.ext

Программа ниже принимает из аргументов командной строки 4 переменные: диск, два каталога и имя файла.
Используя склейку строк, сформируйте полный путь до файла в системе Windows и выведите результат.

Обратите внимание, что обратный слеш в Python имеет особое значение при использовании в строках.
Чтобы добавить в строку один обратный слеш, нужно написать его два раза:
Прямой слеш
print("catalog1/catalog2/task.py")
catalog1/catalog2/task.py

Обратный слеш
print("catalog1\\catalog2\\task.py")  # Указываем по два слеша - выводится один.
catalog1\catalog2\task.py

Пример использования в командной строке Windows:
> python program.py D sources python task.py
> D:\sources\python\task.py
"""

import sys

# Принимаем данные и сохраняем их в переменных disk, catalog1, catalog2, filename
disk, catalog1, catalog2, filename = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

print(disk + ':', catalog1, catalog2, filename, sep="\\")
