"""
УПРАЖНЕНИЯ
По книге "Изучаем Python" Эрика Мэтиза, 3-е издание, издательство ПИТЕР, 2020 г.

9.3. Пользователи: создайте класс с именем User.
Создайте два атрибута first_name и last_name, а затем еще несколько атрибутов,
которые обычно хранятся в профиле пользователя. Напишите метод describe_user(),
который выводит сводку с информацией о пользователе.
Создайте еще один метод greet_user() для вывода персонального приветствия для пользователя.
Создайте несколько экземпляров, представляющих разных пользователей. Вызовите оба метода для каждого пользователя.

9.5. Попытки входа: добавьте атрибут login_attempts в класс User из упражнения 9.3 (с. 175).
Напишите метод increment_login_attempts(), увеличивающий значение login_attempts на 1.
Напишите другой метод с именем reset_login_attempts(), обнуляющий значение login_attempts.
Создайте экземпляр класса User и вызовите increment_login_attempts() несколько раз.
Выведите значение login_attempts, чтобы убедиться в том, что значение было изменено правильно,
а затем вызовите reset_login_attempts(). Снова выведите login_attempts и убедитесь в том, что значение обнулилось.

"""

from Класс_User import User

user1 = User("Vasya", "Pupkin", 25, 180, 76)
user2 = User("Vovochka", "Sidorov", 19, 167, 62)

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user2.login_attempts = 5
print(user2.login_attempts)

user2.increment_login_attempts(8)
print(user2.login_attempts)

user2.reset_login_attempts()
print(user2.login_attempts)
