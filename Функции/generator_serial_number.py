from random import randint, choice


def get_letters(count: int) -> str:
    """
     Генерирует случайную последовательность символов указанной длинны из имеющегося списка
    :param count: длинна последовательности (количество знаков)
    :return: случайная последовательность символов
    """
    series = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
              'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = ""
    for j in range(1, count + 1):
        letters += choice(series)
    return letters


def get_number(pair) -> str:
    """
    Генерирует случайное положительное число в указанном интервале, преобразует в строку, добавляет лидирующие нули
    :param pair: кортеж из пары целых чисел, означающих границы интервала включительно для генерации случайного числа
                 есть возможность принять одно целое число, тогда второе будет равно нулю автоматически
    :return: строку, состоящую из цифровых символов
    """
    if pair == (0, 0):
        return ""
    elif isinstance(pair, int):
        a, b = 0, pair
    else:
        a, b = pair
    a, b = abs(a), abs(b)
    if a > b:
        a, b = b, a
    number = randint(a, b)
    digits = len(str(b))
    str_number = str(number).zfill(digits)
    return str_number


def get_serial_number(number_letters: int, range_numbers=(0, 0), separator=''):
    """
     Герерирует серию и номер с гибкими параметрами
    :param number_letters: число букв в серии. 0 - отсутствие букв
    :param range_numbers: кортеж из пары целых чисел (границы интервала включительно для генерации случайного числа)
           есть возможность принять одно целое число, тогда второе будет равно нулю автоматически
    :param separator: любой символ - разделитель между серией и номером, по умолчанию - отсутствует
    :return: сгенерированный серийный номер
    """
    return get_letters(number_letters) + separator + get_number(range_numbers)
