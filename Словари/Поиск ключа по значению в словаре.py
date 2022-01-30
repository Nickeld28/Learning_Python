"""
Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову.
Все слова в словаре различны.

Для слова из словаря, записанного в последней строке, определите его синоним.

Входные данные:

3
Hello Hi
Bye Goodbye
List Array
Goodbye
"""

# Мое костыльное решение:
n = int(input())
_list = [tuple(input().split()) for i in range(n)]
mydict = dict(_list)
name = input()
list1 = []
for elem in _list:
    list1.extend(elem)
print(list1)
if name in list1:
    print(list1[list1.index(name) - 1])

"""
интересные решения других участников:

d = {}
for i in range(int(input())):
   s = input().split()
   d[s[1]] = s[0]
print(d[input()])

A = dict()
for i in range(int(input())):
    s = input().split()
    A[s[0]] = s[1]

syn = input()

for key in A:
    if A[key] == syn:
        print(key)
"""
