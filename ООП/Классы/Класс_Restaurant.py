""" Класс представления ресторана """


class Restaurant:
    """ Класс ресторан для упражнения 9.1 """

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name, self.cuisine_type)

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name} is open")

    def set_number_served(self, number_served):
        if number_served > self.number_served:
            self.number_served = number_served
        else:
            print("You can't decrease the value")

    def increment_number_served(self, value):
        if value >= 0:
            self.number_served += value
        else:
            print("You can't decrease the value")
