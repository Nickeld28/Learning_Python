"""
Снова видоизменяем словарь
На вход программе подается словарь, полностью состоящий из чисел (и ключи, и элементы являются числами,
причем ключи являются числами от 1 до какого-то числа с разницей между соседними ключами в 1).
Необходимо каждый элемент словаря умножить на ключ следующего за данным элемента,
а последнему элементу словаря присвоить значение 0. Например, если у нас есть следующий словарь:

 {ключ1: элемент1, ключ2: элемент2}, тогда

элемент1 = элемент1 * ключ 2

ключ2 = 0

В результате необходимо вывести получившийся словарь целиком.

Sample Input:
{1: 23, 2: 17, 3: 89}

Sample Output:
{1: 46, 2: 51, 3: 0}
"""

dictionary = {1: 23, 2: 17, 3: 89}
L = len(dictionary)
for i in range(L):
    print(i)
    if i == L - 1:
        dictionary[i + 1] = 0
    else:
        dictionary[i + 1] *= i + 2
print(dictionary)

