"""
Арифметические операции
Напишите программу, в которой вычисляется сумма, разность и произведение двух целых чисел, введенных с клавиатуры.

Формат входных данных
На вход программе подаётся два целых числа, каждое на отдельной строке.

Формат выходных данных
Программа должна вывести сумму, разность и произведение введённых чисел, каждое на отдельной строке.

Тестовые данные
Sample Input 1:

2
7
Sample Output 1:

2 + 7 = 9
2 - 7 = -5
2 * 7 = 14
Sample Input 2:

5
8
Sample Output 2:

5 + 8 = 13
5 - 8 = -3
5 * 8 = 40
Sample Input 3:

10
10
Sample Output 3:

10 + 10 = 20
10 - 10 = 0
10 * 10 = 100
"""
a, b = int(input()), int(input())
print(str(a), '+', str(b), '=', a + b)
print(str(a), '-', str(b), '=', a - b)
print(str(a), '*', str(b), '=', a * b)
