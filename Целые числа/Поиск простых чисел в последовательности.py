"""
Задано целое положительное число n.
Найдите все простые числа в диапазоне от 2 до n включительно.
Числа нужно вывести в одну строку, в порядке возрастания и разделив их пробелом.

Sample Input 1:

6
Sample Output 1:

2 3 5
Sample Input 2:

20
Sample Output 2:

2 3 5 7 11 13 17 19
Sample Input 3:

40
Sample Output 3:

2 3 5 7 11 13 17 19 23 29 31 37
"""

n = int(input())
list_simple = []
for i in range(2, n + 1):
    d = 0
    for j in range(2, i):
        if i % j == 0:
            d += 1
    if d == 0:
        list_simple.append(i)
print(*list_simple)
