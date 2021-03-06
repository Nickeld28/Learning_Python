# \n - спецсимвол перехода на новую строку
lang1 = "python"
lang2 = "javascript"
lang3 = "sql"

print(lang1, lang2, lang3, sep=', ', end='.\n')  # python, javascript, sql.

langs = "python\njavascript\nsql"
print(langs)
# каждый язык будет на новой строке:
# python
# javascript
# sql

# \t - спецсимвол табуляции
langs = "Языки:\n\tpython\n\tjavascript\n\tsql"
print(langs)
# в строке langs сейчас 37 символов (не включая кавычки, конечно)
# но если напечатать длинну строки langs, то получим 31 символ:
print(len(langs))
# это потому, что \n или \t считается одним символом
# Если возьмем python в кавычки, то получится ошибка:
# langs = "Языки:\n\t"python"\n\tjavascript\n\tsql"
# \" - спецсимвол, позволяющий вставить кавычки:
langs = "Языки:\n\t\"python\"\n\t\'javascript\'\n\tsql"
print(langs)
# Если кавычки внутри строки совпадают с крайними кавычками будет ошибка, но если использовать разные кавычки то можно так:
langs = "Языки:\n\t'python'\n\tjavascript\n\tsql"
print(langs)
# или наоборот:
langs = 'Языки:\n\t"python"\n\tjavascript\n\tsql'
print(langs)

# \\ - спецсимвол для отображения обратного слэша

# """ - использование тройных кавычек позволяет сократить код, вместо \n использовать настоящий переход строки,
# вместо \t использовать настоящую табуляцию, а вместо \" использовать кавычки без слэша
langs = """Языки:
    "python"
    'javascript'
    \\sql\\"""  # но для отображения слэша все равно нужен двойной слэш
print(langs)
# Тройные кавычки могут быть одинарными ''' или двойными """, главное одинаковыми с двух сторон.
