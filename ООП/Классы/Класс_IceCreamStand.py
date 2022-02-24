""" Класс киоска с мороженым как подкласс класса ресторан """

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
