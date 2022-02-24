"""
УПРАЖНЕНИЯ
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.

9.9. Обновление аккумулятора: используйте окончательную версию программы electric_car.py из этого раздела.
Добавьте в класс Battery метод с именем upgrade_battery().
Этот метод должен проверять размер аккумулятора и устанавливать мощность равной 100, если она имеет другое значение.
Создайте экземпляр электромобиля с аккумулятором по умолчанию, вызовите get_range(),
а затем вызовите get_range() во второй раз после вызова upgrade_battery().
Убедитесь в том, что запас хода увеличился.

"""

from Класс_ElectricCar import ElectricCar

my_tesla = ElectricCar('Tesla', 'Model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.charge_battery()
print(my_tesla.battery.range_miles)
my_tesla.battery.get_range()
print(my_tesla.battery.range_miles)

# К упражнению 9.9:
my_nissan = ElectricCar("Nissan", "Leaf", 2021)
print(my_nissan.get_descriptive_name())
my_nissan.battery.get_range()
my_nissan.battery.upgrade_battery()
my_nissan.battery.get_range()
