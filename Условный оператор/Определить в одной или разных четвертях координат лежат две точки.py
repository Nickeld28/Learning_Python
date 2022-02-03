"""
Напишите программу, которая считывает координаты двух точек
и определяет лежат ли эти точки в одной координатной четверти.
Ни одна из координат не равна нулю.

В качестве результата выведите "YES" или "NO" (заглавными буквами, без кавычек).

Sample Input:
1
2
3
4.1

Sample Output:
YES
"""


def sign(a, b):
    if a > 0 and b > 0 or a < 0 and b < 0:
        return True
    return False


x1, y1, x2, y2 = (float(input()) for i in range(4))
print("YES" if all([sign(x1, x2), sign(y1, y2)]) else 'NO')
