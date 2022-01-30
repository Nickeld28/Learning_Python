"""
Рекурсия
"""


def matryoshka(n):
    if n == 1:  # важно определить сразу крайний случай рекурсии
        print("Матрешечка")
    else:
        print("Верх матрешки n =", n)
        matryoshka(n - 1)
        print("Низ матрешки n =", n)


import graphics as gr

window = gr.GraphWin("Testing graphics", 600, 600)
alpha = 0.1


def fractal_rectangle(A, B, C, D, deep=10):
    if deep < 1:
        return
    for M, N in (A, B), (B, C), (C, D), (D, A):
        gr.Line(gr.Point(*M), gr.Point(*N)).draw(window)
    A1 = (A[0] * (1 - alpha) + B[0] * alpha, A[1] * (1 - alpha) + B[1] * alpha)
    B1 = (B[0] * (1 - alpha) + C[0] * alpha, B[1] * (1 - alpha) + C[1] * alpha)
    C1 = (C[0] * (1 - alpha) + D[0] * alpha, C[1] * (1 - alpha) + D[1] * alpha)
    D1 = (D[0] * (1 - alpha) + A[0] * alpha, D[1] * (1 - alpha) + A[1] * alpha)
    fractal_rectangle(A1, B1, C1, D1, deep - 1)


def factorial(n: int):
    assert n >= 0, "Факториал отрицательного числа не определен в этой функции"
    if n == 0:
        return 1
    return factorial(n - 1) * n


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
        return gcd(a - b, b)
    else:  # a < b
        return gcd(a, b - a)


def gcd_2(a, b):
    """Функция возвращает наибольший общий делитель  a и b"""
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def gcd_3(a, b):
    return (a if b == 0 else gcd(b, a % b))


"""
Быстрое возведение в степень
Степень можно представить так: a ** n = (a ** (n - 1)) * a
А можно и так a ** n = (a ** 2) ** (n / 2)
"""


def pow_simple(a: float, n: int):
    """Простейший алгоритм возведения в степень с рекурсией"""
    if n == 0:
        return 1
    return pow_simple(a, n - 1) * a


def pow(a: float, n: int):
    """Функция быстрого возведения числа a в степень n"""
    if n == 0:
        return 1
    elif n % 2 == 1:  # нечетная степень
        return pow(a, n - 1) * a
    else:  # четная степень
        return pow(a ** 2, n // 2)


"""
Алгоритм решения задачи Ханойские башни
"""


def towers_of_hanoy(n, pin1, pin2):
    """Функиия для решения задачи Ханойские башни"""
    if n == 1:
        print(f'Переложить диск 1 со стержня {pin1} на {pin2}')
    else:
        towers_of_hanoy(n - 1, pin1, 6 - pin1 - pin2)
        print(f'Переложить диск {n} со стержня {pin1} на {pin2}')
        towers_of_hanoy(n - 1, 6 - pin1 - pin2, pin2)


""" Тестирование """
if __name__ == "__main__":
    matryoshka(5)

    fractal_rectangle((100, 100), (500, 100), (500, 500), (100, 500), 50)
    window.getMouse()
    window.close()

    print(factorial(18))
    print(pow(999, 100))
    n = int(input('Введите количество дисков:\n'))
    towers_of_hanoy(n, 1, 2)
