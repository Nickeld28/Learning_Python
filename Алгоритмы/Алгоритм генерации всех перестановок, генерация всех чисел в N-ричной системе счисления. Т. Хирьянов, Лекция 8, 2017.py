"""
Генерация всех перестановок

Из комбинаторики известно что в массиве N  число перестановок будет N факториал (N!)

Рассмотрим для начала простой случай, сгенерируем все возможные числа в N-ричной системе исчесления где N <= 10

Найдем все числа от 0...0 до N-1...N-1
"""


def generate_number(n: int, m: int, prefix=None):  #
    """ Функция генерирует все числа c лидирующими нулями из всех цифр системы счисления (N <= 10),
        в качестве аргуметов получаем уже сгенерированную часть числа - prefix (по умолчанию None - т.к. нет ничего),
        N - основание N-ричной системы счисления, М - количество цифр в числе (длинна числа)
    """
    if m == 0:
        print(prefix)  # выводит список [ ... ], а если нужны числа без провелов пишем print(*prefix, sep='')
        return
    prefix = prefix or []
    for digit in range(n):
        prefix.append(digit)
        generate_number(n, m - 1, prefix)
        prefix.pop()


def generate_bin(m, prefix=""):
    """ Функция генерирует все числа c лидирующими нулями из всех цифр двоичной системы счисления
    """
    if m == 0:
        print(prefix)
    else:
        generate_bin(m - 1, prefix + '0')
        generate_bin(m - 1, prefix + '1')


def generate_bin_in_cycle(m, prefix=""):
    """ Функция генерирует все числа c лидирующими нулями из всех цифр двоичной системы счисления,
        но только с использованием цикла
    """
    if m == 0:
        print(prefix)
        return
    for digit in '0', '1':
        generate_bin(m - 1, prefix + digit)


def find_number(number, lst):
    """ Функция ищет number в lst и возвращает True, если такое есть
        False, если такого нет
    """
    flag = False
    for x in lst:
        if number == x:
            flag = True
            break
    return flag


def generate_permutations(n: int, m: int = -1, prefix=None):
    """ Функция генерирует все перестановки N чисел в M позициях,
        с префиксом prefix
    """
    m = m if m != -1 else n  # по умолчанию N чисел в N позициях
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return
    for number in range(1, n + 1):
        if find_number(number, prefix):
            continue
        prefix.append(number)
        generate_permutations(n, m - 1, prefix)
        prefix.pop()

""" Тестирование """
if __name__ == "__main__":
    m = 2
    print(f"Генерируем все числа в бинарной СС длинной {m}:")
    generate_bin(m)
    print('Завершено успешно')

    m = 2
    n = 4
    print(f"Генерируем все числа в n-ричной СС, где n = {4} длинной {m}:")
    generate_number(n, m)
    print('Завершено успешно')

    m = -1
    n = 4
    print(f"Генерируем все перестановки {4} чисел в {m} позициях:")
    generate_permutations(n, m)
    print('Завершено успешно')