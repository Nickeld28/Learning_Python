"""
Три последовательных числа
Напишите программу вывода на экран трех последовательно идущих чисел, каждое на отдельной строке.
Первое число вводит пользователь, остальные числа вычисляются в программе.

Формат входных данных
На вход программе подается одно целое число.

Формат выходных данных
Программа должна вывести три последовательно идущих числа в соответствии с условием задачи.

Тестовые данные
Sample Input 1:

8
Sample Output 1:

8
9
10
Sample Input 2:

-341
Sample Output 2:

-341
-340
-339
Sample Input 3:

-1
Sample Output 3:

-1
0
1
"""

num = int(input())
print(num, num + 1, num + 2, sep='\n')
