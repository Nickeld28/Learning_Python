"""
На вход программе подается какое-то количество слов, записанных в одной строке через пробел.
Если количество слов в строке четно, необходимо выбрать слова с индексами 0, 2, 4 и далее,
если же количество слов в строке нечетно - нужно взять только слова с индексами 1, 3, 5 и так далее.
Из выбранных слов нужно определить слово с максимальной длиной и вывести результирующую строку следующего вида:

*слово с максимальной длиной* -> длина = *длина данного слова*

Sample Input 1:

сырок вязание оксимирон пятка мюллер шакал
Sample Output 1:

оксимирон -> длина = 9
Sample Input 2:

плед плазмодий литораль варежка контаминация
Sample Output 2:

плазмодий -> длина = 9
"""

_list = input().split()
res_list = []
if (len(_list)) % 2 == 0:
    for i in len(_list):
        if i % 2 == 0:
            res_list.append(_list[i])
    else:
        if i % 2 != 0:
            res_list.append(_list[i])
print(*res_list)
