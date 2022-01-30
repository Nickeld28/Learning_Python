"""
вычисления
 +, -, *, **, %, унарный минус, округление, Пи
"""

a = 5
b = 10
c = a + b
u = a * b
d = a / b
s = a ** b
o = a % b
print(c)
print(u)
print(d)
print(s)
print(o)

# унарный минус
m = 10
m = - m
print(m)

# округление

r = 5.65
print(round(r))

import math

e = 5.25
# в меньшую сторону
print(math.floor(e))
# в большую сторону
print(math.ceil(e))

# Пи
import math

print(math.pi)
