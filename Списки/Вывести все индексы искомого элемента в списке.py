"""
Напишите программу, которая считывает список чисел lst из первой строки и число xx из второй строки,
которая выводит все позиции, на которых встречается число xx в переданном списке lst.

Позиции нумеруются с нуля, если число x не встречается в списке,
вывести строку "Отсутствует" (без кавычек, с большой буквы).

Позиции должны быть выведены в одну строку, по возрастанию абсолютного значения.

Sample Input 1:
5 8 2 7 8 8 2 4
8

Sample Output 1:
1 4 5

Sample Input 2:
5 8 2 7 8 8 2 4
10

Sample Output 2:
Отсутствует
"""

lst = [int(i) for i in input().split()]
x = int(input())
result = []
if x not in lst:
    print('Отсутствует')
for elem in enumerate(lst):
    if x == elem[1]:
        result.append(elem[0])
print(*result)

# Можно еще так
lst = [i for i in input().split()]
n, result = input(), []
for i, elem in enumerate(lst):
    if elem == n:
        result.append(i)
print(*result if result else ['Отсутствует'])
