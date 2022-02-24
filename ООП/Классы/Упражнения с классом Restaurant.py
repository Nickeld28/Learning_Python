"""
УПРАЖНЕНИЯ
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.

9.1. Ресторан: создайте класс с именем Restaurant.
Метод __init__() класса Restaurant должен содержать два атрибута: restaurant_name и cuisine_type.
Создайте метод describe_restaurant(), который выводит два атрибута, и метод open_restaurant(),
который выводит сообщение о том, что ресторан открыт.
Создайте на основе своего класса экземпляр с именем restaurant.
Выведите два атрибута по отдельности, затем вызовите оба метода.

9.2. Три ресторана: начните с класса из упражнения 9.1.
Создайте три разных экземпляра, вызовите для каждого экземпляра метод describe_restaurant().

9.4. Посетители: начните с программы из упражнения 9.1 (с. 175).
Добавьте атрибут number_served со значением по умолчанию 0; он представляет количество обслуженных посетителей.
Создайте экземпляр с именем restaurant. Выведите значение number_served, потом измените и выведите снова.
Добавьте метод с именем set_number_served(), позволяющий задать количество обслуженных посетителей.
Вызовите метод с новым числом, снова выведите значение.
Добавьте метод с именем increment_number_served(),
который увеличивает количество обслуженных посетителей на заданную величину.
Вызовите этот метод с любым числом, которое могло бы представлять количество обслуженных клиентов,
— скажем, за один день.

9.10. Импортирование класса Restaurant: возьмите последнюю версию класса Restaurant и сохраните ее в модуле.
Создайте отдельный файл, импортирующий класс Restaurant.
Создайте экземпляр Restaurant и вызовите один из методов Restaurant, чтобы показать,
что команда import работает правильно.

"""

from Класс_Restaurant import Restaurant

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

print(restaurant_1.number_served)
restaurant_1.number_served = 5
print(restaurant_1.number_served)

restaurant_1.set_number_served(15)
print(restaurant_1.number_served)

restaurant_2.increment_number_served(34)
print(restaurant_2.number_served)
