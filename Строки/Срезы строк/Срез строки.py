"""
На вход программе подаются на разных строках - какое-то количество слов, разделенных пробелом и число.
Необходимо вывести слова из данной строки до слова (включая) с индексом,
равным введенному числу в одну строку через пробел. Гарантируется,
что введенное число не превышает индекс последнего элемента строки.

Sample Input:

бусы елка кока-кола олень фотокарточка
3
Sample Output:

бусы елка кока-кола олень
"""

_list = input().split()
ind = int(input())
print(*_list[:ind + 1])
