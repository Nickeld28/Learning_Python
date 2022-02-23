"""
Объектно-ориентированное программирование

Ресурс программиста - концентрация внимания

Помощь программисту - ограничить область текущей видимости (имен), сузить решаемую задачу, документировать задачу.
Функции, модули, классы - создаются для помощи программисту и помогают структурировать программный код.

Объект имеет свои свойства и поведение. Объект относится к типу объектов. Класс определяет поведение объектов и свойств.
Класс позволяет конструировать объекты.
Объект - экземпляр класса.
UML - объединенный язык моделирования.
Диаграмма классов. Проектируется модель на бумаге в виде схемы взаимодействия и необходимости создания новых классов.

"""


class Dragon:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def get_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def talk(self):
        print(self.name, 'health', self.health, '. Hit me!')

    def final_cry(self):
        print(self.name, 'AAaaaaaa!')


def main():
    enemy_list = [Dragon('Smaug'), Dragon('Hidra')]
    finish = False
    while not finish:
        enemy = enemy_list[0]
        enemy.talk()
        damage = int(input())
        enemy.get_damage(damage)
        if not enemy.is_alive():  # удалить из списка мертвого врага
            enemy.final_cry()
            enemy_list.pop(0)
        finish = not enemy_list  # проверить пуст ли список врагов
    print('You win')


main()


class PositiveInt:
    __a = 0
    __counter = 0

    def set_a(self, a):
        self.__counter += 1
        if a >= 0:
            self.__a = int(a)
        else:
            print("Wrong parameter, an internal state won't change.")

    def get_a(self):
        print("Was set", self.__counter, "times.")
        return self.__a


if __name__ == "__main__":
    value = PositiveInt()

    print(value.get_a())

    value.set_a(10)
    print(value.get_a())

    value.set_a(-10)
    print(value.get_a())
