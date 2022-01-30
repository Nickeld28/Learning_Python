"""
Простейшая система проверки орфографии может быть основана на использовании списка известных слов.
Если введённое слово не найдено в этом списке, оно помечается как "ошибка".

Попробуем написать подобную систему.

На вход программе первой строкой передаётся количество d известных нам слов, после чего на d строках
указываются эти слова. Затем передаётся количество l строк текста для проверки, после чего l строк текста.

Выведите уникальные "ошибки" в произвольном порядке. Работу производите без учёта регистра.

Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
"""

word_count = int(input())
errors_list = []
word_list = [input().lower() for word in range(word_count)]
string_count = int(input())
for string in range(string_count):
    string_list = input().lower().split()
    for word in string_list:
        if word not in word_list:
            if word not in errors_list:
                errors_list.append(word)
print(*errors_list, sep='\n')
