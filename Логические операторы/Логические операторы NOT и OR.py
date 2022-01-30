# Введение
# Если перед переменной, которая содержит логическое значение поставить слово not,
# то значение переменной будет изменено на обратное.
#
# # Создаем переменную is_phone, содержащую логическое значение True.
is_phone = True
# Выводим оригинальное значение.
print(is_phone) # True
#
# # Выводим обратное значение.
print(not is_phone) # False

# Логическая операция or сравнивает несколько значений и возвращает True, если хотя бы одно из них будет логически верным:

# Создаем четыре логические переменные.
is_male = True
is_female = False
is_old = True
is_young = False

# Сравниваем: True или False.
# Получаем True, так как одна из переменных True.
print(is_male or is_female) #True

# Сравниваем: False или True (поменяли местами).
# Всё равно получаем True, так как одна из переменных True.
print(is_female or is_male) #True

# Сравниваем: False или False.
# Получаем False, так как нет True.
print(is_young or is_female) #False

# Сравниваем все переменные.
print(is_young or is_female or is_old or is_young) #True