import unittest


def fib(n):
    """
    Функция вычисляет число Фибоначчи номер n.
    Выбрасывает исключение TypeError, если вызвана не для целочисленного типа.
    Выбрасывает исключает ValueError, если число отрицательное или больше допустимого.
    :param n: целое число от 0 до 9999
    :return: целое число от 0 до ...
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci function can work with <class 'int'> type only.")
    if n < 0:
        raise ValueError("Fibonacci function can't work with negative numbers.")
    if n >= 10000:
        raise ValueError("Fibonacci function can't work with numbers larger than 9999.")
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


class TestFibonacci(unittest.TestCase):

    def test_simple(self):
        for param, result in [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)]:
            self.assertEqual(fib(param), result)

    def test_stress(self):
        self.assertEqual(fib(9999), fib(9998) + fib(9997))

        with self.assertRaises(ValueError):
            fib(10000)

    def test_negative(self):
        with self.assertRaises(ValueError):
            fib(-1)
        with self.assertRaises(ValueError):
            fib(-100)

    def test_wrong_param_type(self):
        with self.assertRaises(TypeError):
            fib(2.5)
        with self.assertRaises(TypeError):
            fib("Hello")


if __name__ == '__main__':
    # Запускается не наш класс, а функция main из библиотеки unittest.
    # Она пробежится по всем классам, которые являются потомками класса TestCase и вызовет все функции,
    # которые начинаются со слова "test_"
    unittest.main()
