""" Представление класса пользователь """


class User:
    """ Класс для упражнения 9.3 """

    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.login_attempts = 0

    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}, {self.age} years old")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")

    def increment_login_attempts(self, number):
        if number > 0:
            self.login_attempts = number

    def reset_login_attempts(self):
        self.login_attempts = 0
