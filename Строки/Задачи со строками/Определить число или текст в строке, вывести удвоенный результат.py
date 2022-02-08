"""
Прочитайте строку. Если это положительное целое число, то умножьте его на два.
Если это любая другая строка, то повторите её два раза.

Sample Input 1:
asdf

Sample Output 1:
asdfasdf

Sample Input 2:
21

Sample Output 2:
42

Sample Input 3:
2d

Sample Output 3:
2d2d

Sample Input 4:
3 3

Sample Output 4:
3 33 3
"""

s = input()
print(int(s) * 2 if s.isdigit() else s * 2)
