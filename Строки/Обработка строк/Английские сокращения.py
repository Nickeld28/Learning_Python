# АНГЛИЙСКИЕ СОКРАЩЕНИЯ
# В английском языке приняты следующие сокращения:
#
# I am — I'm
# You are — You're
# He is — He's
# She is — She's
# It is — It's
# We are — We're
# They are — They're
# Напишите программу, которая получает из первого аргумента командной строки фразу на английском языке, а затем заменяет в ней все полные сочетания на сокращения (в соответствии со списком выше).
#
# Пример использования:
# > python program.py "I am programmer."
# > I'm programmer.

import sys
text = sys.argv[1]
text = text.\
    replace(" am", "'m").\
    replace(" are", "'re").\
    replace(" is", "'s")

print(text)





