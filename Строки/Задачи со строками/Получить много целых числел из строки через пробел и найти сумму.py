"""
Прочитайте несколько целых чисел разделенных пробелом, выведите их сумму.

Sample Input 1:
8 11 1

Sample Output 1:
20

Sample Input 2:
47 64 -96 -50 26 -59 -85 87 95

Sample Output 2:
29
"""

print(sum(map(int, input().split())))