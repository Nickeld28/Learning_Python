"""
Выводим словарь
Необходимо вывести все значения представленного словаря в следующем формате:

ключ - значение

Каждая отдельная пара ключ - значение выводится на отдельной строке,
попробуйте решить эту задачу, используя метод items().

Sample Input:
{"dish1": "med", "dish2": "pirog", "dish3": "plov"}

Sample Output:
dish1 - med
dish2 - pirog
dish3 - plov

"""

example_dict = {"dish1": "med", "dish2": "pirog", "dish3": "plov"}
for k, v in example_dict.items():
    print(k, '-', v)
