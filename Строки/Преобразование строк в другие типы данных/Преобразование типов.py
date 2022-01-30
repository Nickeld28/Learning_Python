salary = "50000"
year_salary = salary * 12
print(year_salary)  # строка повторена 12 раз, т.к. "50000" это не число

year_salary = int(salary) * 12  # преобразовали в число
print(year_salary)

salary = "50000.5"  # если содержит десятичную точку
# year_salary = int(salary) * 12 # преобразовали в число, но вышла ошибка
print(year_salary)

salary = "50000.5"  # если содержит десятичную точку
year_salary = float(salary) * 12  # преобразовали в число с десятичной точкой
print(year_salary)
# print("Ваша годовая зарплата: " + year_salary) # ошибка склейки строки с числом

print("Ваша годовая зарплата: " + str(year_salary))  # преобразуем число в строку
