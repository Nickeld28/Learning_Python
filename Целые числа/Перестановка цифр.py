"""
Перестановка цифр
Дано трехзначное число abc, в котором все цифры различны. Напишите программу, которая выводит шесть чисел,
образованных при перестановке цифр заданного числа.

Формат входных данных
На вход программе подаётся положительное трёхзначное целое число, все цифры которого различны.

Формат выходных данных
Программа должна вывести шесть чисел, образованных при перестановке цифр заданного числа в следующем порядке:
abc, acb, bac, bca, cab, cba.

Тестовые данные
Sample Input 1:

123
Sample Output 1:

123
132
213
231
312
321
Sample Input 2:

987
Sample Output 2:

987
978
897
879
798
789
"""

num = int(input())
if len(str(num)) != 3 or num % 1 != 0:
    print('Ошибка ввода, введите трехзначное целое число')
else:
    _list = []
    for i in range(3, 0, -1):
        n = (num % 10 ** i) // 10 ** (i - 1)
        _list.append(n)
    _list.append('\n')
    var = [0, 1, 2, 3, 0, 2, 1, 3, 1, 0, 2, 3, 1, 2, 0, 3, 2, 0, 1, 3, 2, 1, 0]
    for i in var:
        print(_list[i], sep='', end='')
