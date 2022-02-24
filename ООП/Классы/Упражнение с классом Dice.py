"""
УПРАЖНЕНИЯ
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.

9.13. Кубики: создайте класс Dice с одним атрибутом sides, который имеет значение по умолчанию 6.
Напишите метод roll_dice() для вывода случайного числа от 1 до количества граней на кубике.
Создайте экземпляр, представляющий 6-гранный кубик, и смоделируйте 10 бросков.

"""
from Класс_Dice import Dice

PLAY_TIMES = 10  # количество бросков

white_dice = Dice()
white_dice.roll_series(PLAY_TIMES)

blue_dice = Dice("синий", 10)
blue_dice.roll_series(PLAY_TIMES)

red_dice = Dice("красный", 20)
red_dice.roll_series(PLAY_TIMES)

yellow_dice = Dice("желтый", 8)
yellow_dice.roll_series(PLAY_TIMES)

green_dice = Dice("зеленый", 4)
green_dice.roll_series(PLAY_TIMES)

black_dice = Dice("черный", 6)
black_dice.roll_series(PLAY_TIMES, 1)
