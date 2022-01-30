"""
Создайте две переменные: first_name и last_name. Переменной first_name присвойте строку с вашим именем,
а в last_name поместите фамилию.

Выведите с помощью print на экран строку вида «Фамилия И.» (без кавычек), где И – первая буква вашего имени.
"""

first_name = 'Nikolay'
last_name = 'Dobrodey'
third_name = 'Anatolevich'

print(last_name, first_name[0] + "." + third_name[0], end='.\n')
