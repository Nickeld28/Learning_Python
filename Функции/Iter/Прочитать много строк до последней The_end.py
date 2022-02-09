"""
Прочитайте последовательность строк до конца ('The_end').
Выведите через пробел все строки, кроме 'The_end'

Sample Input 1:
A some word
tree, sun
anywhere
be happy
The_end

Sample Output 1:
A some word tree, sun anywhere be happy

Sample Input 2:
qwerty, qwerty
history
math
georgraphic
The_end

Sample Output 2:
qwerty, qwerty history math georgraphic


Sample Input 3:
Start
sample, samPLe, SaMpLe
The_end

Sample Output 3:
Start sample, samPLe, SaMpLe
"""

s = [i for i in iter(input, 'The_end')]
print(*s)
