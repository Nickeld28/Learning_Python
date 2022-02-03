"""
Сколько вариантов следующего хода есть у шахматного короля, стоящего в клетке с заданными координатами?

Координаты клетки заданы двумя числами от 1 до 8. Сначала номер столбца, потом номер строки.
"""

# input:
x, y = int(input()), int(input())

# corner position check
if x in (1, 8) and y in (1, 8):
    print(3)

# edge position check
elif x in (1, 8) or y in (1, 8):
    print(5)

# free positions:
else:
    print(8)
