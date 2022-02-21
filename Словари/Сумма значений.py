"""
Сумма значений
Все элементы, лежащие по ключам в представленном словаре - числа.
Необходимо посчитать сумму всех элементов (внимание! ключи не нужно прибавлять к общей сумме)
и в результат вывести получившееся число.

Постарайтесь решить данную задачу в одну строку.

Sample Input:
{1: 24, 2: 29, 3: 12, 4: 13, 5: 89}

Sample Output:
167
"""

numbers_dict = {1: 24, 2: 29, 3: 12, 4: 13, 5: 89}
print(sum(numbers_dict.values()))
