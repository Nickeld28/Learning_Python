"""
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.
с. 175

Создадим атрибут, который будет менять со временем свои значения. В случае машины это ее пробег.
Создадим в методе __init__ атрибут odometer_reading и присвоим ему значение 0.
"""


class Car:
    """ Простая модель автомобиля """

    def __init__(self, manufacturer, model, year):
        """ Инициализирует атрибуты описания автомобиля """
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """ Возвращает аккуратно отформатированное описание """
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """ Выводит пробег машины в милях """
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """ Устанавливает заданное значение на одометре """
        self.odometer_reading = mileage

    def new_update_odometer(self, mileage):
        """
        Устанавливает заданное значение на одометр.
        При попытке обратной подкрутки счетчика изменение отклоняется
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """ Увеличивает показания одометра с заданным приращением """
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        """ Осуществляет заправку автомобиля бензином """
        print(f"{self.manufacturer}: Заливаем полный бензобак!")


if __name__ == '__main__':
    my_new_car = Car('Audi', 'a4', 2019)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()

    # Рассмотрим три способа изменения значения атрибутов

    # 1) - Прямое изменение значения атрибута через экземпляр
    my_new_car.odometer_reading = 23  # иногда такие изменения допустимы, но чаще используются вспомогательные методы
    my_new_car.read_odometer()

    # 2) - Изменение значения атрибута с использованием метода update_odometer()
    my_new_car.update_odometer(30)
    my_new_car.read_odometer()

    my_new_car.new_update_odometer(35)
    my_new_car.read_odometer()
    my_new_car.new_update_odometer(25)  # пресеклась попытка уменьшить счетчик!
    my_new_car.read_odometer()

    # 3) - Изменение значения атрибута с приращением с помощью метода increment_odometer()
    my_new_car.increment_odometer(10)
    my_new_car.read_odometer()

    my_used_car = Car("Subaru", "Outback", 2015)
    print(my_used_car.get_descriptive_name())
    my_used_car.new_update_odometer(23_500)
    my_used_car.read_odometer()
    my_used_car.increment_odometer(100)
    my_used_car.read_odometer()
    my_used_car.fill_gas_tank()
