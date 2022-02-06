"""
Сделайте список чисел из строки так же как в предыдущей задаче.
Сделайте новый список с кумулятивной суммой чисел из исходной строки.

Sample Input:
12345

Sample Output:
[1, 3, 6, 10, 15]
"""

strng = input()
lst = [0]
for sym in strng:
    tmp = int(sym) + lst[-1]
    lst.append(tmp)
lst.pop(0)
print(lst)
