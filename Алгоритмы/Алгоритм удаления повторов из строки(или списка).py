"""
 Дана строка, нужно убрать из неё повторяющие символы.

Не используйте множества (set).

Sample Input:

abracadabra
Sample Output:

abrcd
"""

_list = list(input())
res_list = []
for i in _list:
    if i not in res_list:
        res_list.append(i)
print(*res_list, sep='')

"""
из строки можно так
s = input()
n = ''
for i in s:
   if i not in n:
       n += i
print(n)
"""
