"""
В прошлый раз мы сжимали строки, используя кодирование повторов.
Теперь нашей задачей будет восстановление исходной строки обратно.

Напишите программу, которая считывает из файла строку, соответствующую тексту,
сжатому с помощью кодирования повторов, и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.


Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb
"""

s = 'i2V6q9Z4m18Y5q17A15I7z19R18T13Q17n17B13r6K6y5e5l8n10t10H2i5f12q7D13b19'


def get_list_str_and_int_from_one_string(string):
    string += ' '
    lst = []
    for i in range(0, len(string)):
        if not string[i].isdigit():
            lst.append((string[i]))
        else:
            if string[i - 1].isdigit():
                continue
            tmp = string[i]
            for j in range(i + 1, len(string)):
                if string[j].isdigit():
                    tmp += string[j]
                else:
                    lst.append(int(tmp))
                    break
    lst.pop()
    return lst


def get_aaabbc_from_a3b2c1(lst_1):
    list_result = []
    for i in range(0, len(lst_1) - 1, 2):
        list_tmp = [lst_1[i], lst_1[i + 1]]
        list_result.append(tuple(list_tmp))
    for i in range(0, len(list_result)):
        print(list_result[i][0] * list_result[i][1], sep='', end='')


get_aaabbc_from_a3b2c1(get_list_str_and_int_from_one_string(s))
