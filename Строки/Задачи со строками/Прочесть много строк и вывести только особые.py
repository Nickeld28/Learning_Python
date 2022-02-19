"""
Прочитайте до точки ('.') последовательность строк.
В каждой строке через пробел указано слово и индикатор 'true' или 'false'.
Выведите через пробел все слова с индикатором 'true', а на новой строке их количество.

Sample Input 1:
abc true
.

Sample Output 1:
abc
1

Sample Input 2:
abc false
.

Sample Output 2:


0
Sample Input 3:
abc true
def true
ghi false
gkl true
mno false
.

Sample Output 3:
abc def gkl
3
"""

lst = []
while True:
    s = input().split()
    if '.' in s:
        break
    elif 'true' in s:
        lst.append(s[0])
print(*lst)
print(len(lst))
