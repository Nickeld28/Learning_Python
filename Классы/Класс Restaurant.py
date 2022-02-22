"""
УПРАЖНЕНИЯ

9.1. Ресторан: создайте класс с именем Restaurant.
Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type.
Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(),
который выводит сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем restaurant.
Выведите два атрибута по отдельности, затем вызовите оба метода.

9.2. Три ресторана: начните с класса из упражнения 9.1.
Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant().
"""


class Restaurant:
    """ Класс ресторан для упражнения 9.1 """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open")


restaurant = Restaurant("Golden Dragon", "Chinese cuisine")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_1 = Restaurant("Drunk bear", "Russian cuisine")
restaurant_2 = Restaurant("French bouquet", "French cuisine")
restaurant_3 = Restaurant("Mightiness of Rome", "Italian cuisine")

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
