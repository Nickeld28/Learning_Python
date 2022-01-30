# H1-ЗАГОЛОВОК
# Напишите программу, которая получает из первого аргумента командной строки HTML-текст, а после извлекает
# из него содержание <H1>-заголовка.
#
# Пример использования в командной строке Windows:
# > python program.py '<p>текст</p><h1>Заголовок</h1><p>еще текст</p>'
# > Заголовок

import sys
html_text = sys.argv[1]
h1_start = html_text.find("<h1>")
h1_end = html_text.find("</h1>")
print(html_text[h1_start + 4:h1_end])
