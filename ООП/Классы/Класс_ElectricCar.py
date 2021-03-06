"""
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.
с. 180

Работа над новым классом не обязана начинаться с нуля. Если класс, который вы пишете,
представляет собой специализированную версию ранее написанного класса, вы можете воспользоваться наследованием.
Один класс, наследующий от другого, автоматически получает все атрибуты и методы первого класса.
Исходный класс называется родителем, а новый класс — потомком.
Класс-потомок наследует атрибуты и методы родителя, но при этом также может определять собственные атрибуты и методы.

Новый класс ElectricCar можно создать на базе класса Car, написанного ранее.

Любой метод родительского класса, который в моделируемой ситуации делает не то, что нужно, можно переопределить.
Для этого в классе-потомке определяется метод с тем же именем, что и у метода класса-родителя.
Python игнорирует метод родителя и обращает внимание только на метод, определенный в потомке.

Экземпляры как атрибуты: списки атрибутов и методов со временем растут,
и через какое-то время файлы становятся длинными и громоздкими.
В такой ситуации часть одного класса нередко можно записать в виде отдельного класса.
Большой код разбивается на меньшие классы, которые работают во взаимодействии друг с другом.
Например, при дальнейшей доработке класса ElectricCar может оказаться,
что в нем появилось слишком много атрибутов и методов, относящихся к аккумулятору.
В таком случае можно остановиться и переместить все эти атрибуты и методы в отдельный класс с именем Battery.

"""

from Класс_Battery import Battery
from Класс_Car import Car


class ElectricCar(Car):  # В определении потомка имя класса-родителя заключается в круглые скобки
    """ Представляет аспекты машины, специфические для электромобилей """

    def __init__(self, manufacturer, model, year):
        """ Инициирует атрибуты класса-родителя, затем инициализирует атрибуты, специфические для электромобиля """

        # Функция super() - специальная функция, которая позволяет вызвать метод родительского класса.
        # Эта строка приказывает Python вызвать метод __init__() класса Car,
        # в результате чего экземпляр ElectricCar получает доступ ко всем атрибутам класса-родителя.
        # Имя super происходит из терминологии: класс-родитель называется суперклассом, а класс-потомок — подклассом.
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):  # Переопределение метода класса-родителя
        """ У электромобилей нет бензобака """
        print(f"{self.manufacturer}: Этой машине не нужен бензин!")
