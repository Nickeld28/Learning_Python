"""
=============================
Динамическое программирование
=============================
"""


def fib(number):
    """
    Реккурентный алгоритм нахождения чисел Фибоначчи
    Обладает запредельной ассимптотикой O(fib n) и растет экспоненциально
    Каждое последующее число Фибоначчи вычисляется этим алгоритмом в 2 раза медленее предыдущего
    """
    if number <= 1:
        return number
    return fib(number - 1) + fib(number - 2)


"""
    Простой алгоритм нахождения чисел Фибоначчи
    Обладает линейной ассимптотикой O(n)
"""

n = 5  # найдем число Фибоначчи для n
fib_lst = [0, 1] + [0] * (n - 1)  # создадим пустой список нужного размера, заполнив первые два элемента
for i in range(2, n + 1):  # пробежимся по списку циклом
    fib_lst[i] = fib_lst[i - 1] + fib_lst[i - 2]  # и запишем в него числа Фибоначчи для каждого числа до n
print(fib_lst[n])  # после можем вывести любое число Фибоначчи из списка, до числа n включительно
#  значение элемента списка и есть число Фиббоначи нужного числа, а индекс элемента показывает для какого именно числа


"""
    Еще один простой алгоритм нахождения чисел Фибоначчи c обменом переменных значениями
    Обладает линейной ассимптотикой O(n)
"""
_number_ = 5
a, b = 0, 1
for _ in range(_number_):
    a, b = b, a + b
print(a)


"""
Кузнечик на числовой прямой
Кузнечик может прыгать +1 и +2 клетки
Вопрос: сколько различных траекторий попасти из клетки 1 в клетку n?

Конечная точка - n, в нее можно попасть либо из точки n - 1 прыжком +1 или из точки n - 2 прыжком +2.
Таким образом число способов попасть в клетку n составляет: Kn = Kn-2 + Kn-1
Если считать реккурентным способом, то можно нарваться на ассимптотику, аналогичную числам Фиббоначи.
Посчитаем спомощью списка:
"""


def trajectories_number(num):
    """ возвращает количество траекторий кузнечика из точки 1 в точку num на числовой прямой,
    кузнечик может прыгать +1 или +2 клетки.
    Создадим список k для подчсета количества траекторий.
    """
    k = [0, 1] + [0] * num
    for j in range(2, num + 1):
        k[j] = k[j - 2] + k[j - 1]
    return k[num]  # получившееся решение аналогично нахождению чисел Фиббоначи


"""
Кузнечик на числовой прямой - усложненная задача
Кузнечик может прыгать +1, +2 или + 3 клетки.
Запрещены некоторые клетки для посещения.
Вопрос: сколько различных траекторий попасти из клетки 1 в клетку n?

Как передать в интерфейс программы какие клетки разрешены, а какие запрещены для посещения?
Можно создать список логических значений (где True - разрешено, False - запрещено)
"""


def trajectories_number_hard_task(num: int, allowed: list):
    """ возвращает количество траекторий кузнечика из точки 1 в точку num_ на числовой прямой,
        кузнечик может прыгать +1, +2 или + 3 клетки. В списке allowed перечислены логические значения True или False,
        в зависимости от того, разрешено или запрещено наступать на эту клетку или нет. Индекс списка соответствует
        клетке на числовой оси. Создадим список m для подчсета количества траекторий.
    """
    m = [0, 1, int(allowed[2])] + [0] * (num - 3)
    for e in range(3, num + 1):
        if allowed[e]:
            m[e] = m[e - 1] + m[e - 2] + m[e - 3]
    return m[num]


"""
Кузнечик на числовой прямой - перемещение за минимальную стоимость.
Кузнечик может прыгать +1, +2 клетки.
За посещение каждой клетки x берется некоторая плата - price[x]
Вопрос: какова минимальная стоимость клетки n? Найти cost(n)
"""


def min_cost_count(num, price: list):
    """ возвращает минимальную стоимость перемещения кузнечика из точки 1 в точку num_ на числовой прямой,
        кузнечик может прыгать +1, +2 клетки. В списке price перечислены цены посещения клеток, а индексы списка
        соответствует клеткам на числовой оси. Создадим список count для подчсета количества траекторий.
    """
    # float('-inf') - специфическое состояние числа с плавающей точкой, означает - бесконечность
    count = [float('-inf'), price[1], price[1] + price[2]] + [0] * (num - 2)
    for cell in range(3, num + 1):
        count[cell] = price[cell] + min(count[cell - 1], count[cell - 2])
    return count(num)


"""
=================
Двумерные массивы
=================
Что бы получить элемент из  двумерного массива A, где N - число строк, а M - число элементов в строке
есть два способа:
1) Взять элемент Aij из линейного массива A, в котором N * M элементов вызвав A[i * M + j] - линеаризация массива
2) Создание списка списков.
Неправильная реализация:   A = [[0] * m] * n, каждая строка ссылка на первую строку! A[0] == A[1] и A[0] is A[1]
Правильная реализация: A = [[0] * M for i in range(N)]
В этом случае A[0] == A[1], но A[0] not is A[1]
"""