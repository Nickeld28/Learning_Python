""" Представление класса администратор как подкласс класса пользователь """

from Класс_Priveileges import Privileges as Prv  # использование псевдонима при импорте
from Класс_User import User


class Admin(User):
    """ Класс администратор, это такой пользователь, имеющий привелегии """

    def __init__(self, first_name, last_name, age, height, weight):
        """ Инициирует атрибуты класса-родителя, затем инициализирует атрибуты, специфические для администратора """
        super().__init__(first_name, last_name, age, height, weight)
        self.privileges = Prv()  # здесь создается экземпляр класса с использованием псевдонима
