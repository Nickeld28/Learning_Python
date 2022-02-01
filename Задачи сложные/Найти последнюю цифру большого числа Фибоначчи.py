"""
Найти последнюю цифру большого числа Фибоначчи
Дано число 1 ≤ n ≤ 10^7, необходимо найти последнюю цифру nn-го числа Фибоначчи.

Sample Input:
841645

Sample Output:
5
"""


def fib_last_digit(n):
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b


def main():
    n = int(input())
    print(fib_last_digit(n))


if __name__ == "__main__":
    main()
