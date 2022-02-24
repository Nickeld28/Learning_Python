""" Класс представления батареи """


class Battery:
    """ Простая модель аккумулятора для электромобиля """

    def __init__(self, battery_size=75):
        """ Инициализирует атрибуты аккумулятора """
        self.battery_size = battery_size
        self.range_miles = 315

    def describe_battery(self):
        """ Выводит информацию о мощности аккумулятора """
        print(f"This car has a {self.battery_size}-kWh battery")

    def charge_battery(self):
        """ Подзарядка аккумулятора """
        print(f"Заряжаем аккумулятор! Общая емкость: {self.battery_size}-kWh")

    def get_range(self):
        """ Выводит приблизительный запас хода для аккумулятора """
        if self.battery_size == 75:
            self.range_miles = 260
        elif self.battery_size == 100:
            self.range_miles = 315
        print(f"This car can go about {self.range_miles} miles on a full charge.")

    def upgrade_battery(self):
        """ Увеличение мощности батареи """
        if self.battery_size < 100:
            self.battery_size = 100
            print(f"Upgraded successfully! The battery size now is:", self.battery_size)
