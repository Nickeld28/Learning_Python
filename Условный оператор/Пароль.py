"""
Пароль
При регистрации на сайтах требуется вводить пароль дважды. Это сделано для безопасности,
поскольку такой подход уменьшает возможность неверного ввода пароля.

Напишите программу, которая сравнивает пароль и его подтверждение. Если они совпадают, то программа выводит:
«Пароль принят», иначе: «Пароль не принят».

Формат входных данных
На вход программе подаются две строки.

Формат выходных данных
Программа должна вывести одну строку в соответствии с условием задачи.

Тестовые данные
Sample Input 1:

qwerty
qwerty
Sample Output 1:

Пароль принят
Sample Input 2:

qwerty
Qwerty
Sample Output 2:

Пароль не принят
Sample Input 3:

PythonROCKS
PythonROCKS
Sample Output 3:

Пароль принят
"""

pass1 = input()
pass2 = input()
if pass1 == pass2:
    print('Пароль принят')
else:
    print('Пароль не принят')
