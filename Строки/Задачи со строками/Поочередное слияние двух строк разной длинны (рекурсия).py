"""
Прочитайте две строки и создайте список, в котором будут чередоваться символы из первой и второй строк.

Строки, которые подаются на вход в этой задаче, могут быть разной длины. Если строки разные,
то в конце будут выводится подряд символы более длинной строки.

Sample Input 1:
hello
python

Sample Output 1:
['h', 'p', 'e', 'y', 'l', 't', 'l', 'h', 'o', 'o', 'n']

Sample Input 2:
mouse
cat

Sample Output 2:
['m', 'c', 'o', 'a', 'u', 't', 's', 'e']
"""


def merge_sym(a_lst: list, b_lst: list):
    """Принимает два списка в качестве аргументов, возвращает результирующий список, созданный
       поочередным слиянием элементов списка. Рекурсия"""
    global result
    if len(a_lst) == 0:  # крайний случай рекурсии
        result.extend(b_lst)
        return result
    if len(b_lst) == 0:  # крайний случай рекурсии
        result.extend(a_lst)
        return result
    result.append(a_lst.pop(0))
    result.append(b_lst.pop(0))
    return merge_sym(a_lst, b_lst)  # рекуррентный вызов


a, b, result = [i for i in input()], [i for i in input()], []
print(merge_sym(a, b))
