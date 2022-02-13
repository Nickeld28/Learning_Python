"""
Дан список содержащий последовательность различных элементов, разного типа.
Сохраняя порядок элементов очистить список от всех элементов, которые не являются целыми числами, не равны нулю или 25.
А затем преобразовать все числа в строки и добавить букву 's'.

Sample Input 1:
lst = [1, 2, "word", 3, 25, 4, (4, 5), 4.5, 100, 5, {1: 's'}, 6, "sample", 7, 8, 8.2, 9, 10, None, 11, [], 12, 13, 0]

Sample Output 1:
['1s', '2s', '3s', '25s', '4s', '100s', '5s', '6s', '7s', '8s', '9s', '10s', '11s', '12s', '13s']
"""

pov = 0
lst = [1, 2, "word", 3, 25, 4, (4, 5), 4.5, 100, 5, {1: 's'}, 6, "sample", 7, 8, 8.2, 9, 10, None, 11, [], 12, 13, 0]
print(lst)
print(len(lst))
for i in lst:
    ind = lst.index(i)
    if not isinstance(i, int) or i == 0:
        lst.pop(ind)
        lst.insert(0, '#_$')
        pov += 1
        continue
    tmp = str(i) + 's'
    lst[ind] = tmp
del lst[0:pov]
print(lst)
print(len(lst))

