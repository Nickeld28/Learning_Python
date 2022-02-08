"""
Прочитайте строку состоящую из цифр.
Превратите её в список чисел, каждое число в котором будет цифрой из строки.
Посчитайте среднее арифметическое все чисел в списке.

Sample Input 1:
123

Sample Output 1:
2.0

Sample Input 2:
1

Sample Output 2:
1.0
"""

strng = input()
lst = list(map(int, strng))
result = sum(lst) / len(strng)
print(result)
