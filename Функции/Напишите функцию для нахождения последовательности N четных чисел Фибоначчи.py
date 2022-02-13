"""
Напишите функцию, которая принимает аргумент N (целое число),
а на выходе возвращается N четных элементов последовательности Фибоначчи.
"""


def even_fib_numbers(n: int):
    """ Функция возвращает первые n четных чисел Фибоначчи.
        Принимает один обязательный аргумент n.
    """

    result, fib = [0], [0, 1]
    while n > 1:
        fib_number = fib[-1] + fib[-2]
        fib.append(fib_number)
        if fib_number % 2 == 0:
            result.append(fib_number)
            n -= 1
    return result


if __name__ == "__main__":
    print('Тестируем:', "even_fib_numbers\n", even_fib_numbers.__doc__)

    num = 4
    print("testcase #1: n =", num, end=", ")
    right_result = [0, 2, 8, 34]
    print('OK' if right_result == even_fib_numbers(num) else 'FAIL')

    num = 6
    print("testcase #2: n =", num, end=", ")
    right_result = [0, 2, 8, 34, 144, 610]
    print('OK' if right_result == even_fib_numbers(num) else 'FAIL')

    num = 8
    print("testcase #3: n =", num, end=", ")
    right_result = [0, 2, 8, 34, 144, 610, 2584, 10946]
    print('OK' if right_result == even_fib_numbers(num) else 'FAIL')
