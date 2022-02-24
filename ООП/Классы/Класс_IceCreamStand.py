"""
УПРАЖНЕНИЯ
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.

9.6. Киоск с мороженым: киоск с мороженым — особая разновидность ресторана. Напишите класс IceCreamStand,
наследующий от класса Restaurant из упражнения 9.1 (с. 175) или упражнения 9.4 (с. 180).
Подойдет любая версия класса; просто выберите ту, которая вам больше нравится.
Добавьте атрибут с именем flavors для хранения списка сортов мороженого.
Напишите метод, который выводит этот список. Создайте экземпляр IceCreamStand и вызовите этот метод.

"""

from Класс_Restaurant import Restaurant


class IceCreamStand(Restaurant):
    """ Представляет такой подкласс ресторана, в виде киоска с мороженым """
    def __init__(self, restaurant_name, cuisine_type):
        """ Инициирует атрибуты класса-родителя, затем инициализирует атрибуты, специфические для киоска с мороженым """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["Chocolate ice cream", "Vanilla ice cream",
                        "Strawberry ice cream", "Rocky road ice cream",
                        "Cookies-and-cream ice cream", "Eskimo pie",
                        "Butter Pecan ice cream"]

    def get_flavors(self):
        """ Выводит список видов мороженого """
        print(f"Flavors {self.restaurant_name} is:", end=" ")
        print(*self.flavors, sep=', ')

if __name__ == '__main__':
    little_red_stand = IceCreamStand("Yummy", "Ice cream")
    little_red_stand.describe_restaurant()
    little_red_stand.get_flavors()
