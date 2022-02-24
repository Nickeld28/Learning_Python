""" Представляет класс игральная кость (кубик) """

from random import randint


class Dice:
    """ Класс игральная кость """

    def __init__(self, color="белый", sides=6):
        """
         Инизиализирует атрибуты игрального кубика
        :param color: цвет кубика, по умолчанию - белый
        :param sides: количество граней, по умолчанию - 6
        """
        self.sides = sides  # количество граней кубики
        self.color = color  # цвет игрального кубика
        self.value = 1  # текущее значение на кубике
        self.count = 0  # счетчик выпадения интересующего значения в серии бросков

    def roll_dice(self):
        """ Метод бросания игрального кубика """
        self.value = randint(1, self.sides)
        print("Выпало число:", self.value)

    def roll_series(self, attempts, number=0):
        """
         Метод для выполнения серии бросков кубика и подсчета сколько раз выпадет заданное значение
        :param attempts: целое число - количество бросков
        :param number: целое число - интересующее значение для подсчета, по умолчанию - максимальное на кубике
        :return: печатает одну строку на каждый бросок кубика и выводит счетчик в конце
        """
        self.count = 0  # обнуляем счетчик бросков перед серией
        if number == 0:  # если значение по умолчанию, то подставляем максимально возможное число на кубике
            number = self.sides
        for i in range(attempts):
            print(f"Бросаем {self.color} кубик. У него {self.sides} граней. Попытка №{i + 1}: ", end="")
            self.roll_dice()
            if self.value == number:
                self.count += 1
        print(f"Значение {number} выпало на кубике {self.count} раз из {attempts}")
        print()
