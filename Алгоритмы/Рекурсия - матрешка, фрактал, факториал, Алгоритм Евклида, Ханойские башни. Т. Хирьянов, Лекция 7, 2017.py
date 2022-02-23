"""
Рекурсия
"""
import graphics as gr


def matryoshka(c):
    if c == 1:  # важно определить сразу крайний случай рекурсии
        print("Матрешечка")
    else:
        print("Верх матрешки n =", c)
        matryoshka(c - 1)
        print("Низ матрешки n =", c)


window = gr.GraphWin("Testing graphics", 600, 600)
alpha = 0.1


def fractal_rectangle(a, b, c, d, deep=10):
    if deep < 1:
        return
    for M, N in (a, b), (b, c), (c, d), (d, a):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    a1 = (a[0] * (1 - alpha) + b[0] * alpha, a[1] * (1 - alpha) + b[1] * alpha)
    b1 = (b[0] * (1 - alpha) + c[0] * alpha, b[1] * (1 - alpha) + c[1] * alpha)
    c1 = (c[0] * (1 - alpha) + d[0] * alpha, c[1] * (1 - alpha) + d[1] * alpha)
    d1 = (d[0] * (1 - alpha) + a[0] * alpha, d[1] * (1 - alpha) + a[1] * alpha)
    fractal_rectangle(a1, b1, c1, d1, deep - 1)


def factorial(number: int):
    assert number >= 0, "Факториал отрицательного числа не определен в этой функции"
    if number == 0:
        return 1
    return factorial(number - 1) * number


"""
Алгоритм Евклида
нахождение наибольшего общего делителя у числа а и b
НОД(а, b) = НОД(а - b, b)

Три функции ниже идентичны, разница только в краткости записи кода
"""


def gcd_1(a, b):
    """Функция возвращает наибольший общий делитель  a и b"""
    if a == b:
        return a
    elif a > b:
        return gcd_1(a - b, b)
    else:  # a < b
        return gcd_1(a, b - a)


def gcd_2(a, b):
    """Функция возвращает наибольший общий делитель  a и b"""
    if b == 0:
        return a
    else:
        return gcd_2(b, a % b)


def gcd_3(a, b):
    return a if b == 0 else gcd_3(b, a % b)


"""
Быстрое возведение в степень
Степень можно представить так: a ** n = (a ** (n - 1)) * a
А можно и так a ** n = (a ** 2) ** (n / 2)
"""


def pow_simple(a: float, x: int):
    """Простейший алгоритм возведения в степень с рекурсией"""
    if x == 0:
        return 1
    return pow_simple(a, x - 1) * a


def power(k: float, m: int):
    """Функция быстрого возведения числа a в степень n"""
    if m == 0:
        return 1
    elif m % 2 == 1:  # нечетная степень
        return power(k, m - 1) * k
    else:  # четная степень
        return power(k ** 2, m // 2)


"""
Алгоритм решения задачи Ханойские башни
"""


def towers_of_hanoy(num, pin1, pin2):
    """Функиия для решения задачи Ханойские башни"""
    if num == 1:
        print(f'Переложить диск 1 со стержня {pin1} на {pin2}')
    else:
        towers_of_hanoy(num - 1, pin1, 6 - pin1 - pin2)
        print(f'Переложить диск {num} со стержня {pin1} на {pin2}')
        towers_of_hanoy(num - 1, 6 - pin1 - pin2, pin2)


# еще вариант реализации алгоритма Ханойские башни:
def hanoi(height, start=1, target=3, helper=2):
    """Функиия для решения задачи Ханойские башни"""

    def move(fp, tp):
        print('{} - {}'.format(fp, tp))

    if height >= 1:
        hanoi(height - 1, start, helper, target)
        move(start, target)
        hanoi(height - 1, helper, target, start)


""" Тестирование """
if __name__ == "__main__":
    matryoshka(5)

    fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 50)
    window.getMouse()
    window.close()

    print(factorial(18))
    print(power(99, 10))
    n = int(input('Введите количество дисков:\n'))
    towers_of_hanoy(n, 1, 2)
    hanoi(n, 1, 3)
