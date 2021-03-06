""" Квадратичные сортировки O(N^2)"""


def insert_sort(A):
    """Функция сортировки элементов списка, Алгоритм сортировки вставками"""
    n = len(A)
    for top in range(1, n):
        k = top
        while k > 0 and A[k - 1] > A[k]:
            A[k], A[k - 1] = A[k - 1], A[k]
            k -= 1


def choise_sort(A):
    """Функция сортировки элементов списка, Алгоритм сортировки выбором"""
    n = len(A)
    for pos in range(0, n - 1):
        for k in range(pos + 1, n):
            if A[k] < A[pos]:
                A[k], A[pos] = A[pos], A[k]


def buble_sort(A):
    """Функция сортировки элементов списка, Алгоритм сортировки методом пузырька"""
    n = len(A)
    for bypass in range(1, n):
        for k in range(0, n - bypass):
            if A[k] > A[k + 1]:
                A[k], A[k + 1] = A[k + 1], A[k]


""" Линейная сортировки O(N * log N)"""


def counting_sort(A):
    """Функция сортировки элементов списка, Алгоритм сортировки методом подсчета"""
    min_value = min(A)
    max_value = max(A)
    counters = [0 for i in range(max_value - min_value + 1)]
    for element in A:
        counters[element - min_value] += 1
    index = 0
    for i in range(len(counters)):
        for counter in range(counters[i]):
            A[index] = i + min_value
            index += 1
    return None


def test_sort(sort_algorithm):
    print('Тестируем:', sort_algorithm.__doc__)
    print("testcase #1:", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'FAIL')

    print('Тестируем:', sort_algorithm.__doc__)
    print("testcase #2:", end="")
    A = list(range(10, 20)) + list(range(0, 10))
    A_sorted = list(range(0, 20))
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'FAIL')

    print('Тестируем:', sort_algorithm.__doc__)
    print("testcase #3:", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print('OK' if A == A_sorted else 'FAIL')


if __name__ == '__main__':
    test_sort(insert_sort)
    test_sort(choise_sort)
    test_sort(buble_sort)
    test_sort(counting_sort)
