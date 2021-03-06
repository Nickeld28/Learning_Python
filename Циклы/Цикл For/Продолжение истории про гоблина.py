"""
Продолжение истории про гоблина
Гоблин решил не останавливаться на достигнутом и продолжать совершенствовать свои навыки,
поэтому вскоре он также научился кричать несколькими волнами сразу,
а также использовать в своих криках различные символы. На вход программе подаются три значения,
первое - количество криковых волн, которое нужно создать, второе - пик криковых волн и третье - символ,
которым кричит гоблин. В результате необходимо вывести заданное количество криковых волн,
построенных по введенным параметрам.

Sample Input:
2
3
A

Sample Output:
A
AA
AAA
AA
A
A
AA
AAA
AA
A
"""

count, high, sym = int(input()), int(input()), input()
for i in range(count):
    for j in range(1, (high * 2)):
        print(sym * j if j <= high else sym * (2 * high - j))
