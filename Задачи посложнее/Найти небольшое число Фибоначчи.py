"""
Найти небольшое число Фибоначчи


Дано целое число 1 ≤ n ≤ 40, необходимо вычислить n-е число Фибоначчи

Sample Input:
3
Sample Output:
2
"""


def fib_num(n):
    lst = [0, 1] + [0] * (n - 1)
    if n <= 1:
        return 1
    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]
    return lst[n]


def main():
    n = int(input())
    print(fib_num(n))


if __name__ == "__main__":
    main()
