# комментарий

# integer = int
number = 5

# float
fnumber = 5.7
age = 35

# str
name = "Ripper"

# bool
status = True
# либо False

print("Пример вывода текста")
print(name)

# Экранирование
print("Пример \"c\" кавычками")
# или можно так
print('Пример "c" кавычками')

print('Привет мир!')
# перенос сроки через команду \n
print('Привет \nмир!')

# или вот так
print('Привет')
print('мир!')

# Конкатенация
# can only concatenate str (not "int") to str
# функция str() переводит int в строку
print("Привет, меня зовут " + name + "!")
print("Мне " + str(age) + " лет!")

# функция input - ввод данных
name_2 = input("Введите свое имя: ")
age2 = input("Укажите свой возраст: ")
print("Привет, " + name_2 + "!")
print("Тебе уже " + age2 + " лет!")
