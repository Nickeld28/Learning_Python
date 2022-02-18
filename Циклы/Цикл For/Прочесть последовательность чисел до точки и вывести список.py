"""
Вам подается на вход последовательность целых чисел, в которой каждое число идет на новой строке.
Заканчивается последовательность точкой.

Прочитайте такую последовательность и выведите список, содержащий её элементы.

Поэтому попробуйте решить эту задачу, использовав только один вызов функции input().

Sample Input 1:
1
2
3
.

Sample Output 1:
[1, 2, 3]

Sample Input 2:
.

Sample Output 2:
[]
"""

print([int(i) for i in iter(input, '.')])
