# МЕНЯЕМ ЗАГОЛОВОК
# В прошлом задании вы научились определять содержание H1-заголовка, теперь надо его изменить.
#
# Напишите программу, которая получает из первого аргумента командной строки HTML-текст, а из второго параметра
# значение для заголовка. После программа должна заменить содержание <H1>-заголовка на полученное значение.
#
# Пример использования в командной строке Windows:
# > python program.py "<p>текст</p><h1>Заголовок</h1><p>еще текст</p>" "Главный"
# > <p>текст</p><h1>Главный</h1><p>еще текст</p>

import sys

html_text = sys.argv[1]
h1 = sys.argv[2]

h1_start = html_text.find("<h1>")
h1_end = html_text.find("</h1")
text_before = html_text[:h1_start + 4]
text_after = html_text[h1_end:]

print(text_before + h1 + text_after)
