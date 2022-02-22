"""
УПРАЖНЕНИЯ

9.3. Пользователи: создайте класс с именем User.
Создайте два атрибута first_name и last_name, а затем еще несколько атрибутов,
которые обычно хранятся в профиле пользователя. Напишите метод describe_user(),
который выводит сводку с информацией о пользователе.
Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.
"""


class User:
    """ Класс для упражнения 9.3 """

    def __init__(self, first_name, last_name, age, height, weight):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def describe_user(self):
        print(f"User {self.first_name} {self.last_name}, {self.age} years old")

    def greet_user(self):
        print(f"Hello, {self.first_name}!")


user1 = User("Vasya", "Pupkin", 25, 180, 76)
user2 = User("Vovochka", "Sidorov", 19, 167, 62)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
