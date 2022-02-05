"""
Прочитайте строку чисел, выведите эти числа в обратном порядке через пробел.

Sample Input:
8 11 1

Sample Output:
1 11 8
"""

lst = (input().split())
print(*reversed(lst))
